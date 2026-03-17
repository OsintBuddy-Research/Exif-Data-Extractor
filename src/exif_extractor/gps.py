"""
GPS coordinate conversion utilities.
"""

def convert_to_degrees(value):
    """Convert GPS coordinates from (degrees, minutes, seconds) to decimal degrees."""
    d = float(value[0])
    m = float(value[1])
    s = float(value[2])
    return d + (m / 60.0) + (s / 3600.0)


def extract_gps(exif_data):
    """Extract GPS latitude/longitude from EXIF data if present."""
    gps = {}

    if "gps_latitude" in exif_data and "gps_longitude" in exif_data:
        try:
            lat = convert_to_degrees(exif_data["gps_latitude"])
            lon = convert_to_degrees(exif_data["gps_longitude"])
            gps["latitude"] = lat
            gps["longitude"] = lon
        except (KeyError, TypeError, IndexError):
            pass

    return gps
