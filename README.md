# 🎥 Automated Video Summarizer & Chapter Generator

## 📌 Project Overview

The Automated Video Summarizer & Chapter Generator is an AI-powered application that converts short videos into concise summaries and automatically generates chapter-wise timestamps. The application extracts audio from uploaded videos, converts speech into text using Whisper AI, summarizes the transcript using Facebook BART, and generates meaningful chapter divisions for easy navigation.

---

## ✨ Features

- Upload MP4 video files
- Audio extraction from video
- Speech-to-text transcription using Whisper AI
- AI-generated video summaries
- Automatic chapter generation
- Simple and user-friendly Streamlit interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Whisper AI
- Facebook BART
- Transformers
- PyTorch
- MoviePy
- FFmpeg

---

## 📂 Project Structure

```
Automated_Video_Summarizer/
│
├── app.py
├── requirements.txt
├── utils/
│   ├── audio_extractor.py
│   ├── transcriber.py
│   ├── summarizer.py
│   ├── chapter_generator.py
│   └── helper.py
├── uploads/
├── outputs/
└── README.md
```

---

## 🚀 How to Run

1. Clone the repository

```bash
git clone https://github.com/sangalaramya/Automated-Video-Summarizer.git
```

2. Install the required libraries

```bash
pip install -r requirements.txt
```

3. Run the application

```bash
streamlit run app.py
```

---

## 📸 Output

The application generates:

- Transcript
- AI-generated Summary
- Chapter-wise Timestamps

---

## ⚠️ Limitations

- Best results are obtained with clear audio.
- Processing time depends on video length.
- Summary quality depends on transcription accuracy.

---

## 👩‍💻 Author

**Ramya Sangala**

GitHub: https://github.com/sangalaramya
# Automated Video Summarizer

## Overview
This project is an AI-powered application that converts videos into:
- Transcript
- Summary
- Chapter-wise timestamps

It uses OpenAI Whisper for speech-to-text and BART for text summarization.

## Features
- Upload MP4 videos
- Extract audio
- Generate transcript
- Generate concise summary
- Generate chapter timestamps

## Tech Stack
- Python
- Flask
- OpenAI Whisper
- Transformers (BART)
- FFmpeg

## Project Structure

```
Automated_Video_Summarizer/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│── uploads/
│── outputs/
│── utils/
```

## How to Run

1. Clone the repository

```
git clone https://github.com/sangalaramya/Automated-Video-Summarizer.git
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the application

```
python app.py
```

## Author

Ramya Sangala