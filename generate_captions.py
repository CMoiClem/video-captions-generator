import whisper
import re
from deep_translator import GoogleTranslator

def convert_time(match):
    return f"{int(float(match.group(1))):02d}:{int(float(match.group(2))):02d}:{float(match.group(3)):06.3f}".replace('.', ',')

def generate_french_subtitles(video_path, output_path):
    # Load the Whisper model - 'base' is used here for simplicity, but you can choose other models based on your need for speed vs. accuracy
    model = whisper.load_model("base")

    # Transcribe the audio from the video file
    result = model.transcribe(video_path)

    # Translate the transcribed text
    translated_segments = []
    for segment in result["segments"]:
        translated_text = GoogleTranslator(source='auto', target='fr').translate(segment['text']) #can change the target language here
        translated_segments.append((segment['start'], segment['end'], translated_text))

    # Write to a .srt file with corrected time format
    with open(output_path, 'w', encoding='utf-8') as srt_file:
        for i, (start, end, text) in enumerate(translated_segments, 1):
            # Convert time format
            start_time = convert_time(re.match(r'(\d+\.\d):(\d+\.\d):(\d+\.\d+)', format_time(start)))
            end_time = convert_time(re.match(r'(\d+\.\d):(\d+\.\d):(\d+\.\d+)', format_time(end)))
            
            srt_file.write(f"{i}\n")
            srt_file.write(f"{start_time} --> {end_time}\n")
            srt_file.write(f"{text}\n\n")

def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:06.3f}"

# Usage
video_path = "original_video.mp4"
output_path = "subtitles.srt"
generate_french_subtitles(video_path, output_path)