webcamtoemotion = __import__('webcamtoemotion')
numofframes = 5
emotionFeatures = webcamtoemotion.GetEmotionFromCameraFeed(numofframes)
#emotionFeatues has the mode of the features of (numofframes*numoffacesineachframe)
print(emotionFeatures)
