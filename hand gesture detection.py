import cv2
import mediapipe as mp

# 1. Initialize MediaPipe Hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.9)
mp_draw = mp.solutions.drawing_utils

# 2. Start Webcam
cap = cv2.VideoCapture(0)

print("Project is running... Press 'q' to exit.")

while cap.isOpened():
    success, img = cap.read()
    if not success:
        break

    # Convert image to RGB (MediaPipe needs RGB)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    # 3. Draw Hand Landmarks
    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            # Draw the skeleton lines and dots
            mp_draw.draw_landmarks(img, hand_lms, mp_hands.HAND_CONNECTIONS)
            
            # Example: Get specific finger tip coordinates
            for id, lm in enumerate(hand_lms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 5: # Index finger tip
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

    # Display the result
    cv2.imshow("Hand Gesture Project", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
