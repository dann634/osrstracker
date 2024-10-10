from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QPainter
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget, QStyleOption, QStyle

from main import apiConnection
from pages.CustomQWidget import CustomQWidget


class ItemContainer(CustomQWidget):
    def __init__(self, item_name):
        super().__init__()

        self.hbox = QHBoxLayout()
        self.hbox.setSpacing(5)
        self.hbox.setAlignment(Qt.AlignLeft)

        #Gets Image
        item_id = apiConnection.get_item_id(item_name)
        img = apiConnection.get_item_icon(item_id)

        img = img.convert("RGBA")
        data = img.tobytes("raw", "RGBA")
        qim = QImage(data, img.size[0], img.size[1], QImage.Format_RGBA8888)
        pixmap = QPixmap.fromImage(qim)

        self.img_label = QLabel()
        self.img_label.setPixmap(pixmap)
        self.img_label.setObjectName("img")

        self.item_label = QLabel(item_name)
        self.item_label.setAlignment(Qt.AlignCenter)
        self.item_label.setObjectName("item_name")
        self.item_label.adjustSize()

        self.hbox.addWidget(self.img_label)
        self.hbox.addWidget(self.item_label)
        self.setLayout(self.hbox)

