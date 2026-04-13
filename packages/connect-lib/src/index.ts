type PeerEntry = [RTCPeerConnection, RTCDataChannel];

interface SignalMessage {
  peer: string;
  action: string;
  message: any;
  room_id: string;
}

const mapPeers: Record<string, PeerEntry> = {};

const localVideo = document.querySelector(
  '#local-video',
) as HTMLVideoElement;

let localStream: MediaStream = new MediaStream();

const btnToggleAudio = document.querySelector(
  '#btn-toggle-audio',
) as HTMLButtonElement;
const btnToggleVideo = document.querySelector(
  '#btn-toggle-video',
) as HTMLButtonElement;

const messageInput = document.querySelector(
  '#msg',
) as HTMLInputElement;
const btnSendMsg = document.querySelector(
  '#btn-send-msg',
) as HTMLButtonElement;

const ul = document.querySelector(
  '#message-list',
) as HTMLUListElement;

const room_id: string = JSON.parse(
  (document.getElementById('json-room_id') as HTMLElement)
    .textContent || '""',
);

const start = window.location.protocol === 'https:' ? 'wss' : 'ws';

const endPoint = `${start}://${window.location.host}/${start}/${room_id}/`;

let webSocket: WebSocket;

const usernameInput = document.querySelector(
  '#username',
) as HTMLInputElement;
let username: string;

const btnJoin = document.querySelector(
  '#btn-join',
) as HTMLButtonElement;

btnJoin.onclick = () => {
  username = usernameInput.value;

  if (!username) {
    alert(`The Username can't be Null!`);
    return;
  }

  document.getElementById('complete-div')?.remove();

  webSocket = new WebSocket(endPoint);

  webSocket.onopen = () => {
    sendSignal('new-peer', {});
  };

  webSocket.onmessage = webSocketOnMessage;

  btnSendMsg.disabled = false;
  messageInput.disabled = false;
};

function webSocketOnMessage(event: MessageEvent) {
  const parsedData = JSON.parse(event.data);

  const action = parsedData.action;
  const peerUsername = parsedData.peer;

  if (peerUsername === username) return;

  const receiver_channel_name =
    parsedData.message.receiver_channel_name;

  if (action === 'new-peer') {
    createOfferer(peerUsername, receiver_channel_name);
    return;
  }

  if (action === 'new-offer') {
    const offer = parsedData.message.sdp;
    createAnswerer(offer, peerUsername, receiver_channel_name);
    return;
  }

  if (action === 'new-answer') {
    const peer = mapPeers[peerUsername][0];
    const answer = parsedData.message.sdp;
    peer.setRemoteDescription(answer);
  }
}

messageInput.addEventListener('keyup', (event: KeyboardEvent) => {
  if (event.key === 'Enter') {
    event.preventDefault();
    btnSendMsg.click();
  }
});

btnSendMsg.onclick = btnSendMsgOnClick;

function btnSendMsgOnClick() {
  const message = messageInput.value;

  if (!message) {
    // @ts-ignore (if Swal not typed)
    Swal.fire({
      icon: 'error',
      title: 'Oops ...',
      text: `Message Can't be Empty!`,
    });
    return;
  }

  const li = document.createElement('li');
  li.appendChild(document.createTextNode(`Me: ${message}`));
  ul.appendChild(li);

  const dataChannels = getDataChannels();
  dataChannels.forEach((dc) => {
    dc.send(`${username}: ${message}`);
  });

  messageInput.value = '';
}

const constraints: MediaStreamConstraints = {
  video: true,
  audio: true,
};

navigator.mediaDevices
  .getUserMedia(constraints)
  .then((stream: MediaStream) => {
    localStream = stream;
    localVideo.srcObject = stream;
    localVideo.muted = true;

    const audioTracks = stream.getAudioTracks();
    const videoTracks = stream.getVideoTracks();

    btnToggleAudio.onclick = () => {
      audioTracks[0].enabled = !audioTracks[0].enabled;
    };

    btnToggleVideo.onclick = () => {
      videoTracks[0].enabled = !videoTracks[0].enabled;
    };
  })
  .catch((error: unknown) => {
    console.error('Error accessing media devices.', error);
  });

function sendSignal(action: string, message: any) {
  const data: SignalMessage = {
    peer: username,
    action,
    message,
    room_id,
  };

  webSocket.send(JSON.stringify(data));
}

function createOfferer(
  peerUsername: string,
  receiver_channel_name: string,
) {
  const peer = new RTCPeerConnection();

  addLocalTracks(peer);

  const dc = peer.createDataChannel('channel');

  dc.onopen = () => console.log('Connection opened.');
  dc.onmessage = dcOnMessage;

  const remoteVideo = createVideo(peerUsername);

  setOnTrack(peer, remoteVideo);

  mapPeers[peerUsername] = [peer, dc];

  peer.oniceconnectionstatechange = () => {
    const state = peer.iceConnectionState;

    if (['failed', 'disconnected', 'closed'].includes(state)) {
      delete mapPeers[peerUsername];
      if (state !== 'closed') peer.close();
      removeVideo(remoteVideo);
    }
  };

  peer.onicecandidate = (event) => {
    if (event.candidate) return;

    sendSignal('new-offer', {
      sdp: peer.localDescription,
      receiver_channel_name,
    });
  };

  peer.createOffer().then((o) => peer.setLocalDescription(o));

  return peer;
}

function createAnswerer(
  offer: RTCSessionDescriptionInit,
  peerUsername: string,
  receiver_channel_name: string,
) {
  const peer = new RTCPeerConnection();

  addLocalTracks(peer);

  const remoteVideo = createVideo(peerUsername);

  setOnTrack(peer, remoteVideo);

  peer.ondatachannel = (e: RTCDataChannelEvent) => {
    const dc = e.channel;

    dc.onmessage = dcOnMessage;
    dc.onopen = () => console.log('Connection opened.');

    mapPeers[peerUsername] = [peer, dc];
  };

  peer.oniceconnectionstatechange = () => {
    const state = peer.iceConnectionState;

    if (['failed', 'disconnected', 'closed'].includes(state)) {
      delete mapPeers[peerUsername];
      if (state !== 'closed') peer.close();
      removeVideo(remoteVideo);
    }
  };

  peer.onicecandidate = (event) => {
    if (event.candidate) return;

    sendSignal('new-answer', {
      sdp: peer.localDescription,
      receiver_channel_name,
    });
  };

  peer
    .setRemoteDescription(offer)
    .then(() => peer.createAnswer())
    .then((a) => peer.setLocalDescription(a))
    .catch((error) => {
      console.error(
        `Error creating answer for ${peerUsername}`,
        error,
      );
    });

  return peer;
}

function dcOnMessage(event: MessageEvent) {
  const li = document.createElement('li');
  li.appendChild(document.createTextNode(event.data));
  ul.appendChild(li);
}

function getDataChannels(): RTCDataChannel[] {
  return Object.values(mapPeers).map(([_, dc]) => dc);
}

function getPeers(
  peerStorageObj: Record<string, PeerEntry>,
): RTCPeerConnection[] {
  return Object.values(peerStorageObj).map(([peer]) => peer);
}

function createVideo(peerUsername: string): HTMLVideoElement {
  const videoContainer = document.querySelector(
    '#video-container',
  ) as HTMLElement;

  const remoteVideo = document.createElement('video');
  remoteVideo.id = `${peerUsername}-video`;
  remoteVideo.autoplay = true;
  remoteVideo.playsInline = true;

  const videoWrapper = document.createElement('div');

  videoContainer.appendChild(videoWrapper);
  videoWrapper.appendChild(remoteVideo);

  const pTag = document.createElement('p');
  pTag.className = 'text-center text-xl text-gray-700 font-bold mb-2';
  pTag.innerHTML = peerUsername;

  videoWrapper.appendChild(pTag);

  return remoteVideo;
}

function setOnTrack(
  peer: RTCPeerConnection,
  remoteVideo: HTMLVideoElement,
) {
  const remoteStream = new MediaStream();
  remoteVideo.srcObject = remoteStream;

  peer.addEventListener('track', (event: RTCTrackEvent) => {
    remoteStream.addTrack(event.track);
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
