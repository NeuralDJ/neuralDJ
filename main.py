import time
feed = __import__('feed')
emotion = __import__('emotion')

def run_program():
   print ('started... geting frames')
   
   start_time = time.time()
   frames = feed.getCameraFrames(1)
   print ("get_frames - " + str(time.time() - start_time) +  "s")
   
   start_time = time.time()
   encodedFrames = feed.encodeFrames(frames)
   print ("encode - " + str(time.time() - start_time) +  "s")
   
   emotionOutput = emotion.detect_emotion(encodedFrames)
   print(emotionOutput)
   print ("emotion - " + str(time.time() - start_time) +  "s")

   return 'rock_and_roll_baby! : ' + str(time.time() - start_time)