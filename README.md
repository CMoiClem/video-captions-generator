# video-captions-generator
Easy way to add translated captions to your videos

### Features
One script extracts captions from a video using Speech-to-Text with OpenAI's Whisper and translates them using deep-translator (GoogleTranslator), exporting an editable .srt file for any necessary modifications.
Another script integrates these captions back into the original video.

### Requirements
- Python
- ffmpeg
- whisper (`pip install openai-whisper`)
- deep-translator (`pip install deep-translator`)
 
### How It Works
- Place Your Video: Put your video file in the same directory as the Python scripts or update the video path in the scripts.
- Run the Transcription Script (generate_captions.py)
    Modify generate_subtitles.py if needed to adjust input/output paths or target language (set to French by default).
- Execute the script to generate an .srt file with translated subtitles.
- Review and Edit
    Open the .srt file to manually check or correct the subtitles.
- Run the Captions Integration Script (add_captions.py)
    Adjust the paths in add_subtitles_to_video.py for your input video and .srt file if necessary.
