import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget

import api_connection
from pages import home, items

apiConnection = api_connection.APIConnection()
main_grid = QGridLayout()


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
        self.center_widget.setLayout(main_grid)

        main_grid.setSpacing(0) #Removes whitespace
        main_grid.setContentsMargins(0, 0, 0, 0)

        #Init Left Navigation
        main_grid.addWidget(home.NavigationPanel(self.swapScene), 0, 0)

        #Home Scene
        self.home_scene = home.Home()
        self.item_scene = items.Items()
        main_grid.addWidget(self.home_scene, 0, 1)
        main_grid.addWidget(self.item_scene, 0, 1)

        self.item_scene.hide()



    def swapScene(self, scene):
        self.home_scene.hide()
        self.item_scene.hide()
        match scene:
            case "Home":
                self.home_scene.show()
            case "Items":
                self.item_scene.show()
            case "Gold":
                pass



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()