import requests
import subprocess
import sys
import urllib

def detect_visionFeature(img):
    subscription_key = 'b374d9b47f2f4b25900b5b68a976a3b2'
    api_url = 'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/analyze'

    headers = {
        # Request headers.
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }

    params = urllib.urlencode({
        # Request parameters. All of them are optional.
        'visualFeatures': 'Tags',
        'language': 'en',
    })

    # The URL of a JPEG image to analyze.
    r = requests.post(api_url,
                      params=params,
                      headers=headers,
                      data=img)
    r.raise_for_status()
    data = r.json()
    tags = []
    if data['tags']:
        for tag in data['tags']:
            tags.append(tag['name'])
    return tags

def get_visionFeatures(encodedFrames):
    visionFeatures = []
    for imag in encodedFrames:
      visionFeature = detect_visionFeature(img=imag.tostring())
      visionFeatures.append(visionFeature)
    return visionFeatures



