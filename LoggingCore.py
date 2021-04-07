import logging
import datetime
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject

#Create file logger engine with pattern checker :
class FileLogging(FileSystemEventHandler):
    def __init__(self,pattern=None):
        super().__init__()
        self.pattern=pattern
        # Connect to main logging core
        self.logger=logging.root

    # These functions are overwrited. These methods call allEventHandler, but send their own values. 
    # This will increase the speed and causes no rewriting.
    def on_created(self,event):
        # event.is_directory -> a boolian value 
        # "Created" and others -> what happend to file
        # event.src_path and event.dest_path -> filename
        self.allEventHandler(event.is_directory,"Created",event,event.src_path)

    def on_deleted(self,event):
        self.allEventHandler(event.is_directory,"Deleted",event,event.src_path)
            
    def on_modified(self,event):
        self.allEventHandler(event.is_directory,"Modified",event,event.src_path)
        
    def on_moved(self,event):
        self.allEventHandler(event.is_directory,"Moved",event,event.src_path,event.dest_path)

    def on_closed(self,event):
        self.allEventHandler(event.is_directory,"Closed",event,event.src_path)

    def allEventHandler(self,isDir, whatHappend, fileEvent, fileSrc, fileDest=None):
        # Call the patterncheck function : event.src_path=filename
        isPattern=self.patterncheck(fileSrc)
        what = 'directory' if isDir else 'file'
        # If isPattern be true, then this file/directory is filtered
        if isPattern:
            pass
        else:
            # Call the super class methods for each event
            if whatHappend=="Created":
                super().on_created(fileEvent)
            elif whatHappend=="Deleted":
                super().on_deleted(fileEvent)
            elif whatHappend=="Modified":
                super().on_modified(fileEvent)
            elif whatHappend=="Moved":
                super().on_moved(fileEvent)
            elif whatHappend=="Closed":
                super().on_closed()
            # Logging : If file moved, then the message is deffernt
            if whatHappend=="Moved":
                # Logging message
                self.logger.info("Moved %s: from %s to %s", what, fileSrc,
                         fileDest)
            else:
                # Other logging messages
                self.logger.info("%s %s: %s", whatHappend, what, fileSrc)

    def patterncheck(self,path):
        # Get the last word (example : kasra.code.txt=["kasra","code","txt"])
        extensions=path.split('.')
        try:
            # Get the last word (from example above : index(txt)=2 -> last=-1)
            if extensions[-1] in self.pattern:
                # Reaturning true means that the file is filtered.
                return True
            else:
                # Means that the file is not filtered.
                return False
        except TypeError:
            return False

# This is a bit complicated !
# For recording the log and print it in QPlainTextEdit, we have to 
# create own signal for passing the log.
# For this reason I created an object with two super class.
# 1-QObject : creating an object can use in our gui program.
# 2- logging.Handler : For recording the messages 
# Note : We use this object in WTWController.py
class LoggingTextBox(QObject, logging.Handler):
    # pyqtSignal can create a connection.
    new_record = pyqtSignal(object)
    def __init__(self, parent):
        super().__init__(parent=parent)
        super(logging.Handler).__init__()
    # emit function is an event function from Handler object
    def emit(self, record):
        # Get the message
        msg = self.format(record)
        # Call the new_record object emit function and pass the msg
        self.new_record.emit(msg)

# Create an object for controlling the "observer"
class TrackingCore:
    def __init__(self):
        self.directorPath=None
        # Create event handler core object
        self.event_handler = FileLogging()
        # Use a observer
        self.observer = Observer()
        # The filename of the log
        # Note : If you start the observer and stop it, then start
        # it again, the log file does not change.(for each day)
        self.fileName="LogFiles/LogFile"+str(datetime.date.today().strftime('%y-%m-%d'))+'.log'
        # Configure the basic settings of logging root
        # Such as : filename,level log,log format,date typing format
        logging.basicConfig(filename=self.fileName,level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
        
    def start(self, isfile=False, directoryPath=None, data=None):
        """Starting Tracker"""

        self.observer.start()
        # If config.json file exists, setFilter function will call and
        # gets the filters in config.json file 
        if isfile:
            self.setFilter(data,directoryPath)

    def stop(self):
        """Stoping Tracker"""

        self.observer.stop() 
        
    def setPath(self,directoryPath:str):
        """param:directoryPath -> str
        Setting the path you want to track
        If you want to stop tracking , call unschedule_all method
        else for starting again , call setPath method"""

        # Program the behavior of observer
        self.observer.schedule(self.event_handler, directoryPath, recursive=True)

    def setFilter(self,Filters:str,directoryPath:str):
        # Setting the filters
        patternChecker=FileLogging(Filters)
        # Unprogram all schedules
        self.observer.unschedule_all()
        # Create ne schedule with new filters
        self.observer.schedule(patternChecker,directoryPath,recursive=True)
