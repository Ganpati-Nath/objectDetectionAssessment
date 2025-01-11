# Object Detection and Hierarchical Analysis System

## Project Overview

This project implements an object detection and hierarchical analysis system using YOLOv5 and OpenCV. The system detects objects and sub-objects in a video stream, organizes them hierarchically, and outputs the results in a JSON format. Cropped images of detected objects and sub-objects are also saved for further analysis.

## Directory Structure

```objectDetectionProject/
├── src/
│   ├── detection.py           # Main script for object detection
│   ├── hierarchy.py           # Hierarchical association logic
│   ├── jsonFormatter.py       # Formats results into JSON
│   ├── benchmark.py           # Measures system performance
│   ├── imageUtils.py          # Utilities for cropping images
├── data/
│   ├── sample_video.mp4       # Input video
│   ├── output/                # Output directory (JSONs and images)
├── README.md                  # Documentation
└── requirements.txt           # Dependencies
```

## Setup Instructions

## 1. Prerequisites

Python 3.8 or later

Virtual environment (optional but recommended)

## 2. Install Dependencies

Run the following commands to set up the environment:

`pip install -r requirements.txt`

## 3. Download YOLO Model Weights

Download the YOLOv5 model weights (e.g., yolov5s.pt or yolov5n.pt) from the official Ultralytics repository and place them in the root directory.

## 4. Run the Detection System

To execute the object detection and save results, run:

`python src/detection.py`

## 5. Outputs

JSON File: Results are saved in ./data/output/results.json.

Cropped Images: Saved in ./data/output/ with filenames indicating object type, sub-object, and frame ID.

## System Components

## 1. Object Detection

Script: detection.py

Detects objects using YOLO and outputs results in JSON format.

## 2. Hierarchical Association

Script: hierarchy.py

Associates detected objects with sub-objects based on spatial relationships.

## 3. Image Cropping

Script: imageUtils.py

Crops images of detected objects and saves them for further analysis.

## 4. JSON Formatting

Script: jsonFormatter.py

Converts hierarchical detection results into a structured JSON format.

## 5. Performance Benchmarking

Script: benchmark.py

Evaluates inference speed and overall system performance.

Sample Output

Console Output

```0: 480x640 1 person, 7 cars, 1 truck, 1 umbrella, 113.3ms
Speed: 2.0ms preprocess, 113.3ms inference, 0.0ms postprocess per image at shape (1, 3, 480, 640)
Formatted JSON saved to ./data/output/results.json
Detection complete. Results saved to ./data/output/results.json```

## JSON Output (results.json)

```[
  {
    "object": "Car",
    "id": 1,
    "bbox": [x1, y1, x2, y2],
    "subobjects": [
      {
        "object": "Tire",
        "id": 1,
        "bbox": [x1, y1, x2, y2]
      }
    ]
  }
]```
