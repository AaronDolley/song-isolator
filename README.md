# AI Song Stem Isolator

A web application that allows users to upload a song and seperate it into individual stems like vocals, drums, bass and piano.

## Features
- Upload audio files
- AI-powered stem seperation
- Download individual stems

## Tech Stack
- Python
- Flask
- Demucs
- FFmpeg

## Status
In development

## Day 2 - Demucs Testing
Successfully seperated audio into:
- Vocals
- Drums
- Bass
- Other

## Observations:
- All stems are clear and usable 
- "Other" contains piano and remaining instruments
- No clear guitar detected in this track 
- Separation works well, but not perfect (some overlap)

Next step: automate this process using Python

## Day 3 - Python Integration
Created a Python script to run Demucs automatically.

## Features:
- Runs stem separation using Python
- Outputs stems to structured folder
- Returns list of generated files

Next step: Connect this to a web interface

# Day 4 - File System Structure
Improved file handling and project structure.

### Changes:
- Added uploads/ folder for incoming files
- Added static/stems/ for processed outputs
- Automatically moves separated stems into organized folders

This prepares the app for web integration.

## Day 5 — Flask Web Interface

- Minimal web interface to upload MP3 files
- Automatically separates uploaded songs
- Stores stems in `static/stems/<song_name>/`