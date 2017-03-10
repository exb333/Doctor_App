import unittest
import os

from app.read_xml import Xml_Parser


class TestXml_Parser(unittest.TestCase):
	def test_file_path(self):
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		path = os.path.join(BASE_DIR, 'config')
		s = Xml_Parser()
		self.assertRaises(IOError, s.get_file, path)
	def test_get_file(self):
		self.fail()


if __name__ == "__main__":
	unittest.main()


