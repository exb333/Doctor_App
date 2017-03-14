import xml.etree.ElementTree as ET
import pandas as pd
import os


class Xml_Parser(object):
	def get_file(self, path):
		lt1 = []
		lt2 = []
		for filename in os.listdir(path):
			if not filename.endswith('.xml'):continue
			fullname = os.path.join(path, filename)
			tree = ET.parse(fullname)
			root = tree.getroot()
			x = root.get('name')
			dic = {}
			lsts1 = []
			for child in root.iter('input'):
				# if not child.attrib['type'] =='csv':
				name = child.get('name')
				lsts1.append(name)
				dic[x] =  lsts1
			for key, value in dic.iteritems():
				lt1.append(key)
				lt2.append(value)
		df = pd.DataFrame(data=lt2, index=lt1)
		return df

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, 'config')
xmlfile = Xml_Parser()
xmlfile.get_file(path)

