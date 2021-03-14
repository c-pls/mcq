import sys
from functools import partial
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit



# Create the UI of the app
class MCQ_UI(QMainWindow):
    def __init__(self):
        # Set some properties
        super().__init__()
        self.setWindowTitle('MCQ')
        self.setFixedSize(1080,720)

        # Set the central widget and general layout
        self.general_Layout = QVBoxLayout()

        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.general_Layout)

        # Create the question and answers's displays
        self._Question_display()
        self._Answer_display()
     

    def _Question_display(self):
        """Create the question display"""
        self.display = QLabel()

        # set the display properties
        self.display.setFixedHeight(200)
        self.display.setAlignment(Qt.AlignCenter)


        self.general_Layout.addWidget(self.display)


    def _Answer_display(self):
       """Create the form of answer 4"""
       self.answers = {}
       answers_Layout = QGridLayout()
       # store the position in the GridLayout
       answers = {
           'a': (0, 0),
           'b': (0, 1),
           'c': (1, 0),
           'd': (1, 1)
       }

       # create the button and add it into the grid
       for answersText, pos in answers.items():
            self.answers[answersText] = QPushButton('&Helooooo')
            self.answers[answersText].setFixedSize(300,100)
            answers_Layout.addWidget(self.answers[answersText], pos[0], pos[1])
       self.general_Layout.addLayout(answers_Layout)


    def setDisplayText(self, text):
        """Set display text"""
        self.display.setText(text)
        self.display.setFocus()

