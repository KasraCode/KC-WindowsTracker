from HPController import HP_Controller
from PyQt5.QtWidgets import QApplication
import os


if __name__ == "__main__":
    # The following condition checks the existence of the LogFiles
    # folder and, if it does not exist, creates it.
    if not os.path.isdir("LogFiles"):
        os.mkdir("LogFiles")
    # Running the program
    app=QApplication([])
    home=HP_Controller()
    home.show()
    app.exec_()    