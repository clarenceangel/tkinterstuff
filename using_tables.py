from tkinter import *
import csv
from tables import createStandardTable as cst

window = Tk()

#Your file can contain any number of rows and columns so long as they
#are even of course. Make sure you rename the films to the name of your file
f = open("films.csv")

#note here I have sent it root but you can also send it a frame
#see using tables with frames
#It actually returns a frame that will be placed on the window or frame
#you send
newtable = cst(f,window)

newtable.grid()

