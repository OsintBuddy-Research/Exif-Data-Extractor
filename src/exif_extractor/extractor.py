"""
Core EXIF extraction engine with multiple backends.
"""
from pathlib import Path
from typing import Dict, Any

from .exceptions import ExtractionError
from .logger import get_logger

log = get_logger(__name__)


class ExifExtractor:
    """Main extractor class with pluggable backends."""

    def __init__(self, backend: str = "exif"):
        self.backend = backend

    def extract(self, image_path: str) -> Dict[str, Any]:
        """Extract EXIF metadata from an image file."""
        path = Path(image_path)

        if not path.exists():
            raise ExtractionError(f"File not found: {image_path}")

        if self.backend == "exif":
            return self._extract_exif(path)
        elif self.backend == "exifread":
            return self._extract_exifread(path)
        else:
            raise ExtractionError(f"Unsupported backend: {self.backend}")

    def _extract_exif(self, path: Path) -> Dict[str, Any]:
        """Extract using the 'exif' library."""
        try:
            from exif import Image
        except ImportError:
            raise ExtractionError("exif library not installed")

        with open(path, "rb") as f:
            img = Image(f)

        if not img.has_exif:
            return {}

        data = {}
        for attr in dir(img):
            if attr.startswith("_"):
                continue
            try:
                value = getattr(img, attr)
                if not callable(value):
                    data[attr] = value
            except Exception:
                continue
        return data

    def _extract_exifread(self, path: Path) -> Dict[str, Any]:
        """Extract using the 'exifread' library."""
        try:
            import exifread
        except ImportError:
            raise ExtractionError("exifread library not installed")

        with open(path, "rb") as f:
            tags = exifread.process_file(f)

        return {k: str(v) for k, v in tags.items()}
