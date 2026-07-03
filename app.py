import streamlit as st
import os

from utils.audio_extractor import extract_audio
from utils.transcriber import transcribe_audio
from utils.summarizer import summarize_text
from utils.chapter_generator import generate_chapters
from utils.helper import ensure_directories


st.set_page_config(
    page_title="Automated Video Summarizer",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 Automated Video Summarizer")
st.write("Upload a video and get AI-generated summaries and chapters.")

ensure_directories()

uploaded_file = st.file_uploader(
    "Upload a video",
    type=["mp4", "mov", "avi", "mkv"]
)

if uploaded_file is not None:

    video_path = os.path.join("uploads", uploaded_file.name)

    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("Video uploaded successfully!")

    if st.button("Generate Summary"):

        with st.spinner("Extracting Audio..."):
            audio_path = extract_audio(video_path)

        with st.spinner("Transcribing Audio..."):
            transcript = transcribe_audio(audio_path)

        with st.spinner("Generating Summary..."):
            summary = summarize_text(transcript)

        with st.spinner("Generating Chapters..."):
            chapters = generate_chapters(transcript)

        st.header("📝 Transcript")
        st.write(transcript)

        st.header("📌 Summary")
        st.success(summary)

        st.header("📚 Chapters")

        for chapter in chapters:
            st.write(chapter)