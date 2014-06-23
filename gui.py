import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gui Test")




if __name__ == "__main__":

    #instantiates a QApplication
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    app.exec_()
