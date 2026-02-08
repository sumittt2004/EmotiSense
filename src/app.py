import cv2
from face_mesh import FaceMeshDetector
from emotion_rules import get_emotion_with_confidence, calibrate_neutral

MODEL_PATH = "models/face_landmarker.task"

def main():
    detector = FaceMeshDetector(MODEL_PATH)
    cap = cv2.VideoCapture(0)

    show_landmarks = False
    show_emotion = True

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        result = detector.detect(frame)

        if result.face_landmarks:
            landmarks = result.face_landmarks[0]

            # Emotion inference
            emotion, confidence = get_emotion_with_confidence(landmarks)

            # Draw landmarks (optional)
            if show_landmarks:
                for lm in landmarks:
                    x = int(lm.x * frame.shape[1])
                    y = int(lm.y * frame.shape[0])
                    cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

            # Draw emotion text (optional)
            if show_emotion:
                cv2.putText(
                    frame,
                    f"{emotion} ({confidence}%)",
                    (30, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.2,
                    (0, 255, 0),
                    3
                )

                cv2.putText(
                    frame,
                    "C: Calibrate  L: Landmarks  E: Emotion  Q: Quit",
                    (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 255, 255),
                    2
                )

        cv2.imshow("EmotiSense", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('c') and result.face_landmarks:
            calibrate_neutral(result.face_landmarks[0])

        elif key == ord('l'):
            show_landmarks = not show_landmarks

        elif key == ord('e'):
            show_emotion = not show_emotion

        elif key == ord('q') or key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
