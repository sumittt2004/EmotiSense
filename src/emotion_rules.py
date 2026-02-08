import math
from collections import deque

# -----------------------------
# CONFIG
# -----------------------------
SMOOTHING_WINDOW = 10

# -----------------------------
# STATE
# -----------------------------
emotion_history = deque(maxlen=SMOOTHING_WINDOW)

baseline = {
    "mouth": None,
    "eye": None,
    "brow": None
}

# -----------------------------
# UTILITIES
# -----------------------------
def distance(p1, p2):
    return math.hypot(p1.x - p2.x, p1.y - p2.y)

# -----------------------------
# CALIBRATION
# -----------------------------
def calibrate_neutral(landmarks):
    """Capture user's neutral facial state"""

    # Mouth
    mouth_open = distance(landmarks[13], landmarks[14])
    mouth_width = distance(landmarks[61], landmarks[291])
    baseline["mouth"] = mouth_open / mouth_width

    # Eyes
    left_eye = distance(landmarks[159], landmarks[145])
    right_eye = distance(landmarks[386], landmarks[374])
    baseline["eye"] = (left_eye + right_eye) / 2

    # Brows
    baseline["brow"] = (landmarks[105].y + landmarks[334].y) / 2

# -----------------------------
# EMOTION LOGIC
# -----------------------------
def get_emotion_with_confidence(landmarks):
    if baseline["mouth"] is None:
        return "Calibrate", 0

    # ---- Current measurements ----
    mouth_open = distance(landmarks[13], landmarks[14])
    mouth_width = distance(landmarks[61], landmarks[291])
    mouth_ratio = mouth_open / mouth_width

    left_eye = distance(landmarks[159], landmarks[145])
    right_eye = distance(landmarks[386], landmarks[374])
    eye_open = (left_eye + right_eye) / 2

    brow = (landmarks[105].y + landmarks[334].y) / 2

    # ---- Relative changes ----
    mouth_delta = mouth_ratio - baseline["mouth"]
    eye_delta = eye_open - baseline["eye"]
    brow_delta = brow - baseline["brow"]

    # ---- Default ----
    emotion = "Neutral 😐"
    confidence = 55

    # ---- Rules (ordered by priority) ----
    if mouth_delta > 0.10 and eye_delta > 0.015:
        emotion = "Surprise 😲"
        confidence = min(100, int((mouth_delta / 0.18) * 100))

    elif mouth_delta > 0.06:
        emotion = "Happy 😊"
        confidence = min(100, int((mouth_delta / 0.12) * 100))

    elif brow_delta > 0.02 and eye_delta < -0.005:
        emotion = "Angry 😠"
        confidence = min(100, int((brow_delta / 0.05) * 100))

    elif mouth_delta < -0.04 and eye_delta < -0.01:
        emotion = "Sad 😢"
        confidence = min(100, int((abs(mouth_delta) / 0.08) * 100))

    # ---- Temporal smoothing ----
    emotion_history.append((emotion, confidence))

    # Most frequent emotion
    emotions = [e for e, _ in emotion_history]
    final_emotion = max(set(emotions), key=emotions.count)

    # Average confidence of that emotion
    confs = [c for e, c in emotion_history if e == final_emotion]
    final_confidence = sum(confs) // len(confs)

    return final_emotion, final_confidence
