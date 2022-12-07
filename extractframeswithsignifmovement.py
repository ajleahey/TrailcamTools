import cv2
import os

# Set the path to the directory containing the video files
video_dir = '/Volumes/Video Book/Unedited Video/2022/September 2022/September 24/trailcams/clearing'

# Set the path to the directory where the frames will be saved
output_dir = '/Volumes/Video Book/Unedited Video/2022/September 2022/September 24/trailcams/clearing/movements'

# Set the minimum threshold for movement
threshold = 0

# Get a list of all the video files in the directory
videos = os.listdir(video_dir)

# Iterate over the list of videos
for video in videos:
  # Check if the video file starts with a dot or underscore
  if video[0] == '.' or video[0] == '_':
    continue

  # Open the video using OpenCV
  cap = cv2.VideoCapture(os.path.join(video_dir, video))

  # Read the first frame from the video
  ret, prev_frame = cap.read()

  # Convert the frame to grayscale
  prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

  # Initialize a variable for the maximum sum of the differences
  max_sum = 0

  # Initialize a variable for the frame with the maximum sum of the differences
  max_frame = None

  # Initialize a counter for the frame index
  frame_index = 1

  # Iterate over the frames in the video
  while cap.isOpened():
    # Read the next frame from the video
    ret, frame = cap.read()

    # Check if there are no more frames
    if not ret:
      break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate the difference between the current and previous frames
    diff = cv2.absdiff(prev_gray, gray)

    # Calculate the sum of the difference
    sum = diff.sum()

    # Check if the sum is above the threshold and greater than the maximum sum
    if sum > threshold and sum > max_sum:
      # Update the maximum sum and frame
      max_sum = sum
      max_frame = frame

    # Update the previous frame and frame index
    prev_gray = gray
    frame_index += 1

  # Check if a frame with significant movement was found
  if max_frame is not None:
    # Save the frame to the output directory
    cv2.imwrite(os.path.join(output_dir, video.split('.')[0] + '_max.jpg'), max_frame)

  # Close the video
  cap.release()
