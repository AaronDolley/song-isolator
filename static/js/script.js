let isPlaying = false;
let players = [];
let previousVolumes = [];

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
        const currentTime = players[0]?.getCurrentTime() || 0;

        players.forEach(p => {
            p.seekTo(currentTime / p.getDuration());
            p.play();
        });
        
        isPlaying = true;
    } else {
        players.forEach(p => p.pause());
        isPlaying = false;
    }
}

function toggleMute(index, button) {
    const player = players[index];
    if (!player) return;

    const currentVolume = player.getVolume();
    const reference = players[0]; // use first track as master clock

    if (currentVolume > 0) {
        // if currently not muted
        previousVolumes[index] = currentVolume; // save volume
        player.setVolume(0);
        button.innerText = "🔊 Unmute";
    } else {
        // Restore previous volume (or default to 1)
        const restoreVolume = previousVolumes[index] ?? 1;

        if (reference && reference.isPlaying()) {
            const currentTime = reference.getCurrentTime();
            const duration = player.getDuration();

            if (duration > 0) {
                player.seekTo(currentTime / duration);
            }
        }
        player.setVolume(restoreVolume);
        button.innerText = "🔇 Mute";
    }
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

