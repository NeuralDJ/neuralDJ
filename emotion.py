import boto3

def detect_faces(img, attributes=['ALL'], region="us-east-1"):
	rekognition = boto3.client("rekognition", region)
	response = rekognition.detect_faces(
	    Image={
			"Bytes": img
		},
	    Attributes=attributes,
	)
	return response['FaceDetails']