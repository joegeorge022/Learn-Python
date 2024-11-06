#EXTRA 1
#how to play audio using playsound module.(You must install playsound module for this to work)

from playsound3 import playsound
# Replace '/Users/User/Downloads/song.mp3' with the path to your audio file.
playsound('/Users/User/Downloads/song.mp3')



#EXTRA 2
#how to play video using cv2.(You must install cv2 fot this to work)

import cv2

# Replace '/Users/User/Downloads/video.mp4' with the path to your video file.
video_path = '/Users/User/Downloads/video.mp44'
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting ...")
        break

    cv2.imshow('Video', frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

