import cv2
import mediapipe as mp
import pyautogui

class HandMouseController:
    def _init_(self, dpi_scale=1):
        # Initialize Mediapipe Hands and Drawing
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_drawing = mp.solutions.drawing_utils

        # Define the DPI scaling factor
        self.DPI_SCALE = dpi_scale

    def process_frame(self, frame):
        # Flip the frame horizontally for a later selfie-view display
        image = cv2.flip(frame, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Process the frame and get hand landmarks
        results = self.hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                # Extract landmarks for the index finger tip, middle finger tip, and thumb tip
                index_finger_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
                middle_finger_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
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

                # Calculate the distance between the index finger tip and the thumb tip
                left_click_distance = ((index_finger_tip.x - thumb_tip.x) ** 2 + (index_finger_tip.y - thumb_tip.y) ** 2) ** 0.5

                # Calculate the distance between the middle finger tip and the thumb tip
                right_click_distance = ((middle_finger_tip.x - thumb_tip.x) ** 2 + (middle_finger_tip.y - thumb_tip.y) ** 2) ** 0.5

                # Left click if distance between index finger tip and thumb tip is less than a threshold
                if left_click_distance < 0.05:
                    pyautogui.click()

                # Right click if distance between middle finger tip and thumb tip is less than a threshold
                elif right_click_distance < 0.05:
                    pyautogui.rightClick()

        return image
