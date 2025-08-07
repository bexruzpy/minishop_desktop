from frames.activate_frame import ActivateFrame
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.path = "designs/main.ui"
        loadUi(self.path, self)
    def closeEvent(self, event):
        event.ignore()
        event.accept()


app = QApplication(sys.argv)
main_frame = MainWindow()
main_frame.showFullScreen()
sys.exit(app.exec_())
