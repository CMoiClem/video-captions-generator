import subprocess

def add_subtitles_to_video(video_input, subtitles_file, video_output):
    ffmpeg_command = [
        "ffmpeg", "-v", "debug", "-i", video_input, "-vf", f"subtitles={subtitles_file}", "-c:v", "libx264", "-crf", "18", "-c:a", "copy", video_output
    ]
    subprocess.run(ffmpeg_command, check=True, text=True, capture_output=True)

# Usage
add_subtitles_to_video("original_video.mp4", "subtitles.srt", "output_video_with_subtitles.mp4")