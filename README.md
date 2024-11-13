# SE-Technical-Assessment

**Project Workflow**

Video Processing Setup:

- Use OpenCV to read the uploaded video file (pov.mp4).
- Process each frame to detect and analyze motion features (e.g., arm reach, cadence, and object detection).
- Convert frames to RGB format for compatibility with MediaPipe.

Gait Feature Extraction:

- Pose Detection: Use MediaPipe's Pose model to identify key landmarks for arm reach.

Data Export:

- Store extracted features (arm reach, cadence, detected objects, and area sizes) in a structured format.
- Save data to a CSV file for machine learning analysis.
  
Documentation:

- Include a high-level workflow explanation in README.md (or PDF).
- Provide citations for used libraries and instructions on running the code locally.
  

**Algorithm for Gait Feature Extraction Tool**

Input: A video file containing footage for analysis.
Output: A CSV file with data on each frame, containing extracted features such as area size.

Initialize Resources

- Open the video file using a video processing library (e.g., OpenCV).
- Create an output CSV file to save extracted features (e.g., "gait_features.csv").
- Set Up Feature Extraction Parameters

Frame Processing Loop

- Repeat until all frames in the video are processed:
    1) Read Frame:
       - Capture the next frame in the video.
       - If no frame is captured (end of video), exit the loop.
    2) Preprocess Frame:
       - Convert the BGR image to RGB before processing for easier pose detection.
    3) Extract Features:
       - i.e. arm reach using mediapipe library.
    5) Store Frame Data:
       - Record the current frame number and the largest area size in a temporary data structure (e.g., a list or array).
    6) Save Extracted Features to CSV:
       - After processing all frames, write the recorded frame data (frame number and arm reach) to the output CSV file.
        
Release Resources and Close Files

- Close the video file and the CSV file.
- Output a message indicating that the data extraction is complete.

**Instructions to Run Locally:**
**Install Required Libraries**:
   Open a terminal and run the following commands to install the necessary libraries:
   pip install opencv-python
   pip install mediapipe
   pip install pandas
