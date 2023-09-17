from PySide6.QtWidgets import QApplication,QLineEdit,QPushButton,QVBoxLayout,QDialog

class Form(QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.edit = QLineEdit("World!")
		self.button = QPushButton("Greet please")
		layout = QVBoxLayout()
		layout.addWidget(self.edit)
		layout.addWidget(self.button)
		self.setLayout(layout)
		self.button.clicked.connect(self.greetings)
	def greetings(self):
		self.edit.setText("Hello %s"%self.edit.text())

if __name__ == "__main__":
	app = QApplication()
	form = Form()
	form.show()
	app.exec()
