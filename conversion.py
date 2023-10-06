from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
import os

def normalize_timestamp(timestamp):
    parts = timestamp.split(':')
    while len(parts) < 3:
        parts.insert(0, '0')
    hours, minutes, seconds = map(int, parts)
    return hours, minutes, seconds

# Prompt the user for the input video file
input_video_file = input("Enter the input video file (e.g., input.mp4): ")

# Prompt the user for the start and end timestamps
start_time_str = input("Enter the start timestamp (HH:MM:SS, MM:SS, or SS): ")
end_time_str = input("Enter the end timestamp (HH:MM:SS, MM:SS, or SS): ")

# Normalize the start and end timestamps to HH:MM:SS format
start_time_hours, start_time_minutes, start_time_seconds = normalize_timestamp(start_time_str)
end_time_hours, end_time_minutes, end_time_seconds = normalize_timestamp(end_time_str)

# Calculate the total start and end times in seconds
start_time = (start_time_hours * 3600) + (start_time_minutes * 60) + start_time_seconds
end_time = (end_time_hours * 3600) + (end_time_minutes * 60) + end_time_seconds

# Prompt the user for the input video file
output_video_name = input("Enter the output video file (e.g., puppies): ")

# Output folder
output_folder = 'output_gifs'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Extract hours, minutes, and seconds
start_time_parts = list(map(int, start_time_str.split(':')))
end_time_parts = list(map(int, end_time_str.split(':')))

start_time = sum(part * (60 ** i) for i, part in enumerate(reversed(start_time_parts)))
end_time = sum(part * (60 ** i) for i, part in enumerate(reversed(end_time_parts)))

# Extract the subclip from the input video
output_gif_name = os.path.join(output_folder, f'{output_video_name}.gif')

ffmpeg_extract_subclip(input_video_file, start_time, end_time, targetname="temp_clip.mp4")

# Load the clipped video
video_clip = VideoFileClip("temp_clip.mp4")

# Convert the video clip to a GIF
video_clip.write_gif(output_gif_name)

# Clean up temporary files
video_clip.close()

# Delete the temporary clip file
os.remove("temp_clip.mp4")

print(f"GIF saved as {output_gif_name}")
