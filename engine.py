import cv2
import os # Bu satırı ekledik!

class DetectionEngine:
    def __init__(self):
        
        cascade_path = os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml')
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        

    def load_targets(self, folder="Searchings"):
        print("System is ready: OpenCV Face Recognizetion is active .")

    def scan_frame(self, frame):
        """Detect faces on thr camera."""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        
        if len(faces) > 0:
            return "TARGET"
        return None