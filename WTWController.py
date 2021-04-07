from WindowsTrackerWindow import WTWinodw
from LoggingCore import TrackingCore, LoggingTextBox
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import os, logging, threading, ConfigJson

# Customize the QMessageBox with inheritance.
class MsgBox(QMessageBox):
    def __init__(self):
        super(MsgBox,self).__init__()
        self.setIcon(QMessageBox.Critical)

    def empty(self,target):
        self.setWindowTitle(f"{target} is empty !")
        self.setText(f"Make sure that the {target} field is not empty .")
        self.show()
    
    def pathError(self):
        self.setWindowTitle("Path error")
        self.setText("The path does not exist !")
        self.show()
    
    def setMessage(self,title,text):
        self.setText(text)
        self.setWindowTitle(title)
        self.show()

# Main class
class WTW_Controller(WTWinodw):
    def __init__(self,parent=None):
        super(WTW_Controller,self).__init__(parent=parent)
        self.fileFilters=[]
        # Creating TrackingCore object (main logging core)
        self.logCore=TrackingCore()
        self.messageBox=MsgBox()
        # Connecting click event of buttons to their functions
        self.btn_start.clicked.connect(self.btnStartClicked)
        self.btn_stop.clicked.connect(self.btnStopClicked)
        self.btn_clear.clicked.connect(self.btnClearClicked)
        self.btn_path.clicked.connect(self.btnPathClicked)
        self.btn_submit.clicked.connect(self.btnSubmitClicked)
        self.btn_save.clicked.connect(self.btnSaveClicked)
        self.btn_json.clicked.connect(self.btnJsonClicked)
        
        # Connecting the log message to QPlainTextEdit
        self.handler=LoggingTextBox(self)
        logging.getLogger().addHandler(self.handler)
        self.handler.new_record.connect(self.ptxt_log.appendPlainText)

    def btnStartClicked(self):
        # Path validation :
        # If return value is 0: path filed is empty
        # 1: Path is correct and exists
        # 2: doesn't exist
        _pathValied=self.pathValidation(self.txt_path.text())
        # If observer has not started :
        if not self.logCore.observer.is_alive():
            if _pathValied == 0:
                self.messageBox.empty("PATH")

            elif _pathValied == 1:
                isfile=False
                self.logCore.setPath(self.txt_path.text())
                # If config.json file exists, sets the filter
                if os.path.isfile('config.json'):
                    isfile=True
                    data=ConfigJson.getJsonData()['filters']
                    data=','.join(data)
                    self.txt_filter.setText(data)
                    self.logCore.start(isfile,self.txt_path.text(),data)
                else:
                    self.logCore.start()

            else:
                self.messageBox.pathError()

        else:
            if _pathValied == 0 :
                self.messageBox.empty("PATH")

            elif _pathValied == 1:
                self.logCore.setPath(self.txt_path.text())

            else:
                self.messageBox.pathError()

    def btnStopClicked(self):
        self.logCore.observer.unschedule_all()
    
    def btnClearClicked(self):
        self.ptxt_log.setPlainText("")

    def btnPathClicked(self):
        # Browse dialoge 
        directory=str(QFileDialog.getExistingDirectory(self,"Select Directory"))
        if directory != "":
            self.txt_path.setText(directory)
        
    def btnSubmitClicked(self):
        if self.logCore.observer.is_alive():
            self.fileFilters=self.txt_filter.text().split(',')
            self.logCore.setFilter(self.fileFilters,self.txt_path.text())
        else:
            self.messageBox.setMessage("Logger has not started !","""Please first set the path\nand after that set the filter""")

    def btnSaveClicked(self):
        # Write the filters to config.json file
        if self.fileFilters:
           t=threading.Thread(target=ConfigJson.createJsonFile,args=(self.fileFilters,))
           t.start()
        else:
            self.messageBox.setMessage("FilterEmptyError","No filters yet!")
    
    def btnJsonClicked(self):
        if os.path.isfile("config.json"):
            os.system("notepad config.json")
    
   


    def pathValidation(self,path):
        if path == "" : return 0
        elif os.path.isdir(path) : return 1
        else : return 2

    def PlainTextEditer(self,msg):
        # Print the log into ptxt
        self.ptxt_log.appendPlainText(msg)