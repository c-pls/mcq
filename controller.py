from ui_form import *

import json
from random import randint
import sys


TOPICS_LIST = ['commerce', 'technology' ]
class Controller:
    """Controller thing"""
    def __init__(self, view):
        self._view = view

        # connect to signals and slots
        self._build_Questions()
        self._build_Anwsers()
        self._connectSignals()

    def _build_Questions(self):
        questions = load_question('data/commerce.json')
        self._view.setDisplayText(questions['1']['question'])
        print(questions['1']['question'])


    def _build_Anwsers(self):
        questions = load_question('data/commerce.json')
        list_answer = ['a','b','c','d']
        i = 0
        for each_answer in self._view.answers.items():

            each_answer[1].setText(questions['1'][list_answer[i]])
            i += 1



    def _connectSignals(self):
        pass


# Load question
def load_question(filename):
    questions = None
    with open(filename, 'r') as read_file:
        questions = json.load(read_file)
    return questions


def main():
    app = QApplication(sys.argv)
    view = MCQ_UI()
    view.show()

    Controller(view=view)
    sys.exit(app.exec_())





if __name__ == '__main__':
    main()










