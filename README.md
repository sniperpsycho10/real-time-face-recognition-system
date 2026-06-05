# Face Recognition Attendance Management System

## Overview

A complete Face Recognition Attendance Management System built using Python, OpenCV, InsightFace, SQLite, Pandas, Matplotlib, and Tkinter.

The system automatically detects and recognizes registered users in real-time using a webcam, marks attendance, stores records in a SQLite database, generates analytics, and exports attendance reports in PDF and CSV formats.

This project was developed as a complete end-to-end Computer Vision and Software Engineering project with modular architecture, automated dataset management, analytics, and reporting capabilities.

---

## Features

### Face Recognition

* Real-time face detection and recognition
* InsightFace-based facial embeddings
* Automatic face matching against a local database
* Unknown face handling

### Attendance Management

* Automatic attendance marking
* SQLite database integration
* Duplicate attendance prevention
* Date and time logging

### Dataset Management

* Register new users
* Capture face images directly from webcam
* Automatic dataset organization
* Automatic database rebuilding after enrollment

### Analytics

* Attendance statistics
* Attendance count per user
* Attendance trend analysis
* Visual analytics using Matplotlib

### Report Generation

* CSV attendance export
* PDF attendance report generation
* Automated reporting workflow

### GUI Dashboard

* User registration
* Face capture interface
* Recognition launcher
* Attendance viewer
* Analytics viewer

---

## Project Structure

```text
FaceRecognitionSystem/

├── data/
│   └── known_faces/
│
├── embeddings/
│   └── face_database.pkl
│
├── logs/
│   ├── attendance.csv
│   └── attendance.db
│
├── reports/
│   ├── attendance_export.csv
│   └── attendance_report.pdf
│
├── screenshots/
│
├── src/
│   ├── attendance_logger.py
│   ├── camera.py
│   ├── database_builder.py
│   ├── database_loader.py
│   ├── database_manager.py
│   ├── face_detector.py
│   ├── face_encoder.py
│   ├── face_engine.py
│   ├── recognizer.py
│   └── utils.py
│
├── build_database.py
├── capture_faces.py
├── dashboard.py
├── generate_report.py
├── main.py
├── register_person.py
├── search_attendance.py
├── visual_analytics.py
├── README.md
└── requirements.txt
```

---

## Technologies Used

* Python
* OpenCV
* InsightFace
* NumPy
* Pandas
* SQLite3
* Matplotlib
* Tkinter
* ReportLab

---

## Installation

### Clone Repository

```bash
git clone <your-repository-url>
cd FaceRecognitionSystem
```

### Create Virtual Environment

```bash
python -m venv face
```

### Activate Environment

Linux:

```bash
source face/bin/activate
```

Windows:

```bash
face\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Register a New Person

```bash
python register_person.py
```

### Capture Face Images

```bash
python capture_faces.py
```

### Build Face Database

```bash
python build_database.py
```

### Start Face Recognition

```bash
python main.py
```

### Launch Dashboard

```bash
python dashboard.py
```

### Generate Analytics

```bash
python visual_analytics.py
```

### Generate Reports

```bash
python generate_report.py
```

---

## Workflow

```text
Register User
      ↓
Capture Face Images
      ↓
Build Face Database
      ↓
Start Recognition
      ↓
Mark Attendance
      ↓
Store in SQLite
      ↓
Generate Analytics
      ↓
Export Reports
```

---

## Future Improvements

* Anti-Spoofing Detection
* Unknown Face Screenshot Capture
* Raspberry Pi Deployment
* Cloud Database Integration
* Mobile Application Support
* Email Report Automation
* Modern CustomTkinter Dashboard

---

## Resume Highlights

* Developed a real-time face recognition attendance system using InsightFace and OpenCV.
* Implemented automated attendance logging with SQLite database integration.
* Designed a modular Computer Vision pipeline for face detection, encoding, recognition, and attendance management.
* Built attendance analytics and visualization modules using Pandas and Matplotlib.
* Generated automated PDF and CSV attendance reports using ReportLab.

---

## Author

Ayush Pratap Singh

Computer Vision | Machine Learning | Cybersecurity | Python Development
