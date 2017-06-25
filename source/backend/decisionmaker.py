webcamtoemotion = __import__('webcamtoemotion')

def getDecisionForSongChange(calltyp = 'emotion'):
	numofframes = 5

	emotionFeatures,visionFeatures = webcamtoemotion.GetEmotionFromCameraFeed(numofframes)
	#emotionFeatues(dic) has the mode of the features of the faces(numofframes*numoffacesineachframe)
	#keys of dic - age,smile,gender,emotion
	decision = {}

	print(emotionFeatures)

	if calltyp == 'features':
		if emotionFeatures['age']:
			age = emotionFeatures['age']
			if age < 13:
				decision['age'] = 'young'
			elif age >= 13 and age < 40:
				decision['age'] = 'mid'
			else:
				decision['age'] = 'old'
		if emotionFeatures['gender']:
			decision['gender'] = emotionFeatures['gender']
		if visionFeatures:
			decision['scene'] = visionFeatures
	else:
		if emotionFeatures['emotion']:
			emotion = emotionFeatures['emotion']
			if emotion == 'HAPPY' or emotion == 'UNKNOWN':
				decision['changeSong'] = 'no'
			else:
				decision['changeSong'] = 'yes'
	return decision

