import json
import statistics

def getFeaturesforMusic(FramesList):
	MusicFeatures = []
	age = []
	smile = []
	gender = []
	emotion = []
	for Frame in FramesList:
		for Faces in Frame:
			if Faces['AgeRange']:
				age.append((Faces['AgeRange']['Low']+Faces['AgeRange']['High'])/2)
			if Faces['Smile']:
				smile.append(Faces['Smile']['Value'])
			if Faces['Gender']:
				gender.append(Faces['Gender']['Value'])
			if Faces['Emotions']:
				emotion.append(Faces['Emotions'][0]['Type'])

	MusicFeatures.append(statistics.mode(age))
	MusicFeatures.append(statistics.mode(smile))
	MusicFeatures.append(statistics.mode(gender))
	MusicFeatures.append(statistics.mode(emotion))
	return MusicFeatures


