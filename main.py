import cv2
import datetime

def record_video(duration=60):
    cap = cv2.VideoCapture(0)
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    out = cv2.VideoWriter(f'video_{timestamp}.avi', fourcc, 20.0, (640, 480))
    
    start_time = datetime.datetime.now()
    
    while (datetime.datetime.now() - start_time).seconds < duration:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            break
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    record_video()
