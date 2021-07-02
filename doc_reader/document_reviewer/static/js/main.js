let voices = speechSynthesis.getVoices();
let defaultVoice;

speechSynthesis.onvoiceschanged = () => {
  voices = speechSynthesis.getVoices();
  defaultVoice = voices.find((voice) => voice.name === "Google русский");

  wrapper.addEventListener("click", handleClick);
  window.addEventListener("keydown", handleKeydown);
};

const PLAY = "play";
const PAUSE = "pause";
const RESUME = "resume";

function handleClick({ target }) {
  switch (target.className) {
    case PLAY:
      speechSynthesis.cancel();

      const { textContent } = target.nextElementSibling;

      textContent.split(".").forEach((text) => {
        const trimmed = text.trim();
        if (trimmed) {
          const U = getUtterance(target, text);
          speechSynthesis.speak(U);
        }
      });
      break;
    case PAUSE:
      target.className = RESUME;
      speechSynthesis.pause();
      break;
    case RESUME:
      target.className = PAUSE;
      speechSynthesis.resume();
      break;
    default:
      break;
  }
}

function handleKeydown({ code }) {
  switch (code) {
    case "Escape":
      return speechSynthesis.cancel();
    default:
      break;
  }
}

function getUtterance(target, text) {
  const U = new SpeechSynthesisUtterance(text);
  U.voice = defaultVoice;
  U.lang = defaultVoice.lang;
  U.volume = 1;
  U.rate = 1;
  U.pitch = 1;

  U.onstart = () => {
    console.log("Started");
    target.className = PAUSE;
  };
  U.onend = () => {
    console.log("Finished");
    target.className = PLAY;
  };
  U.onerror = (err) => console.error(err);

  return U;
}
