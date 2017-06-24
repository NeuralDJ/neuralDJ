feed = __import__('feed')
emotion = __import__('emotion')


frames = feed.getCameraFrames(5)

encodedFrames = feed.encodeFrames(frames)

faces = []
for imag in encodedFrames:
  face = emotion.detect_faces(img=imag.tostring())
  faces.append(face)

print(faces)
