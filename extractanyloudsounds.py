import os
import wave

# Set the path to the directory containing the audio files
audio_dir = '/path/to/audio'

# Set the path to the directory where the loud sounds will be saved
output_dir = '/path/to/output'

# Set the minimum threshold for loudness (in dB)
threshold = 0

# Get a list of all the audio files in the directory
audio_files = os.listdir(audio_dir)

# Iterate over the list of audio files
for audio_file in audio_files:
  # Open the audio file using the wave module
  with wave.open(os.path.join(audio_dir, audio_file), 'r') as f:
    # Read the frames from the audio file
    frames = f.readframes(-1)
    # Convert the frames to a byte array
    samples = bytearray(frames)

    # Iterate over the samples in the byte array
    for i in range(0, len(samples), f.getnchannels() * f.getsampwidth()):
      # Calculate the loudness of the sample
      loudness = 0
      for j in range(f.getnchannels()):
        loudness += abs(samples[i + j])

      # Check if the loudness is above the threshold
      if loudness > threshold:
        # Save the loud sound to the output directory
        with open(os.path.join(output_dir, audio_file.split('.')[0] + '.bin'), 'wb') as out:
          out.write(samples[i:i + f.getnchannels() * f.getsampwidth()])
