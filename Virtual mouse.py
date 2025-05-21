import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
hand = mp.solutions.hands.Hands()
draw = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()

while True:
    success, image = cap.read()
    image = cv2.flip(image, 1)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hand.process(rgb)
    
    if result.multi_hand_landmarks:
        for landmark in result.multi_hand_landmarks:
            draw.draw_landmarks(image, landmark, mp.solutions.hands.HAND_CONNECTIONS)
            for id, lm in enumerate(landmark.landmark):
                h, w, _ = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 8:
                    cv2.circle(image, (cx, cy), 10, (0, 255, 255), -1)
                    screen_x = screen_width / w * cx
                    screen_y = screen_height / h * cy
                    pyautogui.moveTo(screen_x, screen_y)

    cv2.imshow("Virtual Mouse", image)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
