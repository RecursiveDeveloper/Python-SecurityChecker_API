# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 16:35:21 2021

@author: Jhoan
"""

import cv2
import os
import dlib

class faceDetection:

    def get_Camera_Frame(self,videoCaptureCv2,ds_factor,CascadeClassifier,detector):
        ret, frame = videoCaptureCv2.read()
        frame = cv2.flip(frame, 1)
        frame = cv2.resize(
            frame,None,
            fx = ds_factor,
            fy = ds_factor,
            interpolation = cv2.INTER_AREA
        )           
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        faces = detector(gray)
        ######## Counter to count number of faces
        i = 0
        for face in faces:
            x, y = face.left(), face.top()
            x1, y1 = face.right(), face.bottom()
            cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
            # Increment the iterartor each time you get the coordinates
            i = i+1
            # Adding face number to the box detecting faces
            cv2.putText(
                frame, 'face num'+str(i), (x-10, y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 
                2
            )
            #print(face, i)
        ########

        face_rects = CascadeClassifier.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x,y,w,h) in face_rects:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        # encode OpenCV raw frame to jpg and displaying it
        ret, image = cv2.imencode('.jpg', frame)
        return image.tobytes()

    def faceDetectionStartUp(self):
        #cascPath=haarcascade_frontalface_default.xml"
        cascPath = "Apis/ImageDetection/Files/haarcascades/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)
        ds_factor = 0.6
        video_capture = cv2.VideoCapture(0)
        detector = dlib.get_frontal_face_detector()
        
        while True:
            frames = faceDetection.get_Camera_Frame(self,video_capture,ds_factor,faceCascade,detector)
            yield b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + frames + b"\r\n"
            
        video_capture.release()
        cv2.destroyAllWindows()

"""
Code extracted from: 
https://techvidvan.com/tutorials/face-recognition-project-python-opencv/
https://medium.datadriveninvestor.com/video-streaming-using-flask-and-opencv-c464bf8473d6
https://github.com/parzibyte/tomar_foto_flask_python/blob/main/app.py
https://www.geeksforgeeks.org/count-number-of-faces-using-python-opencv/
"""