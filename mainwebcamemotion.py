webcamtoemotion = __import__('webcamtoemotion')
numofframes = 5
emotionFeatures = webcamtoemotion.GetEmotionFromCameraFeed(numofframes)
print(emotionFeatures)
