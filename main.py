# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QGridLayout, QVBoxLayout, QPushButton, QLabel
from random import choice
from time import sleep

class Game(QMainWindow):
    def __init__(self):
        super().__init__()

        # 

        # Game Window
        self.setWindowTitle("Tic Tac Toe")
        self.setFixedSize(QSize(600, 300))

        central = QWidget()
        self.setCentralWidget(central)

        self.buttons = [[QPushButton(parent=self, text="") for _ in range(3)] for _ in range(3)]
        print(self.buttons)

        grid_layout = QGridLayout()
        for i in range(3):
            for j in range(3):
                    self.buttons[i][j].setFixedSize(190, 80)
                    self.buttons[i][j].clicked.connect(self.buttonClicked)
                    grid_layout.addWidget(self.buttons[i][j], i, j)
        self.label = QLabel("Choose a button to place an X.", alignment=Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(grid_layout)

        central.setLayout(layout)

    def buttonClicked(self):
        button = self.sender()
        button.setText("X")
        button.setEnabled(False)
        
        # button2 = choice(choice(self.buttons))
        # while button2.text == "X" or button2.text == "O":
        #     button2 = choice(choice(self.buttons))
        # button2.setText("O")
        # button.setEnabled(False)

    # def checkWin(self):
    

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Game()
    window.show()
    
    window.buttons[1][2].animateClick()

    sys.exit(app.exec())
