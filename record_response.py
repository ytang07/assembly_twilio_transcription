from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=["GET", "POST"])
def voice():
    """Read a message aloud"""
    resp = VoiceResponse()
    resp.say("Please leave a message")
    resp.record(timeout=10, transcribe=True)
    resp.hangup()
    return(str(resp))

if __name__ == "__main__":
    app.run(debug=True)