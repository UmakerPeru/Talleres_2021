import sys
from PyQt5.QtWidgets import QWidget , QApplication , QLabel, QPushButton

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.title = "Ventana"
		self.left = 200
		self.top = 200
		self.width = 600
		self.height = 300
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left,self.top,self.width,self.height)
		#Crear Label
		self.label1 = QLabel("Apagado",self)
		self.label1.move(200,50)
		#Crear boton1
		button1 = QPushButton("Encender",self)
		button1.move(200,100)
		button1.clicked.connect(self.encendido)
		#Crear boton2
		button2 = QPushButton("Apagar",self)
		button2.move(200,140)
		button2.clicked.connect(self.apagado)
		self.show()
	def encendido(self):
		self.label1.setText("Encendido")
		self.label1.adjustSize()
		print("Se encendio")
	def apagado(self):
		self.label1.setText("Apagado")
		self.label1.adjustSize()
		print("se apago")
if __name__ == "__main__":
	app = QApplication([])
	ex = App()
	sys.exit(app.exec_())
