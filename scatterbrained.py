import sys

from PyQt5 import QtWidgets

from src import dashboard as db

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = db.Dashboard()
    window.show()
    app.exec_()
