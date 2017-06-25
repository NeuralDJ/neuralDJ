import numpy as np
import cv2
import time
import base64
import boto3 
from PIL import Image

def read_frame(cap):
    # Capture frame-by-frame
   ret, frame = cap.read()
   #cv2.imshow('frame',frame)
   return frame

# When everything done, release the capture

def detect_faces(img, attributes=['ALL'], region="us-east-1"):
	rekognition = boto3.client("rekognition", region)
	response = rekognition.detect_faces(
	    Image={
			"Bytes": img
		},
	    Attributes=attributes,
	)
	return response['FaceDetails']

if __name__ == "__main__":
	ImageList = []
	ct = 0
	faces = []

	cap = cv2.VideoCapture(0)
	
	while(ct < 5):
	 img = read_frame(cap)
	 jpgencode = cv2.imencode('.jpg',img)
	 ImageList.append(jpgencode)
	 ct=ct+1
	 if cv2.waitKey(1) & 0xFF == ord('q'):
	   	break

	for imag in ImageList:
		face = detect_faces(img=imag[1].tostring())
		faces.append(face)
	print(faces)

	