# Real-Time Face Recognition and Identity Management System

## Overview

A modular real-time face recognition system built using Python, OpenCV, InsightFace, and ONNX Runtime. The system creates a facial database from local images, extracts facial embeddings, detects faces in images and live video streams, and performs identity recognition with confidence scoring.

---

## Features

### Completed

* Face Database Creation
* Face Embedding Extraction
* Face Detection using InsightFace
* Bounding Box Visualization
* Face Detection Confidence Display
* Modular Project Architecture
* Git Version Control
* GitHub Integration

### Upcoming

* Real-Time Webcam Recognition
* Confidence-Based Identity Matching
* Unknown Face Detection
* Attendance Logging
* SQLite Integration
* Performance Evaluation
* Multi-Face Recognition

---

## Technology Stack

* Python 3.13
* OpenCV
* InsightFace
* ONNX Runtime
* NumPy
* Pandas
* Scikit-Learn
* Git
* GitHub

---

## Project Structure

FaceRecognitionSystem/

├── data/

│   └── known_faces/

│       ├── Ayush/

│       └── Aryan/

│

├── embeddings/

│   └── face_database.pkl

│

├── logs/

├── screenshots/

│

├── src/

│   ├── face_encoder.py

│   ├── face_detector.py

│   ├── database_builder.py

│   └── utils.py

│

├── tests/

│   └── test_detector.py

│

├── main.py

├── requirements.txt

└── README.md

---

## Phase 1 Workflow

Known Face Images

↓

Face Detection

↓

Face Embedding Extraction

↓

Embedding Database Creation

↓

face_database.pkl

---

## Phase 2 Workflow

Input Image

↓

InsightFace Detector

↓

Bounding Box Detection

↓

Detection Confidence

↓

Visualization

---

## Current Status

Phase 1 : Complete

Phase 2 : Complete

Phase 3 : In Progress

---

## Sample Output

Faces Found: 1

Detection Confidence: 0.82

---

## Future Enhancements

* Real-Time Recognition
* Attendance System
* SQLite Storage
* Face Search Engine
* GUI Dashboard
* Raspberry Pi Deployment
