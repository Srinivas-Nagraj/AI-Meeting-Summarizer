from flask import Flask, request, render_template, jsonify
import os
from werkzeug.utils import secure_filename
from speech_to_text import transcribe_audio
from summarize import summarize_text
from extract_actions import extract_action_items

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_audio():
    if "audio" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["audio"]
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(file_path)

    if not os.path.exists(file_path):
        return jsonify({"error": f"File not found: {file_path}"}), 400

    transcript = transcribe_audio(file_path)
    summary = summarize_text(transcript)
    action_items = extract_action_items(transcript)

    return jsonify({"transcript": transcript, "summary": summary, "action_items": action_items})

if __name__ == "__main__":
    app.run(debug=True)
