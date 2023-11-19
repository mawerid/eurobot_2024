from picamera2 import Picamera2
import time

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start()
time.sleep(0.01)
picam2.capture_file("test.jpg")
