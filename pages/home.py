from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton


class Home(QVBoxLayout):

    def __init__(self):
        super().__init__()
        
        # Init Home Page

        # self.setStyleSheet(open("resources/stylesheets/home.css").read())

        label = QLabel("OSRS Tracker")
        search_box = QLineEdit("Search")

        self.addWidget(label)
        self.addWidget(search_box)
        self.addStretch()


class NavigationPanel(QVBoxLayout):
    def __init__(self):
        super().__init__()
        home_button = QPushButton()
        home_button.setIcon(QIcon("resources/images/house.png"))

        search_button = QPushButton()
        search_button.setIcon(QIcon("resources/images/search.png"))

        items_button = QPushButton()
        items_button.setIcon(QIcon("resources/images/sword.png"))

        self.addWidget(home_button)
        self.addWidget(search_button)
        self.addWidget(items_button)
        self.addStretch()  # Pushes items to top