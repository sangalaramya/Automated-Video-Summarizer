import whisper


def transcribe_audio(audio_path):
    """
    Transcribes the audio using OpenAI Whisper.
    """

    model = whisper.load_model("base")

    result = model.transcribe(audio_path)

    return result["text"]