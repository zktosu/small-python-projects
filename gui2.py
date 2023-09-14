from PySide6.QtWidgets import QApplication, QPushButton,QMainWindow

class Butoner(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Buton Sample")
		self.button = QPushButton("Click")
		self.setCentralWidget(self.button)

if __name__ == "__main__":
	app = QApplication()
	root = Butoner()
	root.show()
	app.exec()
