from faker import Faker
import unittest
from catalog.core.utils import generate_api_key, upload_image

fake = Faker()
class TestGenerateApiKey(unittest.TestCase):
    def test_apikey_len(self):
        self.api_key = generate_api_key()
        self.assertEqual(len(self.api_key), 50)
    

class TestUploadImageImgbb(unittest.TestCase):
    def test_file_not_found_error(self):
        path_image = '/field/expert/example.jpg'
        with self.assertRaises(FileNotFoundError):
            image = upload_image(path_image,'eita')

    