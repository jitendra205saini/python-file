# Search google "opencv python" and code and paste and download
import cv2
from numpy import True_
video_cap =cv2.videocapture()
while True:
    ret, video_data = video_cap.read()
    cv2.imshow("video_live",video_data)
    if cv2.waitkey(10) == ord("c"):
        break
    video_cap.release()