from PyQt5.QtWidgets import QLineEdit, QLabel, QVBoxLayout

from pages.CustomQWidget import CustomQWidget


class Items(CustomQWidget):

    def __init__(self):
        super().__init__()

        self.vbox = QVBoxLayout()

        self.title = QLabel("Item Lookup")
        self.title.setObjectName("title")

        self.searchBar = QLineEdit()
        self.searchBar.setPlaceholderText("Search")
        self.searchBar.setObjectName("search_bar")

        self.vbox.addWidget(self.title)
        self.vbox.addWidget(self.searchBar)
        self.vbox.addStretch()

        self.setLayout(self.vbox)



    #adds first 20 items to screen
    def init_items(self):
        pass