import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Choice(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('choice.ui', self)

        self.pushButton.clicked.connect(self.guitar)
        self.pushButton_2.clicked.connect(self.ukulele)
        self.pushButton_3.clicked.connect(self.violin)
        self.pushButton_4.clicked.connect(self.bas)
        self.pushButton_5.clicked.connect(self.cello)
        self.pushButton_6.clicked.connect(self.balalaika)

    def guitar(self):
        from main2 import Project
        if __name__ == '__main__':
            app1 = QApplication(sys.argv)
            ex1 = Project()
            ex1.show()
            sys.exit(app1.exec())

    def ukulele(self):
        pass

    def violin(self):
        pass

    def bas(self):
        pass

    def cello(self):
        pass

    def balalaika(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Choice()
    ex.show()
    sys.exit(app.exec())
