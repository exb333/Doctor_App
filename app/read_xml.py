import xml.etree.ElementTree as ET
import os
from collections import defaultdict

class Xml_Parser(object):
	def get_file(self, path):
		lst = []
		dd = defaultdict(list)
		try:
			for filename in os.listdir(path):
				if not filename.endswith('.xml'):continue
				fullname = os.path.join(path, filename)

				tree = ET.parse(fullname)
				root = tree.getroot()
				# print root
				# print fullname
				lst.append(root.get('name'))
				# print root.tag
				# print root.attrib
				# # print root.get('desc')
				# # print root.get('sql')
				# # print root.get('table_to_drop')

				x = root.get('name')

				dict = {}

				for child in root.iter('input'):
					# if not child.attrib['type'] =='csv':
					# print child.tag
					# print child.attrib
					name = child.get('name')
					# print name
					id = child.get('id')
				# print '|-->', name, id
					lsts1.append(name)
					dict[x] = name
					for key, value in dict.iteritems():
						dd[key].append(value)


		except:
			raise IOError


		return dd


	def grab_xml_data(self, root=None):
		x = root.get('name')
		dd = defaultdict(list)
		dict = {}

		for child in root.iter('input'):
			# if not child.attrib['type'] =='csv':
			# print child.tag
			# print child.attrib
			name = child.get('name')
			# print name
			id = child.get('id')
		# print '|-->', name, id
			lsts1.append(name)
			dict[x] = name
			for key, value in dict.iteritems():
				dd[key].append(value)


		# for child in root.iter('country'):
		# 	# if not child.attrib['type'] =='csv':
		# 		# print child.tag
		# 		# print child.attrib
		# 	name = child.find('rank').text
		# 	id = child.get('name')
		# 	# print '|-->',name, id
		# 	lsts.append(id)
		# dict[root.get('name')] = lsts
		return dd

		# print lsts
		# print "This is zip file", dict(zip (lst, lsts))



lsts = []
lsts1 = []


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# path = os.path.join(BASE_DIR, 'config')
# xmlfile = Xml_Parser()
# xmlfile.get_file(path)


# names = [name.text for name in doc.findall('.//name')]
# ages = [age.text for age in doc.findall('.//age')]
# people = dict(zip(names,ages))
# print(people)

# from collections import defaultdict
#
# d1 = {1: 2, 3: 4}
# d2 = {1: 6, 3: 7}
#
# dd = defaultdict(list)
#
# for d in (d1, d2): # you can list as many input dicts as you want here
#     for key, value in d.iteritems():
#         dd[key].append(value)
#
# print(dd)