import sys
import subprocess
from pathlib import Path

def isolate_song(filepath):
    print(f"Starting separation for: {filepath}")

    command = [sys.executable, "-m", "demucs", "--mp3", filepath]

    result = subprocess.run(command)
    if result.returncode != 0:
        print("⚠️ Separation failed. Check your Demucs install.")
        return []

    # Get output folder
    song_name = Path(filepath).stem
    output_path = Path("separated") / "htdemucs" / song_name

    print(f"Separation complete! Files saved in {output_path}")

    return list(output_path.glob("*")) 

if __name__ == "__main__":
    isolate_song("Lullaby.mp3")