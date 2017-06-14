from tkinter import *
import csv
from tables import createStandardTable as cst

window = Tk()

tableFrame = Frame(window)

def hideTableFrame():
    tableFrame.grid_remove()

def createTableFrame():
    #Your csv file can contain as many rows and colums as needed
    f = open("films.csv")

    #note here I have sent it root but you can also send it a frame
    newtable = cst(f,tableFrame)
    newtable.grid()
    Button(tableFrame,text="Hide Me",command=hideTableFrame).grid()


createTableFrame()
tableFrame.grid()
