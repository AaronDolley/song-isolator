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
