import whisper
import os

def transcribe_audio(audio_file):
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    return result["text"]

if __name__ == "__main__":
     audio_path = os.path.join(os.getcwd(), "data", "meeting_audio.wav")
     text = transcribe_audio(audio_path)
     print("Transcribed Text:\n", text)
