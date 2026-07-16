from faster_whisper import WhisperModel


def transcribe_audio(audio_path):
    """
    Transcribes audio using Faster Whisper.
    """

    # Load the model
    model = WhisperModel("base", device="cpu", compute_type="int8")

    # Transcribe
    segments, info = model.transcribe(audio_path)

    # Combine all text
    transcript = ""
    for segment in segments:
        transcript += segment.text + " "

    return transcript.strip()