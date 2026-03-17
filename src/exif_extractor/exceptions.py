class ExifExtractorError(Exception):
    """Base exception for EXIF extractor."""


class UnsupportedFormatError(ExifExtractorError):
    """Raised when image format is not supported."""


class ExtractionError(ExifExtractorError):
    """Raised when EXIF extraction fails."""
