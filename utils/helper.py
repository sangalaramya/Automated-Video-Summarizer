import os


def ensure_directories():
    """
    Creates required folders if they don't exist.
    """

    os.makedirs("uploads", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)