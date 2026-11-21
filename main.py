import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QBrush, QColor
import random
from PyQt6 import uic

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("ui.ui", self)
        self.do_paint = False
        self.pushbtn.clicked.connect(self.draw_yellow_ellipse)

    def draw_yellow_ellipse(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter(self)
            qp.setBrush(QBrush(QColor("yellow")))
            for i in range(random.randint(1, 15)):
                r = random.randint(10, 100) // 2
                x = random.randint(100, 700)
                y = random.randint(100, 500)
                qp.drawEllipse(x, y, r, r)
            self.do_paint = False

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())