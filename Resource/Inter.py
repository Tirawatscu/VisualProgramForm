import sys
import os

from PyQt5.QtWidgets import (QPushButton, QWidget,
                             QLineEdit, QApplication)


class Line(QLineEdit):

    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            path = str(url.toLocalFile())
            if os.path.isfile(path):
                self.setText(path)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        edit = Line('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = QPushButton("Button", self)
        button.move(190, 65)

        self.setWindowTitle('Simple drag and drop')
        self.setGeometry(300, 300, 300, 150)


def main():

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()
