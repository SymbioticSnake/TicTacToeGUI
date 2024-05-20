# import sys

# from PySide6.QtCore import Qt
# from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.label = QLabel("Click in this window")
#         self.setCentralWidget(self.label)

#     def mouseMoveEvent(self, e):
#         self.label.setText("mouseMoveEvent")

#     def mousePressEvent(self, e):
#         self.label.setText("mousePressEvent")

#     def mouseReleaseEvent(self, e):
#         self.label.setText("mouseReleaseEvent")

#     def mouseDoubleClickEvent(self, e):
#         self.label.setText("mouseDoubleClickEvent")


# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec()


from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()