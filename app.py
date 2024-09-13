from flask import Flask, request, render_template
import base64
import cv2
import numpy as np
from pipeline import HandMouseController

app = Flask(__name__)
hand_mouse_controller = HandMouseController()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_frame', methods=['POST'])
def upload_frame():
    data = request.json
    frame_data = data['frame'].split(',')[1]
    frame = base64.b64decode(frame_data)
    np_frame = np.frombuffer(frame, dtype=np.uint8)
    image = cv2.imdecode(np_frame, cv2.IMREAD_COLOR)

    # Process the frame with the HandMouseController
    processed_image = hand_mouse_controller.process_frame(image)
    
    # Optionally display the frame (comment out in production)
    cv2.imshow('Processed Frame', processed_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return 'Stopped'

    return 'Frame received', 200

if __name__ == '__main__':
    app.run(debug=True,host = '0.0.0.0',port = 5000)
