from configure import assembly_auth_key
import requests
import json
from time import sleep

transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
upload_endpoint = 'https://api.assemblyai.com/v2/upload'
headers = {
    "authorization": assembly_auth_key,
    "content-type": "application/json"
}
CHUNK_SIZE = 5242880

def read_file(location):
    with open(location, 'rb') as _file:
        while True:
            data = _file.read(CHUNK_SIZE)
            if not data:
                break
            yield data

location = input("Which file do you want to transcribe?")

upload_response = requests.post(
    upload_endpoint,
    headers=headers, data=read_file(location)
)
audio_url = upload_response.json()['upload_url']
print('Uploaded to', audio_url)
transcript_request = {
    'audio_url': audio_url,
    'iab_categories': 'True'
}

transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
transcript_id = transcript_response.json()['id']
polling_endpoint = transcript_endpoint + "/" + transcript_id
print("Transcribing at", polling_endpoint)
polling_response = requests.get(polling_endpoint, headers=headers)
while polling_response.json()['status'] != 'completed':
    sleep(5)
    print("Transcript processing ...")
    try:
        polling_response = requests.get(polling_endpoint, headers=headers)
    except:
        print("Expected to wait 30 percent of the length of your video")
        print("After wait time is up, call poll with id", transcript_id)
categories_filename = transcript_id + '_categories.json'
with open(categories_filename, 'w') as f:
    f.write(json.dumps(polling_response.json()['iab_categories_result']))
print('Categories saved to', categories_filename)