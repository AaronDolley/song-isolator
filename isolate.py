import sys
import subprocess
from pathlib import Path
import shutil
import time

def isolate_song(filepath):
    print(f"Starting separation for: {filepath}")

    # Run Demucs
    command = [sys.executable, "-m", "demucs", "--mp3", filepath]

    result = subprocess.run(command)
    if result.returncode != 0:
        print("⚠️ Separation failed. Check your Demucs install.")
        return []

    # Locate Demucs output
    song_name = f"{Path(filepath).stem}_{int(time.time())}"
    demucs_output = Path("separated") / "htdemucs" / song_name

    # Target folder (your app structure)
    target_folder = Path("static/stems") / song_name
    target_folder.mkdir(parents=True, exist_ok=True)

    # Move files
    for file in demucs_output.glob("*"):
        shutil.move(str(file), target_folder / file.name)

    print(f"✅Files moved to: {target_folder}")

    return list(target_folder.glob("*"))

if __name__ == "__main__":
    isolate_song("Lullaby.mp3")