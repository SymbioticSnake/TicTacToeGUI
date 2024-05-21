from PyQt6.QtWidgets import QApplication
from Game import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())