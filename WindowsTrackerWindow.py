from PyQt5.QtWidgets import QMainWindow, QPushButton, QPlainTextEdit, QLineEdit, QLabel, QCheckBox, QToolButton
from PyQt5.uic import loadUi
 
class WTWinodw(QMainWindow):
    """Created by Kasra Hosseini
    Github : https://github.com/KasraCode
    gmail : kasracodec@gmail.com
    Class to showing Windows Tracker Window
       Button names : 
                Path dialog(...) -> btn_path
                Start Logging -> btn_start
                Stop Logging -> btn_stop
                Home Page -> btn_back
                Submit -> btn_submit
                Save -> btn_save
                Clear -> btn_Clear
                Open config.json -> btn_json
        Plain Text Edits :
                Logging PTE -> ptxt_log
        Line Edits : 
                Path box -> txt_path
                HintBox -> txt_hintEx
                Custom Filter -> txt_filter
        Labels :
                "File Filters" -> lbl_filter
                "Logging" -> lbl_log
                "PATH" -> lbl_path
        Check Boxes :
                "Sys Files" -> chb_sysfile
                "Hidden Files" -> chb_hidden
                "Read only Files" -> chb_readO
                "Archive Files" -> chb_archive
    """
    def __init__(self,parent=None):
        super(WTWinodw,self).__init__(parent=parent)
        # Loading WinTracker.ui file to design the window
        loadUi("UiFiles/WinTracker.ui",self)
        self.parentWindow=parent
        # Finding components in ui file (Sometimes it's important)
        self.btn_path=self.findChild(QToolButton,"btn_path")
        
        self.btn_start=self.findChild(QPushButton,"btn_start")
        self.btn_stop=self.findChild(QPushButton,"btn_stop")
        self.btn_back=self.findChild(QPushButton,"btn_back")
        self.btn_submit=self.findChild(QPushButton,"btn_submit")
        self.btn_save=self.findChild(QPushButton,"btn_save")
        self.btn_Clear=self.findChild(QPushButton,"btn_Clear")
        self.btn_json=self.findChild(QPushButton,"btn_json")
        
        self.ptxt_log=self.findChild(QPlainTextEdit,"ptxt_log")

        self.txt_path=self.findChild(QLineEdit,"txt_path")
        self.txt_hintEx=self.findChild(QLineEdit,"txt_hintEx")
        self.txt_filter=self.findChild(QLineEdit,"txt_filter")

        self.lbl_filter=self.findChild(QLabel,"lbl_filter")
        self.lbl_log=self.findChild(QLabel,"lbl_log")
        self.lbl_path=self.findChild(QLabel,"lbl_path")

        self.chb_sysfile=self.findChild(QCheckBox,"chb_sysfile")
        self.chb_hidden=self.findChild(QCheckBox,"chb_hidden")
        self.chb_readO=self.findChild(QCheckBox,"chb_readO")
        self.chb_archive=self.findChild(QCheckBox,"chb_archive")

        self.btn_back.clicked.connect(self.btnBackClicked)

    def btnBackClicked(self):
        self.hide()
        self.parentWindow.show()