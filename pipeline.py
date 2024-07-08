import cv2
import mediapipe as mp
import pyautogui
import threading

class HandMouseController:
    def __init__(self, dpi_scale=2.0):
        # Initialize Mediapipe Hands and Drawing
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_drawing = mp.solutions.drawing_utils

        # Initialize the video capture
        self.cap = cv2.VideoCapture(0)
        ret, frame = self.cap.read()
        if not ret:
            raise Exception("Unable to read from the webcam")
        
        self.height, self.width, _ = frame.shape

        # Initialize a variable to store the current frame
        self.current_frame = None

        # Define the DPI scaling factor
        self.DPI_SCALE = dpi_scale

        # Start the frame capture thread
        self.capture_thread = threading.Thread(target=self.capture_frames)
        self.capture_thread.start()

    def capture_frames(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            self.current_frame = frame

    def process_frame(self, frame):
        # Flip the frame horizontally for a later selfie-view display
        image = cv2.flip(frame, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Process the frame and get hand landmarks
        results = self.hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                # Extract landmarks for the index finger tip and thumb tip
                index_finger_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP]

                # Convert normalized coordinates to screen coordinates
                screen_width, screen_height = pyautogui.size()
                x = int(index_finger_tip.x * screen_width * self.DPI_SCALE)
                y = int(index_finger_tip.y * screen_height * self.DPI_SCALE)

                # Ensure the cursor does not move out of the screen bounds
                x = max(0, min(screen_width - 1, x))
                y = max(0, min(screen_height - 1, y))

                # Move the mouse
                pyautogui.moveTo(x, y)

                # Check distance between index finger tip and thumb tip
                distance = ((index_finger_tip.x - thumb_tip.x) ** 2 + (index_finger_tip.y - thumb_tip.y) ** 2) ** 0.5

                # Click if distance is less than a threshold
                if distance < 0.05:
                    pyautogui.click()

        return image

    def run(self):
        while True:
            if self.current_frame is not None:
                processed_frame = self.process_frame(self.current_frame)

                # Display the frame
                cv2.imshow('Hand Tracking', processed_frame)

            if cv2.waitKey(1) & 0xFF == 27:  # Exit on pressing 'Esc'
                break

        # Release resources
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    controller = HandMouseController(dpi_scale=2.0)
    controller.run()
