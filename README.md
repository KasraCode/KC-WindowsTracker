# KC-WindowsTracker
A project to track changes that occur in Windows files.</br>
Such as : Modified files , deleted and created and ...
# Files in main folder :
<ul>
  <li>Main.py</li>
  <li>HomePage.py</li>
  <li>WindowsTrackerWindow.py</li>
  <li>HPController.py</li>
  <li>WTWController.py</li>
  <li>LoggingCore.py</li>
  <li>ConfigJson.py</li>
  <li>AboutUs.py</li>
</ul>
<h2>Main.py</h2>
Starting the program.
<h2>HomePage.py</h2>
Design the home page and components.This file use the MainWindow.ui file in UiFiles Folder.</br>
This file contains variables to define the components and access to them.
<h2>WindowsTrackerWindow.py</h2>
Design the Windows Tracker components with WinTracker.ui file in UiFiles Folder.
<h2>HPController.py</h2>
Controll the home page behavior (ex. Click event, show and hide ,etc ...)
<h2>WTWController.py</h2>
Controll the Tracking window behavior (ex. Click event, logging ,etc ...)</br>
<h2>LoggingCore.py</h2>
This files is the main core of the program. In this script,</br> the main software programs are written. Like Logging engine, pattern checker, etc ...
<h2>ConfigJson.py</h2>
This script used for creating config.json file and saving settings in that.
<h2>AboutUs.py</h2>
Open the about us window with UiFiles/AboutUs.ui file
<h2>Libraries</h2>
PyQt5 - watchdog
