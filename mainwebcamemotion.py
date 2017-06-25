webcamtoemotion = __import__('webcamtoemotion')
fps = 5
emotionFeatures = webcamtoemotion.GetEmotionFromCameraFeed(fps)
print(emotionFeatures)
