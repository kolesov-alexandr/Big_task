import os
import sys
import Full_search

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt
from io import BytesIO
from PIL import Image


SCREEN_SIZE = [600, 450]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.map_file = "map.png"
        self.ll, self.spn = Full_search.search("Мурманск Софьи Перовской 5")
        self.initUI()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageDown:
            lon, lat = map(float, self.spn.split(","))
            lon -= 0.001
            lat -= 0.001
            self.spn = f"{lon},{lat}"
        if event.key() == Qt.Key_PageUp:
            lon, lat = map(float, self.spn.split(","))
            lon += 0.001
            lat += 0.001
            self.spn = f"{lon},{lat}"
        if event.key() == Qt.Key_Up:
            lon, lat = map(float, self.ll.split(","))
            lat += 0.001
            self.ll = f"{lon},{lat}"
        if event.key() == Qt.Key_Right:
            lon, lat = map(float, self.ll.split(","))
            lon += 0.001
            self.ll = f"{lon},{lat}"
        if event.key() == Qt.Key_Down:
            lon, lat = map(float, self.ll.split(","))
            lat -= 0.001
            self.ll = f"{lon},{lat}"
        if event.key() == Qt.Key_Left:
            lon, lat = map(float, self.ll.split(","))
            lon -= 0.001
            self.ll = f"{lon},{lat}"
        Full_search.make_map(Full_search.set_map_params(self.ll, self.spn))
        self.pixmap = QPixmap(self.map_file)
        self.image.setPixmap(self.pixmap)


    def initUI(self):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle("Отображение карты")
        self.pixmap = QPixmap(self.map_file)
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
