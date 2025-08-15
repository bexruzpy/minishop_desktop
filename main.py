from frames.activate_frame import ActivateFrame
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from crypto.check_license import verify_license
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.path = "designs/main.ui"
        loadUi(self.path, self)

    def chech_license(self):
        return verify_license()
    def closeEvent(self, event):
        event.ignore()
        event.accept()
    


app = QApplication(sys.argv)
main_frame = MainWindow()
if main_frame.chech_license():
    main_frame.showFullScreen()
else:
    main_frame.show()
sys.exit(app.exec_())
