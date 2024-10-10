from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
from pages import items
from pages.CustomQWidget import CustomQWidget


class Home(CustomQWidget):

    def __init__(self):
        super().__init__()
        
        # Init Home Page

        self.vbox = QVBoxLayout()
        self.setObjectName("home_vbox")

        self.title_label = QLabel("OSRS Tracker")
        self.title_label.setObjectName("title")

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search")

        self.hot_label = QLabel("🔥Hot Items🔥")
        self.hot_label.setObjectName("hot_title")

        self.hot_items_grid = QGridLayout()
        self.hot_items_grid.setHorizontalSpacing(15)
        self.hot_items_grid.setAlignment(Qt.AlignCenter)

        hot_items = ["Bronze sword", "Bronze pickaxe", "Steel dagger", "Longbow"]
        self.hot_item_containers = []
        for item in hot_items:
            item_container = items.ItemContainer(item)
            item_container.setObjectName("hot_container")
            self.hot_item_containers.append(item_container)

        self.hot_items_grid.addWidget(self.hot_item_containers[0], 0, 0)
        self.hot_items_grid.addWidget(self.hot_item_containers[1], 1, 0)
        self.hot_items_grid.addWidget(self.hot_item_containers[2], 0, 1)
        self.hot_items_grid.addWidget(self.hot_item_containers[3], 1, 1)

        self.vbox.addWidget(self.title_label)
        self.vbox.addWidget(self.search_box)
        self.vbox.addWidget(self.hot_label)
        self.vbox.addLayout(self.hot_items_grid)
        self.vbox.addStretch()

        self.setLayout(self.vbox)


    def get_hot_items(self):
        return self.hot_item_containers



class NavigationPanel(CustomQWidget):
    def __init__(self):
        super().__init__()

        self.vbox = QVBoxLayout()
        self.setObjectName("navigation_panel")

        home_button = QPushButton()
        home_button.setIcon(QIcon("resources/images/house.png"))

        search_button = QPushButton()
        search_button.setIcon(QIcon("resources/images/sword.png"))

        items_button = QPushButton()
        items_button.setIcon(QIcon("resources/images/ingots.png"))

        self.vbox.addWidget(home_button)
        self.vbox.addWidget(search_button)
        self.vbox.addWidget(items_button)
        self.vbox.addStretch()  # Pushes items to top
        self.setLayout(self.vbox)