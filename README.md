# VolumeControl - Gesture Recognition

## Introduction

Gesture recognition is a technology that bridges the gap between humans and machines, enabling interactions beyond traditional text or graphical user interfaces. In this project, we use computer vision to capture and interpret human hand gestures through a computer camera. The objective is to create an interface that dynamically captures hand gestures and uses them to control the volume level of a device.

## Libraries Used

- **NumPy**: NumPy is a Python library that provides support for large, multi-dimensional arrays and matrices. It also offers a collection of high-level mathematical functions to operate on these arrays.

- **Pycaw**: Pycaw is a Python Audio Control Library that allows us to control audio settings programmatically.

- **MediaPipe**: MediaPipe is an open-source machine learning library developed by Google. It offers solutions for face recognition and gesture recognition. In this project, we leverage MediaPipe Hands, a high-fidelity hand and finger tracking solution that uses machine learning to infer 21 key 3D hand landmarks from a single frame.

## Working Principle

1. **Hand Detection**: The project uses the device's camera to detect hand landmarks, capturing the positions of various key points on the hand.

2. **Distance Calculation**: It calculates the distance between the thumb tip and the index finger tip, which serves as a gesture indicator.

3. **Volume Mapping**: The calculated distance between thumb tip and index finger tip is mapped to a predefined volume range. In our case, the distance range was 30 to 350, and the volume range was -63.5 to 0.0.

4. **Control Volume**: The program then adjusts the device's volume based on the mapped gesture. Moving the hand closer or farther apart controls the volume accordingly.

5. **Exit**: To exit the program, simply press the 'Spacebar'.

## How to Use

1. Ensure you have all the required libraries installed, including NumPy, Pycaw, and MediaPipe.

2. Run the project.

3. Use hand gestures to control the volume dynamically.

4. To exit, press the 'Spacebar'.

## Example Image

![Gesture Recognition](https://user-images.githubusercontent.com/82171169/171317563-c598abea-72f8-4176-83e7-2c4efb08205d.png)

Empower your computer to understand and respond to your hand gestures with "VolumeControl." Take control of your device's audio experience like never before.

