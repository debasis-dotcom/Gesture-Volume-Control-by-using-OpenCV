# Gesture-Volume-Control-by-using-OpenCV

## Description
In this project we are going to learn how to use Gesture Control to change the volume of a computer. We first look into hand tracking and then we will use the hand landmarks to find gesture of our hand to change the volume.

## Features
- Can change your computer's volume based on your hand activity
- Can track your hand in real-time

## Packages Used
- OpenCV
- Mediapipe
- NumPy
- pyCaw

Here's a list of files in the directory:

- src/Gesture Volume Control.py: Contains all the module to detect the landmarks on the hand.
- src/HandTrackingModule.py: Contains the code to calculate the ditance between the thumb tip and index finger tip by recognising the landmark and based on the distnace it adjust the volume.

## How to use?
Step 1: Clone this repository on your local computer

git clone https://github.com/debasis-dotcom/Gesture-Volume-Control-by-using-OpenCV

Step 2: Install all the requirements
- pip install mediapipe
- pip install opencv-python
- pip install pycaw

Or else if you are using pyCharm then you can directly add by going through its setting --> interpreter --> add

Step 3: Run the program

## Demo
![Demo](https://github.com/debasis-dotcom/Gesture-Volume-Control-by-using-OpenCV/blob/main/Gesture%20Volume%20Control.gif)
