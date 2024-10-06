import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QVBoxLayout, QWidget, QLabel, QPushButton, \
    QLineEdit

from pages import home, search


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

        #Add External CSS
        self.setStyleSheet(open("resources/stylesheets/home.css").read())

        #Set Central Widget
        self.center_widget = QWidget()
        self.setCentralWidget(self.center_widget)

        #Init Main Grid Layout Manager
        self.main_grid = QGridLayout()
        self.center_widget.setLayout(self.main_grid)

        self.main_grid.setSpacing(0) #Removes whitespace
        self.main_grid.setContentsMargins(0, 0, 0, 0)

        #Init Left Navigation
        navigation_panel = home.NavigationPanel()

        navigation_container = QWidget()
        navigation_container.setObjectName("navigation_panel")
        navigation_container.setLayout(navigation_panel)

        self.main_grid.addWidget(navigation_container, 0, 0)

        #Home Scene
        home_container = QWidget()
        home_container.setLayout(home.Home())
        home_container.setObjectName("home_vbox")
        self.main_grid.addWidget(home_container, 0, 1)




def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()