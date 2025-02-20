import os
import random
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

# Define input/output directories
input_folder = "videos"  # Folder containing videos
output_folder = os.path.join(input_folder, "ready")
watermark_folder = "watermark"  # Folder containing watermark templates

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Scan for watermark files
watermark_files = [f for f in os.listdir(watermark_folder) if f.lower().endswith(".png")]

# Scan folder for video files
video_extensions = ('.mp4', '.avi', '.mov', '.mkv')
video_files = [f for f in os.listdir(input_folder) if f.lower().endswith(video_extensions)]

# Process each video
for video in video_files:
    video_path = os.path.join(input_folder, video)
    
    # Load video clip
    clip = VideoFileClip(video_path)
    
    # Resize video to 720x1280
    clip = clip.resize(height=1280, width=720)
    
    # Select a random watermark
    selected_watermark = random.choice(watermark_files)
    watermark_path = os.path.join(watermark_folder, selected_watermark)

    # Load watermark and resize to 720x1280
    watermark = ImageClip(watermark_path, transparent=True).resize((720, 1280))

    # Set watermark position to cover the entire video
    watermark = watermark.set_position(("center", "center")).set_duration(clip.duration)

    # Overlay watermark on video using CompositeVideoClip
    final_clip = CompositeVideoClip([clip, watermark]).set_audio(None)

    # Save output video without audio
    output_path = os.path.join(output_folder, f"processed_{video}")
    final_clip.write_videofile(output_path, codec="libx264", fps=clip.fps, audio=False)

    # Close clips to release memory
    clip.close()
    watermark.close()
    final_clip.close()

print("Processing complete. Check the 'ready' folder.")
