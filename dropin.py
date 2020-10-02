from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtGui import QPixmap


class DropIn(QtWidgets.QLabel):

    def __init__(self, parent):
        super().__init__(parent)
        self.path = ''
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            self.path = str(url.toLocalFile())
            if os.path.isfile(self.path):
                # self.setText(path)
                pixmap = QPixmap(self.path)
                size = QtCore.QSize(300, 200)
                pixmap = pixmap.scaled(size)
                self.setPixmap(pixmap)

    def topath(self):
        return self.path
