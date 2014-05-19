
from Tkinter import Tk
from time import sleep
from tkMessageBox import showwarning
import win32com.client as win32

warn = lambda app: showwarning(app,'Exit?')
RANGE=range(3,8)

def word():
    app = 'Word'
    word = win32.gencache.EnsureDispatch('%s.Application' %app)
    doc = word.Documents.Add()
    word.Visible = True
    sleep(1)
    
    
    rng =doc.Range(0,0)
    rng.InsertAfter('Python to  %s Test'%app)
    sleep(1)
    #Insert strints into text range of document
    for i in RANGE:
        rng.InsertAfter('Line %d \r\n' %i) #Provide line termination
        sleep(1)
    rng.InsertAfter("\r\n Th th thats all folks!")
    warn(app)
    doc.Close(False)
    word.Application.Quit()
    
if __name__=='__main__':
    Tk().withdraw()
    word()