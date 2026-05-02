#"AI-Powered Gesture Interface for System Audio Control"
#"Touchless Audio: AI Hand Tracker"
# 🖐️ AI Gesture Volume Controller

A high-performance real-time computer vision application that allows users to control system volume through hand gestures. This project leverages AI to create a touchless interaction experience.

## 📖 Overview
This project uses **OpenCV** and **MediaPipe** to detect hand landmarks in real-time. By calculating the distance between the thumb and index finger tips, the system dynamically maps and adjusts the computer's master volume.

## ✨ Features
- **Real-time Detection:** High-fidelity hand landmark tracking using Google's MediaPipe.
- **Dynamic Volume Control:** Intuitive pinch-to-adjust gesture mapping.
- **Visual Feedback:** On-screen volume bar and percentage display for a better user experience.
- **Responsive UI:** Large HD window support for clear visual tracking.

## 🚀 Getting Started

### Prerequisites
Ensure you have Python installed on your machine.

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd Hand-Gesture-Recognition
   ```

2. **Install required dependencies:**
   ```bash
   pip install opencv-python mediapipe pycaw comtypes numpy
   ```

### Usage
Run the main script:
```bash
python main.py
```
- **Increase Volume:** Move thumb and index finger apart.
- **Decrease Volume:** Bring thumb and index finger together.
- **Exit:** Press 'q' on your keyboard.

## 🛠️ Tech Stack
- **Python**: Core logic.
- **OpenCV**: Image processing and webcam integration.
- **MediaPipe**: Hand landmark detection (21 points).
- **Pycaw**: Interface for Windows Core Audio APIs.
- **NumPy**: Data interpolation for volume mapping.
---
Developed by [aishu.codes](https://github.com)
