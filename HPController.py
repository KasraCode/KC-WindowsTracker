from WTWController import WTW_Controller
from HomePage import HPWindow
from AboutUs import AboutUsWindow
# Create main window
class HP_Controller(HPWindow):
    def __init__(self):
        # Inheritance :)
        super(HP_Controller,self).__init__()
        # Connect the click event to the function.
        self.btn_tracker.clicked.connect(self.btnTrackerHpClicked)
        # Create an object from "windows tracker" window.
        self.wtw=WTW_Controller(self)
        self.btn_aboutUs.clicked.connect(self.btnAboutUsClicked)
        self.about=AboutUsWindow(self)
    # Click function
    def btnTrackerHpClicked(self):
        # Hiding the main window and switch to WT (windows tracker) window
        self.hide()
        self.wtw.show()
    
    def btnAboutUsClicked(self):
        self.hide()
        self.about.show()