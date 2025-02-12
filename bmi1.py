from tkinter import *
from tkinter import ttk
import os
from datetime import datetime
import matplotlib.pyplot as plt

co0 = "#444466"
co1 = "#feffff"
co2 = "#6856FF"

history_file = "bmi_history.txt"

if os.path.exists(history_file):
    with open(history_file, "r") as file:
        bmi_history = file.read().splitlines()
else:
    bmi_history = []

window = Tk()
window.title('')
window.geometry('295x380')
window.resizable(height=FALSE, width=FALSE)
window.configure(bg=co1)

top_frame = Frame(window, width=295, height=50, bg=co1, pady=0, padx=0)
top_frame.grid(row=0, column=0)

down_frame = Frame(window, width=295, height=330, bg=co1, pady=0, padx=0)
down_frame.grid(row=1, column=0)