feed = __import__('feed')
emotion = __import__('emotion')


frames = feed.getCameraFrames(5)

encodedFrames = feed.encodeFrames(frames)

emotionOutput = emotion.detect_emotion(encodedFrames)

print(emotionOutput)
