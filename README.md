# 🎯 Real-Time Face Recognition System

A modular real-time face recognition system built using **Python, OpenCV, InsightFace, and ONNX Runtime**. The system creates a face database from local images, extracts facial embeddings, performs real-time face detection through a webcam, and identifies known individuals using embedding-based matching.

---

## 🚀 Features

### Phase 1 - Face Database Generation

* Automatic dataset scanning
* Face detection from images
* Face embedding extraction
* Serialized embedding database creation
* Multi-person support

### Phase 2 - Face Detection

* Real-time face detection
* Bounding box visualization
* Multi-face support
* Detection confidence scores

### Phase 3 - Real-Time Face Recognition

* Webcam-based face recognition
* Identity matching using facial embeddings
* Unknown face rejection
* Confidence score display
* Reduced flickering using frame caching
* CPU optimization using frame skipping

---

## 🛠️ Tech Stack

### Languages

* Python 3.13

### Computer Vision

* OpenCV
* InsightFace

### Deep Learning Runtime

* ONNX Runtime

### Data Processing

* NumPy
* Pickle

### Development Tools

* Git
* GitHub
* VS Code

---

## 📂 Project Structure

```text
FaceRecognitionSystem/

├── data/
│   ├── known_faces/
│   │   ├── Ayush/
│   │   └── Aryan/
│   │
│   └── test_images/
│
├── embeddings/
│   └── face_database.pkl
│
├── screenshots/
│
├── src/
│   ├── __init__.py
│   ├── face_engine.py
│   ├── database_builder.py
│   ├── database_loader.py
│   ├── recognizer.py
│   └── camera.py
│
├── build_database.py
├── test_recognition.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ System Workflow

```text
Known Face Images
        │
        ▼
Face Database Builder
        │
        ▼
Face Embeddings
        │
        ▼
face_database.pkl
        │
        ▼
Webcam Input
        │
        ▼
Face Detection
        │
        ▼
Embedding Extraction
        │
        ▼
Database Matching
        │
        ▼
Identity Recognition
        │
        ▼
Name + Confidence Display
```

---

## 📥 Installation

### Clone Repository

```bash
git clone https://github.com/<username>/FaceRecognitionSystem.git

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

## 📸 Dataset Preparation

Store images in the following format:

```text
data/

└── known_faces/

    ├── Person1/
    │   ├── image1.jpg
    │   ├── image2.jpg
    │   └── image3.jpg
    │
    └── Person2/
        ├── image1.jpg
        ├── image2.jpg
        └── image3.jpg
```

Each folder name becomes the identity label.

---

## 🏗️ Build Face Database

Generate facial embeddings:

```bash
python build_database.py
```

Example Output:

```text
Processing Ayush
✓ image1.jpg
✓ image2.jpg

Database saved to embeddings/face_database.pkl
```

---

## 🧪 Test Recognition on an Image

Place a test image inside:

```text
data/test_images/
```

Run:

```bash
python test_recognition.py
```

Example Output:

```text
Faces Found: 1

Name: Ayush
Distance: 11.43
Confidence: 36.49%
```

---

## 🎥 Run Real-Time Face Recognition

Start webcam recognition:

```bash
python main.py
```

Press:

```text
Q
```

to quit.

---

## 📊 Performance

Observed Matching Distances:

| Scenario     | Distance Range |
| ------------ | -------------- |
| Known Face   | 11 - 14        |
| Unknown Face | 15+            |

Current Recognition Threshold:

```python
threshold = 15.0
```

---

## ⚠️ Limitations

* Accuracy decreases at extreme face angles.
* Long-distance recognition depends on face resolution.
* Dataset quality directly affects recognition performance.
* Webcam support depends on operating system drivers.

---

## 🔮 Future Enhancements

### Phase 4

* Attendance Logging System
* CSV Export
* Recognition History

### Phase 5

* SQLite Database Integration
* Attendance Analytics Dashboard
* Searchable Records

### Phase 6

* Multi-Person Recognition
* GPU Acceleration
* Raspberry Pi Deployment

---

## 📸 Screenshots

### Face Detection

Add:

```text
screenshots/phase2_face_detection.png
```

### Real-Time Recognition

Add:

```text
screenshots/phase3_recognition.png
```

### Terminal Output

Add:

```text
screenshots/phase3_terminal_output.png
```

---

## 👨‍💻 Author

**Ayush**

Computer Vision | Machine Learning | Artificial Intelligence | Python Development
