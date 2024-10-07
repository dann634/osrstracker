from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget

from main import apiConnection


class ItemContainer(QWidget):
    def __init__(self, item_name):
        super().__init__()

        self.hbox = QHBoxLayout()

        item_id = apiConnection.get_item_id(item_name)
        img = apiConnection.get_item_icon(item_id)

        img = img.convert("RGBA")
        data = img.tobytes("raw", "RGBA")
        qim = QImage(data, img.size[0], img.size[1], QImage.Format_RGBA8888)
        pixmap = QPixmap.fromImage(qim)

        self.img_label = QLabel()
        self.img_label.setPixmap(pixmap)

        self.item_label = QLabel(item_name)

        self.hbox.addWidget(self.img_label)
        self.hbox.addWidget(self.item_label)
        self.setProperty("class", "hot_item")
        self.setLayout(self.hbox)



