import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gui Test")
        self.create_initial_layout()

    def create_initial_layout(self):

        #create widgets
        self.textbox = QLineEdit()
        self.button = QPushButton("Submit")
        self.label = QLabel()
        
        #create layout

        self.layout = QVBoxLayout()

        #add widgets to the layout

        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)

        #set the central widget

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        #button connection
        self.button.clicked.connect(self.display_text)
        self.textbox.returnPressed.connect(self.display_text)

    def display_text(self):
        name = self.textbox.text()
        self.label.setText("Hello {0}".format(name))



if __name__ == "__main__":

    #instantiates a QApplication
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    app.exec_()
