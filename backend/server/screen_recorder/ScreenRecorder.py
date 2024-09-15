import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time


class ScreenRecorder:
    def __init__(self):
        self.unique_text_blocks = []
        self.recent_text = ""
        self.deduplication_threshold = 5
        self.start_time = time.time()

    def capture_screen(self):
        """Grabs the screen, converting it for OpenCV"""
        cap_scr = np.array(ImageGrab.grab())
        cap_scr = cv2.cvtColor(cap_scr, cv2.COLOR_RGB2BGR)
        return cap_scr

    def is_recent(self, text):
        """Check if the text is similar to recent text"""
        return text == self.recent_text

    def run(self, max_runtime=10):
        """Run the screen recorder for a specified amount of time"""
        try:
            while True:
                elapsed_time = time.time() - self.start_time

                if elapsed_time > max_runtime:
                    break

                # Capture the screen
                frame = self.capture_screen()

                # Optionally resize the frame to speed up text recognition
                height, width = frame.shape[:2]
                frame = cv2.resize(frame, (width // 2, height // 2))

                # Perform text detection on the captured screen frame
                recognized_text = pytesseract.image_to_string(frame).strip()

                # Only add text if it's different from recent text
                if not self.is_recent(recognized_text):
                    self.unique_text_blocks.append(recognized_text)
                    self.recent_text = recognized_text

                # Calculate the time taken for this iteration
                frame_elapsed_time = time.time() - self.start_time

                # If capturing too quickly, sleep to reduce CPU load
                if frame_elapsed_time < 0.5:  # Capture frame every 500ms
                    time.sleep(0.5 - frame_elapsed_time)

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            # Release resources and close OpenCV windows
            cv2.destroyAllWindows()

        self.unique_text_blocks = "\n".join(self.unique_text_blocks)

        return self.unique_text_blocks
