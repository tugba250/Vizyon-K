import cv2
import time
from engine import DetectionEngine


engine = DetectionEngine()
engine.load_targets()


CAMERA_SOURCE = "YOUR_URL_HERE"

def start_scanning():
    print(f"Analize is starting: {CAMERA_SOURCE}")
    
    # 0 yerine CAMERA_SOURCE yazarak canlı yayına bağlanıyoruz
    cap = cv2.VideoCapture(CAMERA_SOURCE)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Cannot access live action or finished.")
            break
            
        display_frame = frame.copy()
    
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        
       
        target_found = engine.scan_frame(small_frame)

        if target_found:
         
            cv2.putText(display_frame, f"TARGET DETECTION: {target_found}", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
         
            with open("alerts.log", "a") as f:
             f.write(f"Target detected at {time.ctime()}\n")

      
        cv2.imshow('Vizyon-K: Analysis Pane', display_frame)

      
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start_scanning()