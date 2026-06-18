# 🪄 Magical Cloak

A fun Computer Vision project inspired by the famous "Invisibility Cloak" concept from Harry Potter. This project uses OpenCV and Python to make a colored cloak appear invisible in real-time using image processing techniques.

## 📌 Project Overview

The Magical Cloak project creates the illusion of invisibility by detecting a specific cloak color and replacing it with the previously captured background frame.

When a person wears the selected colored cloth, the cloak area is replaced with the background, making it appear as if the person is invisible.

## ✨ Features

- Real-time video processing
- Color detection using HSV color space
- Background capture and replacement
- OpenCV-based implementation
- Fun demonstration of Computer Vision concepts

## 🛠️ Technologies Used

- Python
- OpenCV
- NumPy

## 📂 Project Structure

```
Magical-Cloak/
│
├── magical_cloak.py
├── requirements.txt
├── README.md
└── assets/
    └── demo.gif
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/saargi15/Magical-Cloak.git
cd Magical-Cloak
```

### 2. Install dependencies

```bash
pip install opencv-python numpy
```

Or

```bash
pip install -r requirements.txt
```

## ▶️ Running the Project

Run the Python file:

```bash
python magical_cloak.py
```

### Steps:

1. Start the webcam.
2. Stay out of the camera frame for a few seconds while the background is captured.
3. Wear or hold the selected cloak color.
4. Watch the cloak become "invisible".

## 🧠 How It Works

1. The webcam captures the background scene.
2. Frames are continuously read from the camera.
3. The cloak color is detected using HSV color segmentation.
4. A mask is created for the cloak region.
5. The detected cloak area is replaced with the stored background.
6. The final output creates the illusion of invisibility.

## 📸 Demo

Add your screenshots or GIF here:

```markdown
![Demo](assets/demo.gif)
```

## 🎯 Learning Outcomes

- Image Processing
- Computer Vision Fundamentals
- Color Detection
- Masking Techniques
- OpenCV Applications
- Real-Time Video Processing

## 🚀 Future Enhancements

- Support multiple cloak colors
- Improve edge detection
- Add GUI controls
- Optimize processing speed
- Deploy as a desktop application

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

## 👩‍💻 Author

**Saargi Singh**

B.Tech CSE Student  
Computer Vision & Web Development Enthusiast

GitHub: https://github.com/saargi15

## 📜 License

This project is open-source and available under the MIT License.
