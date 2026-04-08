let isPlaying = false;
let players = [];

window.addEventListener("DOMContentLoaded", () => {
    const stems = document.querySelectorAll(".stem");

    stems.forEach((stem, index) => {
        const url = stem.getAttribute("data-url");
        const container = stem.querySelector(".waveform");

        console.log("Loading:", url);

        const wavesurfer = WaveSurfer.create({
            container: container,
            waveColor: "#555",
            progressColor: "#1db954",
            height: 80
        });

        wavesurfer.load(url);

        players.push(wavesurfer);
    });
});

function togglePlay() {
    if (!isPlaying) {
        players.forEach(p => p.play());
        isPlaying = true;
    } else {
        players.forEach(p => p.pause());
        isPlaying = false;
    }
}

function toggleMute(index, button) {
    const player = players[index];

    if (!player) return;

    //Track mute manually
    player.muted = !player.muted;
    player.setVolume(player.muted ? 0 : 1);

    button.innerText = player.muted ? "Unmute" : "Mute";
}

function toggleSinglePlay(index, button) {
    const player = players[index];

    if (!player) return;

    if (player.isPlaying()) {
        player.pause();
        button.innerText = "Play";
    } else {
        player.play();
        button.innerText = "Pause";
    }
}