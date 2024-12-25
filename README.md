# 🖐️ Hand Mouse Controller Web Application 🖱️

This project allows you to control your computer's mouse using hand gestures 🤚, leveraging the power of **MediaPipe** for hand tracking and **PyAutoGUI** for mouse control. It provides a web interface 🌐 where you can upload frames captured from your webcam, and the system will detect hand movements to move the mouse cursor 🖱️ and perform click actions 👆.

## Features ✨
- **Hand Tracking**: Uses MediaPipe to detect hand landmarks and track the movements of fingers ✋.
- **Mouse Control**: Moves the mouse based on the index finger's position 🖱️ and supports left and right clicks using finger gestures 👈👉.
- **Web Interface**: Built with Flask to serve the application and provide an interface to interact with the hand tracking system 🌍.
- **Real-Time Processing**: The app processes frames uploaded from the front end and performs actions like mouse movement and clicking ⚡.

## Requirements 📦
- Python 3.8+
- Flask 🧪
- OpenCV 🖼️
- Mediapipe 🖐️
- PyAutoGUI 🖱️
- NumPy 🔢

## Installation 🛠️

### STEP 01 - Clone the repository

Open your terminal and paste the following command to clone the repository:

```bash
git clone https://github.com/Rahulagowda004/Virtual_mouse.git
```

### STEP 02 - Create a virtual environment

After opening the cloned repository, create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On macOS/Linux
```

### STEP 03 - Install the requirements

Install all the necessary dependencies:

```bash
pip install -r requirements.txt
```

### STEP 04 - Run the application

Finally, run the application with:

```bash
python app.py
```

## Usage 🚀

1. After running the command above, open your web browser 🌐 and go to `http://localhost:5000`.
2. Upload webcam frames 📸 to the Flask server, which will process the hand movements and control your mouse 🖱️.

## Contributing 🤝

Feel free to fork this repository and submit pull requests. Contributions are welcome! 🚀

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This should provide clear and structured instructions for setting up and running your application. Let me know if you'd like any further adjustments!
