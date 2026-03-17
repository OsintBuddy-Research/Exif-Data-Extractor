import unittest
from pathlib import Path
from exif_extractor.extractor import ExifExtractor

class TestExifExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = ExifExtractor()
        # Use a sample image with known EXIF (you may need to provide one)
        self.sample = Path("data/sample.jpg")

    @unittest.skipIf(not Path("data/sample.jpg").exists(), "Sample image missing")
    def test_extract(self):
        data = self.extractor.extract(str(self.sample))
        self.assertIsInstance(data, dict)

if __name__ == "__main__":
    unittest.main()
