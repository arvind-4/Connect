type PeerEntry = [RTCPeerConnection, RTCDataChannel];

interface SignalPayload {
  sdp?: RTCSessionDescriptionInit;
  receiver_channel_name?: string;
}

interface SignalMessage {
  peer: string;
  action: "new-peer" | "new-offer" | "new-answer";
  message: SignalPayload;
  room_id: string;
}

const mapPeers: Record<string, PeerEntry> = {};

function getEl<T extends HTMLElement>(selector: string, type: { new (): T }): T {
  const el = document.querySelector(selector);
  if (!(el instanceof type)) {
    throw new Error(`${selector} not found or wrong type`);
  }
  return el;
}

const localVideo = getEl("#local-video", HTMLVideoElement);
const btnToggleAudio = getEl("#btn-toggle-audio", HTMLButtonElement);
const btnToggleVideo = getEl("#btn-toggle-video", HTMLButtonElement);
const messageInput = getEl("#msg", HTMLInputElement);
const btnSendMsg = getEl("#btn-send-msg", HTMLButtonElement);
const ul = getEl("#message-list", HTMLUListElement);
const usernameInput = getEl("#username", HTMLInputElement);
const btnJoin = getEl("#btn-join", HTMLButtonElement);

let localStream: MediaStream = new MediaStream();

function safeParseString(value: string): string {
  try {
    const parsed: unknown = JSON.parse(value);
    return typeof parsed === "string" ? parsed : "";
  } catch {
    return "";
  }
}

const room_id = safeParseString(getEl("#json-room_id", HTMLElement).textContent);

const start = window.location.protocol === "https:" ? "wss" : "ws";
const endPoint = `${start}://${window.location.host}/${start}/${room_id}/`;

let webSocket: WebSocket;
let username = "";

btnJoin.onclick = () => {
  username = usernameInput.value.trim();

  if (!username) {
    alert(`The Username can't be Null!`);
    return;
  }

  document.getElementById("complete-div")?.remove();

  webSocket = new WebSocket(endPoint);

  webSocket.onopen = () => {
    sendSignal("new-peer", {});
  };

  webSocket.onmessage = webSocketOnMessage;

  btnSendMsg.disabled = false;
  messageInput.disabled = false;
};

function parseMessage(data: string): SignalMessage | null {
  try {
    return JSON.parse(data) as SignalMessage;
  } catch {
    return null;
  }
}

function webSocketOnMessage(event: MessageEvent<string>) {
  const parsedData = parseMessage(event.data);
  if (!parsedData) return;

  const { action, peer, message } = parsedData;

  if (peer === username) return;

  const receiver = message.receiver_channel_name ?? "";

  switch (action) {
    case "new-peer":
      createOfferer(peer, receiver);
      break;

    case "new-offer":
      if (message.sdp) {
        createAnswerer(message.sdp, peer, receiver);
      }
      break;

    case "new-answer": {
      const peerEntry = mapPeers[peer];
      if (peerEntry && message.sdp) {
        void peerEntry[0].setRemoteDescription(message.sdp);
      }
      break;
    }
  }
}

btnSendMsg.onclick = () => {
  const message = messageInput.value.trim();
  if (!message) return;

  const li = document.createElement("li");
  li.textContent = `Me: ${message}`;
  ul.appendChild(li);

  getDataChannels().forEach((dc) => {
    dc.send(`${username}: ${message}`);
  });

  messageInput.value = "";
};

navigator.mediaDevices
  .getUserMedia({ video: true, audio: true })
  .then((stream) => {
    localStream = stream;
    localVideo.srcObject = stream;
    localVideo.muted = true;

    const [audioTrack] = stream.getAudioTracks();
    const [videoTrack] = stream.getVideoTracks();

    btnToggleAudio.onclick = () => {
      if (audioTrack) audioTrack.enabled = !audioTrack.enabled;
    };

    btnToggleVideo.onclick = () => {
      if (videoTrack) videoTrack.enabled = !videoTrack.enabled;
    };
  })
  .catch((error: unknown) => {
    console.error("Media error:", error);
  });

function sendSignal(action: SignalMessage["action"], message: SignalPayload) {
  const data: SignalMessage = {
    peer: username,
    action,
    message,
    room_id,
  };

  webSocket.send(JSON.stringify(data));
}

function createOfferer(peerUsername: string, receiver: string) {
  const peer = new RTCPeerConnection();
  addLocalTracks(peer);

  const dc = peer.createDataChannel("channel");
  dc.onmessage = dcOnMessage;

  const remoteVideo = createVideo(peerUsername);
  setOnTrack(peer, remoteVideo);

  mapPeers[peerUsername] = [peer, dc];

  peer.oniceconnectionstatechange = () => {
    const state = peer.iceConnectionState;
    if (["failed", "disconnected", "closed"].includes(state)) {
      cleanupPeer(peerUsername, remoteVideo, peer);
    }
  };

  peer.onicecandidate = (event) => {
    if (event.candidate) return;
    const sdp = peer.localDescription;
    if (!sdp) return;
    sendSignal("new-offer", {
      sdp: sdp,
      receiver_channel_name: receiver,
    });
  };

  void peer.createOffer().then((o) => peer.setLocalDescription(o));
}

function createAnswerer(offer: RTCSessionDescriptionInit, peerUsername: string, receiver: string) {
  const peer = new RTCPeerConnection();
  addLocalTracks(peer);

  const remoteVideo = createVideo(peerUsername);
  setOnTrack(peer, remoteVideo);

  peer.ondatachannel = (e) => {
    const dc = e.channel;
    dc.onmessage = dcOnMessage;

    mapPeers[peerUsername] = [peer, dc];
  };

  peer.oniceconnectionstatechange = () => {
    const state = peer.iceConnectionState;
    if (["failed", "disconnected", "closed"].includes(state)) {
      cleanupPeer(peerUsername, remoteVideo, peer);
    }
  };

  peer.onicecandidate = (event) => {
    if (event.candidate) return;
    const sdp = peer.localDescription;
    if (!sdp) return;
    sendSignal("new-answer", {
      sdp: sdp,
      receiver_channel_name: receiver,
    });
  };

  void peer
    .setRemoteDescription(offer)
    .then(() => peer.createAnswer())
    .then((a) => peer.setLocalDescription(a))
    .catch((error: unknown) => {
      console.error("Answer error:", error);
    });
}

function cleanupPeer(username: string, video: HTMLVideoElement, peer: RTCPeerConnection) {
  Reflect.deleteProperty(mapPeers, username);

  peer.close();
  removeVideo(video);
}

function dcOnMessage(event: MessageEvent<string>) {
  const li = document.createElement("li");
  li.textContent = event.data;
  ul.appendChild(li);
}

function getDataChannels(): RTCDataChannel[] {
  return Object.values(mapPeers).map(([, dc]) => dc);
}

function createVideo(peerUsername: string): HTMLVideoElement {
  const container = getEl("#video-container", HTMLElement);

  const video = document.createElement("video");
  video.autoplay = true;
  video.playsInline = true;

  const wrapper = document.createElement("div");
  const label = document.createElement("p");

  label.textContent = peerUsername;

  wrapper.append(video, label);
  container.appendChild(wrapper);

  return video;
}

function setOnTrack(peer: RTCPeerConnection, video: HTMLVideoElement) {
  const stream = new MediaStream();
  video.srcObject = stream;

  peer.addEventListener("track", (event) => {
    stream.addTrack(event.track);
  });
}

function addLocalTracks(peer: RTCPeerConnection) {
  localStream.getTracks().forEach((track) => {
    peer.addTrack(track, localStream);
  });
}

function removeVideo(video: HTMLVideoElement) {
  video.parentElement?.remove();
}
