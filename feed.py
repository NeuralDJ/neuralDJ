import numpy as np
import cv2
import time
import base64
import boto3 
from PIL import Image

def getCameraFrames(frameCount):
   frameList = []

   maxTries = frameCount*2
   cap = cv2.VideoCapture(0)

   while(frameCount > 0):
     ret, frame = cap.read()

     if(ret):
       frameList.append(frame)
       frameCount = frameCount - 1
     
     maxTries = maxTries - 1
     if(maxTries < 0):
       break

   return frameList

def encodeFrames(frameList):
   encodedList = []
   for frame in frameList:
     temp = cv2.imencode('.jpg',frame)
     if(temp[0]):
       encodedList.append(temp[1])

   return encodedList