# Import necessary libraries
import cv2  # For video processing
import sys # For error checking
import mediapipe as mp  # For pose detection
import pandas as pd  # For saving data to a CSV file

# Initialize Mediapipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Attempt to read video from source
cap = cv2.VideoCapture("pov.mp4")

# Data storage for gait features
data = []

# Error check to make sure the frame is open. Exit if video isn't opened 
if not cap.isOpened():
    print("Couldn't open video")
    sys.exit()

# Loop through each frame in the video
while cap.isOpened():
    ret, frame = cap.read() # Read frame from the video
    if not ret: # If the end of the video is reached exit the loop
        break

# Error check to make sure the frame is valid 
if frame is not None and frame.size > 0: # Checking if frame is valid
    cv2.imshow('Frame', frame) # Only show the frame is it's valid
else: 
    print("Error: Frame is empty or not initialized.") # Error message is printed if frame is invalid

    # Convert the BGR image to RGB before processing. This will make it easier to process pose detection
    results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        
        # Initialize left and right arm and wrist variables in order to calculate arm reach (distance from shoulder to wrist)
        left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
        left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST]
        right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST]
        # Distance Formula =√((x_2-x_1)²+(y_2-y_1)²). This will find the distance between the shoulder and wrist in order to calculate arm reach
        left_arm_reach = ((left_wrist.x - left_shoulder.x) ** 2 + (left_wrist.y - left_shoulder.y) ** 2) ** 0.5
        right_arm_reach = ((right_wrist.x -right_shoulder.x)**2 + (right_wrist.y - right_shoulder.y)**2) ** 0.5
        
        # Store the frame and left/right arm reach data in order to output to a csv file
        frame_data = {
            # Use get function documentation and typecast to int to get data frame by frame
            "frame": int(cap.get(cv2.CAP_PROP_POS_FRAMES)),
            "left_arm_reach": left_arm_reach,
            "right_arm_reach": right_arm_reach
        }
        
        # Add frame's data to the list
        data.append(frame_data)

# Release resources
cap.release()

# Save extracted data to a csv file using the pandas library
df = pd.DataFrame(data)
df.to_csv("gait_features.csv", index=False)

#print message for users to know that the program is complete and where the created csv file is saved
print("Data extraction complete. Results saved to 'gait_features.csv'.")
