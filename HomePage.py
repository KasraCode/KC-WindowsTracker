from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
 

class HPWindow(QMainWindow):
    """Created by Kasra Hosseini
    Github : https://github.com/KasraCode
    gmail : kasracodec@gmail.com
    Class to showing home page
       Button names : 
                Windows Tracker -> btn_tracker
                CPU Analyze -> btn_cpu
                Hard Disk Tracker -> btn_hardDisk
                System Info -> btn_sysInfo
                Settings -> btn_settings
                About Us -> btn_aboutUs
        Labels :
                "Home Page - Select" -> lbl_homeTitle
    """
    def __init__(self):
        super(HPWindow,self).__init__()
        loadUi("UiFiles/MainWindow.ui",self)
        

