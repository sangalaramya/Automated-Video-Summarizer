def generate_chapters(transcript):
    """
    Generates simple chapter headings from the transcript.
    """

    sentences = transcript.split(".")

    chapters = []

    for i, sentence in enumerate(sentences):
        sentence = sentence.strip()

        if sentence:
            chapters.append(f"Chapter {i+1}: {sentence[:50]}...")

    return chapters