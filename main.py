import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        #where window shows on run
        window_x = 200
        window_y = 200

        #initial width and height of window
        initial_width = 1200
        initial_height = 600

        self.setGeometry(window_x, window_y, initial_width, initial_height)

        #set window icon
        self.setWindowIcon(QIcon("resources/images/icon.png"))

        #set window title
        self.setWindowTitle("OSRS Tracker")



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()