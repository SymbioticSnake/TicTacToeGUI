from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QWidget, QMainWindow, QGridLayout, QVBoxLayout, QPushButton, QLabel, QMessageBox
from random import choice
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Game Information
        self.turns = 0
        self.winner = ("No one", False)

        ## Game GUI Creation ##
        self.setWindowTitle("Tito's Tic Tac Toe")
        self.setFixedSize(QSize(600, 300))

        # Creating central/main window
        central = QWidget()
        self.setCentralWidget(central)

        # Creating button grid for game
        self.buttons = [[QPushButton(parent=self, text=" ") for _ in range(3)] for _ in range(3)]
        grid_layout = QGridLayout()
        for i in range(3):
            for j in range(3):
                    self.buttons[i][j].setFixedSize(190, 80)
                    self.buttons[i][j].clicked.connect(self.buttonClicked)

                    font = self.buttons[i][j].font()
                    font.setPointSize(30)
                    self.buttons[i][j].setFont(font)

                    grid_layout.addWidget(self.buttons[i][j], i, j)
        self.label = QLabel("Have fun! X is first; O is second.", alignment=Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(grid_layout)

        central.setLayout(layout)

    def __resetBoard(self):
        self.turns = 0
        self.winner = "No one"
        self.label.setText("Have fun! X is Player 1; O is Player 2.")
    
        for row in self.buttons:
            for button in row:
                button.setText(" ")
                button.setEnabled(True)
    
    def __playAgain(self):
        choice = QMessageBox.question(self, "Thanks for playing!", "Would you like to play again?")
        if choice == QMessageBox.StandardButton.Yes:
            self.__resetBoard()
        else:
            sys.exit()
    
    def __gameEnd(self, winner):
        if winner == "You" or winner == "Computer":
            self.label.setText("Winner: "+winner)
            for row in self.buttons:
                for button in row: button.setEnabled(False)
            self.__playAgain()

        elif self.turns == 9:
            self.label.setText("It's A Draw!")
            self.__playAgain()

    def __checkWin(self):
        # print("     |     |     ")
        # print("  "+self.buttons[0][0].text()+"  |  "+self.buttons[0][1].text()+"  |  "+self.buttons[0][2].text()+"  ")
        # print("_____|_____|_____")
        # print("     |     |     ")
        # print("  "+self.buttons[1][0].text()+"  |  "+self.buttons[1][1].text()+"  |  "+self.buttons[1][2].text()+"  ")
        # print("_____|_____|_____")
        # print("     |     |     ")
        # print("  "+self.buttons[2][0].text()+"  |  "+self.buttons[2][1].text()+"  |  "+self.buttons[2][2].text()+"  ")
        # print("     |     |     \n")

        if self.buttons[0][0].text() != " " and self.buttons[0][0].text() == self.buttons[0][1].text() and self.buttons[0][1].text() == self.buttons[0][2].text():
            winner = "You" if self.buttons[0][0].text() == "X" else "Computer"
        elif self.buttons[1][0].text() != " " and self.buttons[1][0].text() == self.buttons[1][1].text() and self.buttons[1][1].text() == self.buttons[1][2].text():
            winner = "You" if self.buttons[1][0].text() == "X" else "Computer"
        elif self.buttons[2][0].text() != " " and self.buttons[2][0].text() == self.buttons[2][1].text() and self.buttons[2][1].text() == self.buttons[2][2].text():
            winner = "You" if self.buttons[2][0].text() == "X" else "Computer"
        elif self.buttons[0][0].text() != " " and self.buttons[0][0].text() == self.buttons[1][0].text() and self.buttons[1][0].text() == self.buttons[2][0].text():
            winner = "You" if self.buttons[0][0].text() == "X" else "Computer"
        elif self.buttons[0][1].text() != " " and self.buttons[0][1].text() == self.buttons[1][1].text() and self.buttons[1][1].text() == self.buttons[2][1].text():
            winner = "You" if self.buttons[0][1].text() == "X" else "Computer"
        elif self.buttons[0][2].text() != " " and self.buttons[0][2].text() == self.buttons[1][2].text() and self.buttons[1][2].text() == self.buttons[2][2].text():
            winner = "You" if self.buttons[0][2].text() == "X" else "Computer"
        elif self.buttons[0][0].text() != " " and self.buttons[0][0].text() == self.buttons[1][1].text() and self.buttons[1][1].text() == self.buttons[2][2].text():
            winner = "You" if self.buttons[0][0].text() == "X" else "Computer"
        elif self.buttons[0][2].text() != " " and self.buttons[0][2].text() == self.buttons[1][1].text() and self.buttons[1][1].text() == self.buttons[2][0].text():
            winner = "You" if self.buttons[0][2].text() == "X" else "Computer"
        else: return "None"
        return winner
    
    def buttonClicked(self):
        button = self.sender()
        button.setText("X")
        button.setEnabled(False)
        self.turns += 1

        self.winner = self.__checkWin()
        self.__gameEnd(self.winner)

        if self.winner == "None":
            computer_button = choice(choice(self.buttons))
            while computer_button.text() != " ":
                computer_button = choice(choice(self.buttons))

            computer_button.setText("O")
            computer_button.setEnabled(False)
            self.turns += 1
            
            self.winner = self.__checkWin()
            self.__gameEnd(self.winner)
        
