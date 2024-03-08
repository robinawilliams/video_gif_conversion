from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
import os

# Prompt the user for the input video file
input_video_file = input("Enter the input video file (e.g., input.mp4): ")

# Prompt the user for the start and end timestamps
start_time_str = input("Enter the start timestamp (HH:MM:SS, MM:SS, or SS): ")
end_time_str = input("Enter the end timestamp (HH:MM:SS, MM:SS, or SS): ")

# Calculate the total start and end times in seconds
start_time_parts = list(map(int, start_time_str.split(':')))
end_time_parts = list(map(int, end_time_str.split(':')))
start_time = sum(part * (60 ** i) for i, part in enumerate(reversed(start_time_parts)))
end_time = sum(part * (60 ** i) for i, part in enumerate(reversed(end_time_parts)))

# Prompt the user for the output video file
output_gif_name = os.path.join('output_gifs', f'{input("Enter the output video file (e.g., puppies): ")}.gif')

# Create the output folder if it doesn't exist
os.makedirs('output_gifs', exist_ok=True)

# Extract the subclip from the input video
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
