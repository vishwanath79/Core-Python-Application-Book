#5-5 Road Signs Partial Function Applications 

from functools import partial as pto
from Tkinter import Tk,Button,X
from tkMessageBox import showinfo,showwarning,showerror
#Define signs along with categories
WARN='warn'
CRIT='crit'
REGU='regu'
SIGNS={
    'do not enter': CRIT,
    'railroad crossing':WARN,
    '55 speed limit':REGU,
    'wrong way':CRIT,
    'merging traffic':WARN,
    'one way':REGU,
}
#Test
#Tk dialogs are assigned as button callbacks.
critCB=lambda:showerror('Error','Error button presssed')
warnCB=lambda:showwarning('Warning','Warning button pressed')
infoCB=lambda:showinfo('Info','Info button pressed')
# launch Tk sset title and create quit
top = Tk()
top.title('Road signs')
Button(top,text='QUIT',command=top.quit,bg='red',fg='white').pack()

#PFA- Templatize button class and root window top
MyButton=pto(Button,top)
#PFA - Use myButton and templatize that. CritButton calls MyButton calls Button
CritButton=pto(MyButton,command=critCB,bg='white',fg='red')
WarnButton = pto(MyButton,command=warnCB,bg='goldenrod1')
ReguButton = pto(MyButton, command =infoCB,bg='white')
# Construct string Python can evaluate
#pass button label as text argument, if critical sign then capitalize the button text esle titelcase it
#instantiate button with eval()
for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = '%sButton(text=%r%s).pack(fill=X,expand=True)'%(signType.title(),eachSign,'.upper()' if signType == CRIT else '.title()')
    eval(cmd)
top.mainloop()