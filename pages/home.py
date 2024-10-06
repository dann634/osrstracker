from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QLineEdit


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
