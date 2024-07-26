import cv2
import numpy as np
import csv
import face_recognition as fr
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import subprocess

face_recognized = False
sony_image = fr.load_image_file("/home/rguktongole/Downloads/WhatsApp Image 2023-11-28 at 10.55.13 PM (1).jpeg")
sony_encoding = fr.face_encodings(sony_image)[0]
suvarna_image = fr.load_image_file("/home/rguktongole/Pictures/wai/IMG_20220419_093512.jpg")
suvarna_encoding = fr.face_encodings(suvarna_image)[0]
malli_image = fr.load_image_file("/home/rguktongole/Downloads/WhatsApp Image 2023-12-06 at 2.09.48 PM.jpeg")
malli_encoding = fr.face_encodings(malli_image)[0]
video_capture = cv2.VideoCapture(0)
known_face_encoding = [sony_encoding, suvarna_encoding, malli_encoding]
known_faces_names = ["vathsalya", "suvarna", "malli"]

while True:
    ret, frame = video_capture.read()
    rgb_small_frame = np.ascontiguousarray(frame[:, :, ::-1])

    fc_locations = fr.face_locations(rgb_small_frame)
    fc_encodings = fr.face_encodings(rgb_small_frame, fc_locations)

    face_recognized = False 
    for (top, right, bottom, left), face_encoding in zip(fc_locations, fc_encodings):
        matches = fr.compare_faces(known_face_encoding, face_encoding)

        name = "not matched"

        fc_distances = fr.face_distance(known_face_encoding, face_encoding)
        match_index = np.argmin(fc_distances)


        if matches[match_index]:
            name = known_faces_names[match_index]
            face_recognized = True  
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('candi-connect', frame)
    
    if face_recognized:
        if cv2.waitKey(1) & 0xFF == ord('e'):
            subprocess.run(["python3", "v.py"])
            break
video_capture.release()
cv2.destroyAllWindows()
