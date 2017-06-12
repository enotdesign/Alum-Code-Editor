from PyQt4.QtGui import*
from PyQt4.QtGui import QDesktopServices
from PyQt4.QtCore import QUrl

class About_us(QDialog):
	def link(self,linkStr):
		QDesktopServices.openUrl(QUrl(linkStr))
	def __init__(self,parent=None):
		QDialog.__init__(self,parent)
		#CONFIG WINDOW
		self.resize(500,250)
		self.setWindowTitle("Alum Code Editor | About us")
		self.setMaximumSize(500,250)
		self.setMinimumSize(500,250)
		#IMAGE
		self.picture = QLabel(self)
		self.picture.setGeometry(10,90,480,160)
		self.picture.setPixmap(QPixmap("images/alum_logo.png"))
		self.picture.setStyleSheet("height:160px;")
		#QLABELS
		self.label = QLabel("<h1>Alum Code Editor</h1>",self)
		self.label2 = QLabel("<h4>A simple editor build in Python</h4>",self)
		self.labelgithub = QLabel("",self)
		self.labeldominio = QLabel("",self)
		self.labeldominio.hide()
		self.labelgithub.linkActivated.connect(self.link)
		self.labelgithub.setText("<h2><a href='https://github.com/procreativo/Alum-Code-Editor'>GITHUB</a></h2>")
		#self.labeldominio.setText("<h2><a href='#'>DOMINIO NO DISPONIBLE</a></h2>")
		self.label.move(140,10)
		self.labelgithub.move(200,80)
		#self.labeldominio.move(120,120)
		self.label2.move(150,50)
