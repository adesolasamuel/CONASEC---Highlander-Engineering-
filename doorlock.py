#from gpiozero.pins.native import NativeFactory
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np 
import pickle
from gpiozero import Servo, Device
from time import sleep
#Device.pin_factory = NativeFactory()

servo = Servo(17) # The gpio pin the servo is connected 
servo.min()

with open('labels', 'rb') as f:
    dict = pickle.load(f)
    f.close()

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480))


faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

font = cv2.FONT_HERSHEY_SIMPLEX

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    frame = frame.array
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
    for (x, y, w, h) in faces:
        roiGray = gray[y:y+h, x:x+w]

        id_, conf = recognizer.predict(roiGray)

        for name, value in dict.items():
            if value == id_:
                print(name)
                if name == "Sam":
                    servo.max()
                    break;
                else:
                    servo.min()

        #if conf <= 50:
            #servo.max()
            #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            #cv2.putText(frame, name + str(conf), (x, y), font, 2, (0, 0 ,255), 2,cv2.LINE_AA)

        else:
            servo.min()

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)

    rawCapture.truncate(0)

    if key == 27:
        break

cv2.destroyAllWindows()
