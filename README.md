# Live Face Detection with Python

## Overview

This project implements live face detection using Python and OpenCV. It captures video from your webcam, detects faces in real-time, and highlights them in the video feed.

## Features

- Real-time face detection using Haar cascades.
- Modular design for easy maintenance and extension.
- Organized directory structure for better manageability.

## Directory Structure

```plaintext
face_detection_project/
├── models/              # Pre-trained models
│   └── haarcascades/    # Haar cascade XML files
├── src/                 # Source code
│   └── detect_faces.py  # Script for face detection
└── main.py              # Main script to run the project
