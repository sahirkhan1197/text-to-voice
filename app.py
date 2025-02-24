from flask import Flask, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/speak", methods=["GET", "POST"])
def speak():
    if request.method == "POST":
        text = request.form.get("text")
    else:  # Allow GET requests for easier testing
        text = request.args.get("text", "नमस्ते")

    if not text or text.strip() == "":
        return "Error: No text provided!", 400

    language = "hi"  # Hindi language
    tts = gTTS(text=text, lang=language)

    filename = "output.mp3"
    tts.save(filename)

    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    from waitress import serve
    port = int(os.environ.get("PORT", 8080))  # Render requires 8080
    serve(app, host="0.0.0.0", port=port)
