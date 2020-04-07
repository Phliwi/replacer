from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from test import Ui_Dialog
from tkinter import *
from tkinter import filedialog as fd
import os
import fileinput



# start app
app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

'''
def bp():
    if ui.pushButton.clicked.connect(bp):
        file_name = fd.askopenfilename(filetypes=(("TXT files", "*.txt"),
                                                ("CSV files", "*.csv"),
                                                ("All files", "*.*")))
        f = open(file_name)
        s = f.read()
        text.insert(1.0, s)
        ui.label.setText(f)
    
        f.close()
        root = Tk()
        root.mainloop()
        
'''
sys.exit(app.exec_())