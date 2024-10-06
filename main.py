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
        self.navigation_panel = QVBoxLayout()

        self.navigation_container = QWidget()
        self.navigation_container.setObjectName("navigation_panel")
        self.navigation_container.setLayout(self.navigation_panel)

        self.main_grid.addWidget(self.navigation_container, 0, 0)

        home_container = QWidget()
        home_container.setLayout(home.Home())
        home_container.setObjectName("home_vbox")
        self.main_grid.addWidget(home_container, 0, 1)

        self.initNavPane()



    def initNavPane(self):
        home_button = QPushButton()
        home_button.setIcon(QIcon("resources/images/house.png"))

        search_button = QPushButton()
        search_button.setIcon(QIcon("resources/images/search.png"))

        items_button = QPushButton()
        items_button.setIcon(QIcon("resources/images/sword.png"))

        self.navigation_panel.addWidget(home_button)
        self.navigation_panel.addWidget(search_button)
        self.navigation_panel.addWidget(items_button)
        self.navigation_panel.addStretch() #Pushes items to top



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()