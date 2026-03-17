"""
Output formatters for EXIF data.
"""
import json

def format_text(data):
    """Format EXIF data as human-readable text."""
    lines = []
    for k, v in data.items():
        lines.append(f"{k:30} : {v}")
    return "\n".join(lines)


def format_json(data):
    """Format EXIF data as pretty JSON."""
    return json.dumps(data, indent=2, default=str)
