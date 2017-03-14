from PyQt4 import QtGui, QtCore
from read_xml import Xml_Parser
from functools import partial
# from StyleSet import stylish


class Column_Window(QtGui.QWidget):
	def __init__(self, val=None):
		QtGui.QWidget.__init__(self)

		self.vbox = QtGui.QHBoxLayout()
		self.gbox = QtGui.QGridLayout()
		self.mygroupbox = QtGui.QGroupBox()
		myform = QtGui.QFormLayout()
		self.font = QtGui.QFont()
		palette = QtGui.QPalette()

		self.font.setPointSize(12)
		self.font.setBold(True)
		self.font.setWeight(90)
		for index, vals in val.iterrows():
		# Buttons are generated dynamically
			self.button=QtGui.QPushButton(index, self)
			self.button.setFixedWidth(100)
			self.button.clicked.connect(partial(self.get_values, vals))
			self.vbox.addWidget(self.button)

			scroll = QtGui.QScrollArea()
			scroll.setWidget(self.mygroupbox)
			scroll.setWidgetResizable(True)
			scroll.setFixedHeight(800)
			layout = QtGui.QVBoxLayout()
			layout.addWidget(scroll)

		# spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		# self.vbox.addItem(spacerItem, 1, 1, 1, 1)
		# self.gbox.addLayout(self.vbox, 0, 6)
		self.setGeometry(500, 100, 800, 400)
		self.setLayout(self.vbox)
		self.show()




	def get_values(self, text):
		for i in text:
			print "%s" % i


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
	window = Column_Window(y)
	sys.exit(app.exec_())