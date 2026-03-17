"""
Command-line interface for EXIF Extractor.
"""
import argparse
import sys

from .extractor import ExifExtractor
from .formatter import format_text, format_json
from .scanner import scan_directory


def main():
    parser = argparse.ArgumentParser(
        description="EXIF Metadata Extraction Tool (Production Grade)"
    )
    parser.add_argument("target", help="Image file or folder (if --scan is used)")
    parser.add_argument(
        "--library",
        choices=["exif", "exifread"],
        default="exif",
        help="Backend library to use (default: exif)"
    )
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--tag", help="Show only a specific tag")
    parser.add_argument("--scan", action="store_true", help="Scan folder recursively")

    args = parser.parse_args()

    extractor = ExifExtractor(args.library)

    try:
        if args.scan:
            files = scan_directory(args.target)
            for f in files:
                data = extractor.extract(str(f))
                print(f"\nFILE: {f}")
                print(format_text(data))
            return 0

        data = extractor.extract(args.target)

        if args.tag:
            print(data.get(args.tag, "Tag not found"))
            return 0

        if args.json:
            print(format_json(data))
            return 0

        print(format_text(data))

    except KeyboardInterrupt:
        return 130
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
