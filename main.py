from PyQt5 import QtWidgets
import calculator

app = QtWidgets.QApplication([])
win = calculator.Windows()
win.show()
app.exec()
