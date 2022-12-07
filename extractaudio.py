import os
import subprocess

# Set the path to the directory containing the videos
video_dir = '/path/to/videos'

# Set the path to the directory where the audio will be saved
audio_dir = '/path/to/audio'

# Get a list of all the video files in the directory
videos = os.listdir(video_dir)

# Iterate over the list of videos
for video in videos:
  # Construct the file paths
  video_path = os.path.join(video_dir, video)
  audio_path = os.path.join(audio_dir, video.split('.')[0] + '.mp3')

  # Use ffmpeg to extract the audio from the video and save it as an MP3 file
  command = ['ffmpeg', '-i', video_path, '-vn', '-acodec', 'libmp3lame', audio_path]
  subprocess.run(command)

