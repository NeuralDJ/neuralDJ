feed = __import__('feed')
emotion = __import__('emotion')
analytics = __import__('analytics')
azurevision = __import__('azurevision')

def GetEmotionFromCameraFeed(fps) :
	frames = feed.getCameraFrames(fps)
	encodedFrames = feed.encodeFrames(frames)
	emotionOutput = emotion.detect_emotion(encodedFrames)
	visionOutput = azurevision.get_visionFeatures(encodedFrames)
	emotionFeatures = analytics.getFeaturesforMusic(emotionOutput)
<<<<<<< HEAD
	visionFeatures = analytics.getVisionforMusic(visionOutput)
	return emotionFeatures,visionFeatures
=======

	print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
	print(emotionFeatures)
	print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
	
	return emotionFeatures
>>>>>>> bc02b9f2841b3fd2e7c1f284c0a0a1d7c50547c4

