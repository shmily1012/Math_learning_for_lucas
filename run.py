import sys
import time
from os import path

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIntValidator
from PyQt5.Qt import Qt
from PyQt5.QtCore import QTimer, QDateTime
from main_ui import Ui_MainWindow
from Game import Game
from ErrorBook import ErrorBook


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # self.connectSignalsSlots()
        self.initConnections()
        self.game = Game()
        self.errorbook = ErrorBook()
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.time_left = self.game.single_question_duration
        self.lcdNumber.display(str(self.time_left))
        # conditions
        self.onlyInt = QIntValidator()
        self.lineEdit.setValidator(self.onlyInt)
        self.confirmButton.setEnabled(False)

    def showTime(self):
        self.time_left = int(self.game.single_question_duration -
                             (time.time()-self.start_time))
        self.lcdNumber.display(str(self.time_left))
        if self.time_left <= 0:
            self.clickConfirmButton()

    def initConnections(self):
        self.pushButton_3.clicked.connect(self.clickStartButton)
        self.confirmButton.clicked.connect(self.clickConfirmButton)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter:
            print('ENter')
            self.clickConfirmButton()

    def NextQuestion(self):
        self.game.provideQuestions()
        self.A_label.setText('%d' % self.game.value1)
        if self.game.sign == 'Add':
            self.sign_label.setText('+')
        elif self.game.sign == 'Subtract':
            self.sign_label.setText('-')
        elif self.game.sign == 'Multiply':
            self.sign_label.setText('x')
        elif self.game.sign == 'Divide':
            self.sign_label.setText('/')
        self.B_label.setText('%d' % self.game.value2)
        self.start_time = time.time()
        self.timer.start(1000)

    def clickStartButton(self):
        # self.statusBar.showMessage('click start')
        print('click start')
        self.NextQuestion()
        self.UsernameBox.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.confirmButton.setEnabled(True)

    def clickConfirmButton(self):
        if self.game.is_done:
            self.confirmButton.setEnabled(False)
            self.lineEdit.setEnabled(False)
            self.timer.stop()
            self.pushButton_3.setEnabled(True)
        self.game.number_answer += 1
        try:
            current_result = int(self.lineEdit.text(), 10)
        except ValueError:
            current_result = 0
        status, price = self.game.check(current_result, self.time_left)
        if status:
            self.Display_Label.setText("Correct +%d" % price)
        else:
            self.Display_Label.setText("WRONG! -%d" % price)

        self.label_2.setText('Rate: {}%'.format(
            round(self.game.number_pass/self.game.number_answer*100, 2)))
        self.label.setText('Score: {}'.format(self.game.score))
        self.lineEdit.setFocus()
        self.lineEdit.setText('')
        self.NextQuestion()

    def __del__(self):
        sys.exit(app.exec())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
