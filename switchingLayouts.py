import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello Program")
        self.resize(300,150)

        self.stacked_layout = QStackedLayout()

        #create each layout - call methods
        
        self.first_layout()
        self.second_layout()


        #create final widget
        
        self.widget = QWidget()

        self.widget.setLayout(self.stacked_layout)

        #set the central widget

        self.setCentralWidget(self.widget)

    def switch_layout(self):
        if self.stacked_layout.currentIndex() == 0:
            
            self.stacked_layout.setCurrentIndex(1)

            
            self.greetingLabel.setText("Hello, {0}".format(self.nameLineEdit.text()))
            
        elif self.stacked_layout.currentIndex() == 1:
            
            self.stacked_layout.setCurrentIndex(0)

            
            self.nameLineEdit.clear()

    def first_layout(self):
        
        self.nameLineEdit = QLineEdit()
        self.button = QPushButton("Submit")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.nameLineEdit)
        self.layout.addWidget(self.button)

        #new widget

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.layout)

        #add the widget to the stacked layout

        self.stacked_layout.addWidget(self.mainWidget)

        #connect the button to the method for handling button press

        self.button.clicked.connect(self.switch_layout)
        self.nameLineEdit.returnPressed.connect(self.switch_layout)
        
        

    def second_layout(self):

        self.greetingLabel = QLabel()
        self.backButton = QPushButton("Back")

        #newLayout

        self.newLayout = QVBoxLayout()

        self.newLayout.addWidget(self.greetingLabel)
        self.newLayout.addWidget(self.backButton)

        #new Widget

        self.newWidget = QWidget()
        self.newWidget.setLayout(self.newLayout)

        #add the widget to the stacked layout

        self.stacked_layout.addWidget(self.newWidget)

        #connect the back button to the back method

        self.backButton.clicked.connect(self.switch_layout)

        
if __name__ == "__main__":

    #instantiates a QApplication
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    app.exec_()
