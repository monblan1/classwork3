import sys
import random
from UI import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor


class Circless(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.draw = False
        self.show()

    def paintEvent(self, event):
        if not self.draw:
            return
        qp = QPainter()
        qp.begin(self)
        self.drawCircles(qp)
        qp.end()

    def run(self):
        self.draw = True
        self.update()

    def drawCircles(self, qp):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        x = random.randint(1, self.width())
        y = random.randint(50, self.height())
        w = random.randint(10, 100)
        qp.drawEllipse(x, y, w, w)


app = QApplication(sys.argv)
ex = Circless()
sys.exit(app.exec_())
