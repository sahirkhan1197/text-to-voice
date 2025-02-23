from flask import Flask, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/speak", methods=["POST"])
def speak():
    text = request.form.get("text")
    if not text:
        return "Error: No text provided!", 400
    
    language = "hi"  # Set language to Hindi
    tts = gTTS(text=text, lang=language)
    
    filename = "output.mp3"
    tts.save(filename)
    
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
