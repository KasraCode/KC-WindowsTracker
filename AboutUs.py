from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

class AboutUsWindow(QMainWindow):
    def __init__(self,parent):
        super(AboutUsWindow,self).__init__(parent=parent)
        loadUi("UiFiles/AboutUs.ui",self)
        self.parentWindow=parent
        self.btn_ok.clicked.connect(self.btnOkClicked)

    def btnOkClicked(self):
        self.hide()
        self.parentWindow.show()