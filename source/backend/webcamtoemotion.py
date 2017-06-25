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
	visionFeatures = analytics.getVisionforMusic(visionOutput)
	return emotionFeatures,visionFeatures


