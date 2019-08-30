import sys
import random

from PySide2.QtCore import Slot, Qt, QPoint
from PySide2.QtGui import QPainter, QPen, QBrush
from PySide2.QtWidgets import QApplication, QDialog

from pyside2app.ui_window import Ui_MyAppWindow


class MyAppWindow(QDialog):
    def __init__(self):
        super(MyAppWindow, self).__init__()
        self.ui = Ui_MyAppWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.Window)

        self.points = []

    @Slot()
    def on_btnHello_clicked(self):
        name = self.ui.edtName.text()
        self.ui.txtMessages.append('hello, <b>{}</b>! ☃'.format(name))

    def generate_point(self):
        colors = [Qt.red, Qt.blue, Qt.yellow, Qt.green]
        min_y = self.ui.txtMessages.height() + 15
        x = random.randint(10, self.width() - 10)
        y = random.randint(min_y, min_y + 200)
        return {'x': x, 'y': y, 'color': random.choice(colors)}

    @Slot()
    def on_btnDraw_clicked(self):
        for x in range(0, random.randint(1, 4)):
            self.points.append(self.generate_point())
        self.update()

    def paintEvent(self, ev):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)
        for p in self.points:
            pen = QPen(p['color'], 5)
            brush = QBrush(p['color'])
            qp.setPen(pen)
            qp.setBrush(brush)
            qp.drawEllipse(QPoint(p['x'], p['y']), 5, 5)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyAppWindow()
    window.show()

    sys.exit(app.exec_())
