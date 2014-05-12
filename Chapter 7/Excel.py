# Excel Example

from Tkinter import Tk
from time import sleep
from tkMessageBox import showwarning
import win32com.client as win32

warn = lambda app: showwarning(app,'Exit?')
RANGE = range(3,8)

def excel():
    
    app = 'Excel'
    xl = win32.gencache.EnsureDispatch('%s.Application' %app)
    ss = xl.Workbooks.Add() # Add a workbook that containts sheets to wich data is written
    sh =ss.ActiveSheet
    xl.visible = True
    sleep(1)

    sh.Cells(1,1).Value = 'Python-to-%s Demo' %app # Title of the program 
    sleep(1)
    for i in RANGE:
        sh.Cells(i,1).Value = 'Line %d' %i
        sleep(1) #Pause 1 second between each row
    
    sh.Cells(i+2,1).Value = "Th-th-thats all Folks!"
    warn(app)
    ss.Close(False)
    xl.Application.Quit()