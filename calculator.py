#   Calculator process
#   Calculator windows

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt  # for QlineEdit edit alignment
from PyQt5.QtGui import QFont, QKeySequence
from PyQt5.QtWidgets import QShortcut

buttons = {"MC": (1, 0, 1, 1),
           "MR": (1, 1, 1, 1),
           "MS": (1, 2, 1, 1),
           "M+": (1, 3, 1, 1),
           "M-": (1, 4, 1, 1),
           "DEL": (2, 0, 1, 1),
           "CE": (2, 1, 1, 1),
           "C": (2, 2, 1, 1),
           "+|-": (2, 3, 1, 1),
           "SQRT": (2, 4, 1, 1),
           "7": (3, 0, 1, 1),
           "8": (3, 1, 1, 1),
           "9": (3, 2, 1, 1),
           "/": (3, 3, 1, 1),
           "%": (3, 4, 1, 1),
           "4": (4, 0, 1, 1),
           "5": (4, 1, 1, 1),
           "6": (4, 2, 1, 1),
           "*": (4, 3, 1, 1),
           "1/x": (4, 4, 1, 1),
           "1": (5, 0, 1, 1),
           "2": (5, 1, 1, 1),
           "3": (5, 2, 1, 1),
           "-": (5, 3, 1, 1),
           "=": (5, 4, 2, 1),
           "0": (6, 0, 1, 2),
           ".": (6, 2, 1, 1),
           "+": (6, 3, 1, 1)
           }


class Windows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CalcApp")

        self.le_display = QtWidgets.QLineEdit("0")
        self.le_display.setReadOnly(True)
        self.le_display.setTextMargins(5, 10, 10, 5)
        self.le_display.setAlignment(Qt.AlignRight)
        self.le_display.setFont(QFont('Arial', 22))

        self.b_buttons = {}

        layout_main = QtWidgets.QGridLayout(self)
        layout_main.addWidget(self.le_display, 0, 0, 1, 5)
        for button_name, button_position in buttons.items():
            button = QtWidgets.QPushButton(button_name)

            layout_main.addWidget(button, *button_position)  # * is for unpack list
            self.b_buttons[button_name] = button  # save button

            if button_name not in ["MC", "MR", "MS", "M+", "M-", "DEL", "CE", "C", "="]:
                button.clicked.connect(self.number_operation_pressed)

        self.b_buttons["C"].clicked.connect(self.clear_display)
        self.b_buttons["="].clicked.connect(self.result)
        self.keybord_connect()

    def result(self):
        try:
            self.le_display.setText(str(eval(self.le_display.text().replace("X", "*"))))
        except SyntaxError:
            return

    def number_operation_pressed(self):
        if self.le_display.text() == "0":
            self.le_display.clear()
        self.le_display.setText(self.le_display.text() + self.sender().text())

    def clear_display(self):
        self.le_display.setText("0")

    def keybord_connect(self):
        # QShortcut prend en parametre la touche a connecter, la fenetre a agir et la methode a appeler
        # Puisqu'il est fastidieux de connaitre le nom logique de chaque touche...
        # QKeySequence retourne le nom logique en utilisant la lettre correspondante sur le clavier
        # button.clicked.emit permet de simuler un clic sur la touche
        for button_text, button in self.b_buttons.items():
            QShortcut(QKeySequence(button_text), self, button.clicked.emit)
        
