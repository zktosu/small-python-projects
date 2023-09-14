from PySide6.QtWidgets import QPushButton,QLabel,QApplication
from PySide6.QtCore import Slot

@Slot()
def hey():
    print("Say Hey!")
app = QApplication()
button = QPushButton("<h1>Say Hi</h1>")
button.clicked.connect(hey)
button.show()
app.exec()
