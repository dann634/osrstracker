from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
from pages import items


class Home(QVBoxLayout):

    def __init__(self):
        super().__init__()
        
        # Init Home Page

        self.title_label = QLabel("OSRS Tracker")
        self.title_label.setObjectName("title")
        self.search_box = QLineEdit("Search")
        self.hot_label = QLabel("🔥Hot Items🔥")
        self.hot_label.setObjectName("hot_title")

        self.hot_items_grid = QGridLayout()
        hot_items = ["Bronze sword", "Bronze pickaxe", "Steel dagger", "Longbow"]
        self.hot_item_containers = []
        for item in hot_items:
            self.hot_item_containers.append(items.ItemContainer(item))

        self.hot_items_grid.addWidget(self.hot_item_containers[0], 0, 0)
        self.hot_items_grid.addWidget(self.hot_item_containers[1], 1, 0)
        self.hot_items_grid.addWidget(self.hot_item_containers[2], 0, 1)
        self.hot_items_grid.addWidget(self.hot_item_containers[3], 1, 1)


        self.addWidget(self.title_label)
        self.addWidget(self.search_box)
        self.addWidget(self.hot_label)
        self.addLayout(self.hot_items_grid)
        self.addStretch()

    def get_hot_items(self):
        return self.hot_item_containers



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