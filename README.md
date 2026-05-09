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
## view output video on linkedin post
https://www.linkedin.com/posts/aishwarya-s-bbb99529a_ai-computervision-datascience-ugcPost-7457356907872178176-dqE5?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEhnjX8BM-GrNrlJhx2p4G1wr3CpxvecgaU
<img width="1080" height="599" alt="v1" src="https://github.com/user-attachments/assets/836fd868-d524-48a7-a80e-c87480add343" />
<img width="1080" height="575" alt="v2" src="https://github.com/user-attachments/assets/7e5036b9-cb55-473f-b1e5-0a4d0e99bbb8" />
<img width="1080" height="586" alt="v3" src="https://github.com/user-attachments/assets/5ca18e7c-948e-4162-98c7-8dc9d661bc56" />









Developed by [aishu.codes](https://github.com)
