# EmotiSense 😃😐😠
**AI-Powered Real-Time Emotion Detection System**


**EmotiSense** is a real-time emotion detection system that uses computer vision and facial landmark analysis to infer human emotions from live webcam input. The project is designed for **learning, demonstration, and portfolio use**, with a strong focus on explainable AI and clean system design.

---
## 🌐 Live Demo

**[🚀 Try EmotiSense Live](https://emotisense-ai.streamlit.app)** - No installation required!

---

## 🚀 Features

* 🎥 Real-time webcam-based face analysis
* 🧠 Emotion detection using **rule-based logic** on facial landmarks
* 👁️ MediaPipe Face Mesh (468 landmarks)
* 🎛️ Interactive controls for calibration and UI toggles
* 📊 Emotion confidence scoring
* 🧩 Modular, easy-to-understand codebase

---

## 🧠 Emotions Supported

* Happy 😊
* Sad 😢
* Angry 😠
* Surprised 😲
* Neutral 😐

> Emotions are inferred using explainable geometric ratios (mouth openness, eyebrow movement, eye openness), not a black-box model.

---

## 🏗️ Project Architecture

```text
EmotiSense/
│
├── src/
│   ├── app.py               # Main application (entry point)
│   ├── face_mesh.py         # MediaPipe Face Mesh detector
│   ├── emotion_rules.py     # Rule-based emotion logic
│
├── models/
│   └── face_landmarker.task # MediaPipe model
│
├── venv/                    # Virtual environment
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

| Category        | Tools / Libraries             |
| --------------- | ----------------------------- |
| Language        | Python 3.10+                  |
| Computer Vision | OpenCV                        |
| Face Landmarks  | MediaPipe Face Mesh           |
| AI Logic        | Rule-based geometric analysis |
| Environment     | Virtualenv                    |

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/sumittt2004/EmotiSense 
cd EmotiSense
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python src/app.py
```

---

## 🎮 Controls

| Key         | Action                 |
| ----------- | ---------------------- |
| `C`         | Calibrate neutral face |
| `L`         | Toggle face landmarks  |
| `E`         | Toggle emotion display |
| `Q` / `ESC` | Exit application       |

---

## 🧪 How Emotion Detection Works

Instead of using a pre-trained deep learning classifier, EmotiSense:

1. Detects 468 facial landmarks using MediaPipe
2. Measures facial geometry (distances & ratios)
3. Compares them against calibrated neutral values
4. Applies rule-based thresholds
5. Outputs emotion + confidence score

This approach ensures:

* ✔ Explainability
* ✔ Lightweight execution
* ✔ No dataset bias


---

## 🎯 Use Cases

* AI / CV portfolio project
* Emotion-aware applications
* Human–Computer Interaction research
* Learning MediaPipe & facial landmarks
* Interview demonstrations

---

## 🔮 Future Improvements

* Add deep learning emotion classifier (CNN)
* Multi-face emotion detection
* Emotion timeline analytics
* Streamlit web deployment
* Dataset-based benchmarking

---

## 📬 Contact & Support

- **Author:** Sumit Mishra
- **GitHub:** [@sumittt.2004](https://github.com/sumittt2004)
- **Linkedin:** [Sumit Mishra](https://www.linkedin.com/in/mishra-sumit-/)

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork or contribute!
