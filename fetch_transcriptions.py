from twilio.rest import Client
from configure import twilio_auth_key, acct_id

client = Client(acct_id, twilio_auth_key)

transcriptions = client.transcriptions.list()

for record in transcriptions:
    _tid = record.sid
    transcript = client.transcriptions(_tid).fetch()
    print(transcript.transcription_text)