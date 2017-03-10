from PyQt4 import QtGui, QtCore
from read_xml import Xml_Parser
from functools import partial
import read_xml
# from StyleSet import stylish



class Column_Window(QtGui.QWidget):
	def __init__(self, val=None):
		QtGui.QWidget.__init__(self)
		# stylish(self)

		# check_API(self.id, self.sheet, self.user, self.passwrd)
		self.val = val
		self.vbox = QtGui.QHBoxLayout()
		self.mygroupbox = QtGui.QGroupBox()
		myform = QtGui.QFormLayout()
		self.font = QtGui.QFont()
		palette = QtGui.QPalette()

		self.font.setPointSize(12)
		self.font.setBold(True)
		self.font.setWeight(50)

# 		dic = {'a':'111', 'b':'222', 'c':'333'}
#
# def create_connect(x):
#     return lambda: doit(x)
#
# for key in dic:
#     btn = QPushButton(key, self)
#     btn.clicked.connect(create_connect(dic[key]))
		for index, vals in self.val.iteritems():
			# print index, vals
			# self.btn_no = str(index).replace(" ", "_")
		# TextField are generated dynamically
			button=QtGui.QPushButton(index, self)
			button.setFixedWidth(100)
			# exec('self.button_'+str(self.btn_no)+'.setText("'+ str(index) +'")')
			# exec('self.button_'+str(self.btn_no)+'.setPalette(palette)')
			# exec('self.button_'+str(self.btn_no)+'.setFont(self.font)')
			button.clicked.connect(partial(self.post_json, vals))
			self.vbox.addWidget(button)




			# ButtonBox = QtGui.QGroupBox()
			# ButtonsLayout = QtGui.QHBoxLayout()
			#
			# Button_01 = QtGui.QPushButton("Post")
			# Button_01.clicked.connect(self.post_json)
			#
			# Button_02 = QtGui.QPushButton("Recover")
			# # Button_02.clicked.connect(self.backup_button)


			# ButtonsLayout.addWidget(Button_01)
			# ButtonsLayout.addWidget(Button_02)
			#
			#
			# ButtonBox.setLayout(ButtonsLayout)


			scroll = QtGui.QScrollArea()
			scroll.setWidget(self.mygroupbox)
			scroll.setWidgetResizable(True)
			scroll.setFixedHeight(800)
			layout = QtGui.QVBoxLayout()
			layout.addWidget(scroll)
			# layout.addWidget(ButtonBox)
			self.setGeometry(500, 100, 800, 400)
			self.setLayout(self.vbox)
			self.show()



	def doit(self, text):
		print "%s" % text
	def post_json(self, x):

		print x
		# 	if key == eval( 'self.button_'+str(self.btn_no)+'.text()' ):
		# 		print value
		# replace(lst)


	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())



if __name__ == '__main__':
	import sys
	import os
	app = QtGui.QApplication(sys.argv)
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	path = os.path.join(BASE_DIR, 'config')
	xmlfile = Xml_Parser()
	y = xmlfile.get_file(path)
	# xy = xmlfile.grab_xml_data()
	# print xy
	window = Column_Window(y)
	sys.exit(app.exec_())