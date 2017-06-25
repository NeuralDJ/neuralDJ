feed = __import__('feed')
emotion = __import__('emotion')
analytics = __import__('analytics')


def GetEmotionFromCameraFeed(fps) :
	frames = feed.getCameraFrames(fps)
	encodedFrames = feed.encodeFrames(frames)
	emotionOutput = emotion.detect_emotion(encodedFrames)
	emotionFeatures = analytics.getFeaturesforMusic(emotionOutput)
	
	return emotionFeatures

