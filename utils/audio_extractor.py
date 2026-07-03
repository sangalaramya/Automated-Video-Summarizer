from moviepy.editor import VideoFileClip
import os


def extract_audio(video_path, output_folder="outputs"):
    """
    Extracts audio from a video and saves it as audio.wav
    """

    os.makedirs(output_folder, exist_ok=True)

    audio_path = os.path.join(output_folder, "audio.wav")

    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

    video.close()

    return audio_path