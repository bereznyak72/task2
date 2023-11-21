import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Yellow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.button.clicked.connect(self.add_circle)
        self.circles = []
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()

    def draw_circles(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for x, y, r in self.circles:
            qp.drawEllipse(x, y, r, r)

    def add_circle(self):
        x = randint(100, 500)
        y = randint(100, 300)
        r = randint(20, 50)
        self.circles.append((x, y, r))
        self.do_paint = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Yellow()
    ex.show()
    sys.exit(app.exec())
