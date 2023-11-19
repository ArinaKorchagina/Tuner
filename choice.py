import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from guitar import Guitar
from ukulele import Ukulele
from violin import Violin
from cello import Cello
from bas import Bas
from balalaika import Balalaika


class Choice(QMainWindow):
    def __init__(self):
        super().__init__()
        self.balalaika = None
        self.cello = None
        self.bas = None
        self.violin = None
        self.ukulele = None
        self.guitar = None
        uic.loadUi('choice.ui', self)
        # Подключаем кнопки
        self.pushButton.clicked.connect(self.show_guitar)
        self.pushButton_2.clicked.connect(self.show_ukulele)
        self.pushButton_3.clicked.connect(self.show_violin)
        self.pushButton_4.clicked.connect(self.show_bas)
        self.pushButton_5.clicked.connect(self.show_cello)
        self.pushButton_6.clicked.connect(self.show_balalaika)

    def show_guitar(self):
        self.guitar = Guitar()
        self.guitar.Exit.clicked.connect(self.close_guitar)
        self.guitar.show()  # вывод нового окна
        self.close()  # удаление старого

    def close_guitar(self):
        self.show()
        self.guitar.close()

    def show_ukulele(self):
        self.ukulele = Ukulele()
        self.ukulele.Exit.clicked.connect(self.close_ukulele)
        self.ukulele.show()
        self.close()

    def close_ukulele(self):
        self.show()
        self.ukulele.close()

    def show_violin(self):
        self.violin = Violin()
        self.violin.Exit.clicked.connect(self.close_violin)
        self.violin.show()
        self.close()

    def close_violin(self):
        self.show()
        self.violin.close()

    def show_bas(self):
        self.bas = Bas()
        self.bas.Exit.clicked.connect(self.close_bas)
        self.bas.show()
        self.close()

    def close_bas(self):
        self.show()
        self.bas.close()

    def show_cello(self):
        self.cello = Cello()
        self.cello.Exit.clicked.connect(self.close_cello)
        self.cello.show()
        self.close()

    def close_cello(self):
        self.show()
        self.cello.close()

    def show_balalaika(self):
        self.balalaika = Balalaika()
        self.balalaika.Exit.clicked.connect(self.close_balalaika)
        self.balalaika.show()
        self.close()

    def close_balalaika(self):
        self.show()
        self.balalaika.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Choice()
    ex.show()
    sys.exit(app.exec())
