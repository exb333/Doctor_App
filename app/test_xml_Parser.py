from unittest import TestCase
from read_xml import Xml_Parser
import os
__author__ = 'bordee'


class TestXml_Parser(TestCase):
	def test_file_path(self):
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		path = os.path.join(BASE_DIR, 'config')
		path1 = os.path.join(BASE_DIR, 'config')
		s = Xml_Parser()
		self.assertEqual(s.get_file(path), path1)
	# def test_get_file(self):
	#
	# 	self.fail()
