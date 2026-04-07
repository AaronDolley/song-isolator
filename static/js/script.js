let isPlaying = false;

function togglePlay() {
    const audios = document.querySelectorAll(".stem-audio");

    if (!isPlaying) {
        audios.forEach(audio => {
            audio.play().catch(err => console.log(err));
        });
        isPlaying = true;
    } else {
        audios.forEach(audio => audio.pause());
        isPlaying = false;
    }
    console.log("Play button clicked");
}

function toggleMute(button) {
    const audio = button.parentElement.querySelector("audio");

    audio.muted = !audio.muted;

    if (audio.muted) {
        button.innerText = "Unmute";
    } else {
        button.innerText = "Mute";
    }
}