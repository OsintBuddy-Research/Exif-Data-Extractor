"""
Directory scanner for image files.
"""
from pathlib import Path

IMAGE_EXT = {".jpg", ".jpeg", ".tiff", ".png", ".jfif"}

def scan_directory(folder):
    """Recursively scan a folder for image files."""
    files = []
    for file in Path(folder).rglob("*"):
        if file.suffix.lower() in IMAGE_EXT:
            files.append(file)
    return files
