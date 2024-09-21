# 8.WHILE LOOPS
#I HAVE DISABLED THE NEXT FEW LINES OF CODE TO PREVENT US FROM BEING STUCK IN AN ENDLESS LOOP💀.

#if 1 == 1:
#    print("I am stuck in a loop")

#while 1 == 1:
#   print("I am stuck in a loop")        #while loop will repeat the same block
                                         #forever as long as condition remains true.

name = input("Enter your name: ")

while name == "":
    name = input("Enter your name: ")

print(f"Hello {name}!")                   #if name is not typed then you will be stuck in a while loop.

age = int(input("Enter your age: "))

while age < 0:

    print("Age can't be less than 0")
    age = int(input("Enter your age: "))   #here age can be 0 or more.
                                           #or else u will be in a loop


# 9.FOR LOOPS
#used to repeat a block of code an exact amount of times.

for i in range(1, 5):        #here 1 is inclusive and 5 is exclusive while counting
    print(i)

print("")                    #just leaving space in between.🙂

for i in range(1, 10, 2):
    print(i)                 #here it counts from 1 to 10 but in intervals of 2.

print("")                    #just leaving space in between.🙂

name = "Joe"

for letter in name:
    print(letter)            #my name is spelled out

print("")                    #just leaving space in between.🙂

for letter in name:
    print(letter, end="-")   #my name is spelled out but with '-' after every letter ends

print("")                    #just leaving space in between.🙂



# 10.COUNTDOWN TIMER

import time

for i in range(10, 0, -1):
    print(i)                 #here it counts backwards in intervals of 1.
    time.sleep(1)            #also note that the 2nd number (here 0) is exclusive.
                             #importing time module made it start a countdown and sleep(1) made it countdown in intervals of 1 sec.
print("Happy New Year!")





#EXTRA 1
#how to play audio using playsound module.(You must install playsound for this to work)

#TOOK ME QUITE SOME TIME TO GET RIGHT🫠.
from playsound3 import playsound
# Replace '/Users/User/Downloads/song.mp3' with the path to your audio file.
playsound('/Users/User/Downloads/song.mp3')



#EXTRA 2
#how to play video using cv2.(You must install cv2 fot this to work)

#THIS ALSO TOOK ME SOME TIME TO DO. BUT IT WAS WORTH IT IN THE END.
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
