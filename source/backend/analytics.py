import statistics
from sets import Set

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

	EmotionFeatures = {}
	EmotionFeatures['age'] = 27
	EmotionFeatures['gender'] = 'male'
	EmotionFeatures['smile'] = 'yes'
	EmotionFeatures['emotion'] = 'SAD'

	if age:
		try:
    			EmotionFeatures['age'] = statistics.mode(age)
		except statistics.StatisticsError:
    			EmotionFeatures['age'] = age[0]

	if smile:
		try:
			EmotionFeatures['smile'] = statistics.mode(smile)
		except statistics.StatisticsError:
			EmotionFeatures['smile'] = smile[0]

	if gender:
		try:
			EmotionFeatures['gender'] = statistics.mode(gender)
		except statistics.StatisticsError:
			EmotionFeatures['gender'] = gender[0]

	if emotion:
		try:
			EmotionFeatures['emotion'] = statistics.mode(emotion)
		except statistics.StatisticsError:
			EmotionFeatures['emotion'] = emotion[0]

	return EmotionFeatures

def getVisionforMusic(VisionFeaturesList):
	visionFeatures = set()
	for features in VisionFeaturesList:
		visionFeatures.update(features)
	visionFeatures = [str(x) for x in visionFeatures]
	return visionFeatures

