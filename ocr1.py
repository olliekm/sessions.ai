# Old save (in case needed later)

'''

import cv2
import pytesseract
import numpy as np
import mss
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

captured_text = []

# Real-time screen capture?
with mss.mss() as sct:
    # Define the part of the screen to capture (full screen or specific region)
    monitor = sct.monitors[1]  # Fullscreen

    start_time = time.time()

    while True:
        # Screen capture
        screen_shot = sct.grab(monitor)
        
        # Convert the captured screenshot to NumPy array
        frame = np.array(screen_shot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert frame to grayscale for better OCR

        # Apply OCR on the captured frame
        text = pytesseract.image_to_string(gray_frame)
        
        captured_text.append(text)

        cv2.imshow("Screen", frame) # Display screen capture

        if cv2.waitKey(1) & 0xFF == ord('q') or time.time() - start_time > 5:
            break

    cv2.destroyAllWindows()

# cap = cv2.VideoCapture('')
print("Below is the captured text")
for entry in captured_text:
    print(entry)


'''