import unittest
from exif_extractor.gps import convert_to_degrees, extract_gps

class TestGPS(unittest.TestCase):
    def test_convert_to_degrees(self):
        # (deg, min, sec)
        self.assertAlmostEqual(convert_to_degrees([30, 15, 50]), 30.2638888889)

    def test_extract_gps_empty(self):
        self.assertEqual(extract_gps({}), {})

if __name__ == "__main__":
    unittest.main()
