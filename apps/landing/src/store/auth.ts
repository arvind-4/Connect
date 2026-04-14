const rootDiv = document.querySelector("#root") as HTMLElement;
export const is_authenticated = rootDiv.getAttribute("data-is_authenticated") ?? false;
