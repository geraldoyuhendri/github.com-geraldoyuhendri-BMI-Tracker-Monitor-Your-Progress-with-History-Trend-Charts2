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

app_name = Label(top_frame, text="BMI Calculator", width=23, height=1, padx=0, anchor="center", font=("Ivy 16 bold"), bg=co1, fg=co0)
app_name.place(x=0, y=2)

app_line = Label(top_frame, text="", width=400, height=1, padx=0, anchor="center", font=("Arial 1"), bg=co2, fg=co0)
app_line.place(x=0, y=35)

def calculate():
    try:
        weight = float(e_weight.get())
        height = float(e_height.get()) ** 2
        result = weight / height

        if result < 18.4:
            category = "Underweight"
        elif result >= 18.5 and result < 24.9:
            category = "Normal"
        elif result >= 25 and result < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        l_result_text['text'] = f"Your BMI is: {category}"
        l_result['text'] = "{:.2f}".format(result)

        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"Date: {current_date}, Weight: {weight} kg, Height: {height ** 0.5:.2f} m, BMI: {result:.2f}, Category: {category}"
        bmi_history.append(entry)

        with open(history_file, "a") as file:
            file.write(entry + "\n")
    except ValueError:
        l_result_text['text'] = "Please enter valid inputs!"

def show_history():
    history_window = Toplevel(window)
    history_window.title("BMI History")
    history_window.geometry("300x300")
    history_window.configure(bg=co1)

    history_label = Label(history_window, text="BMI History", font=("Ivy 14 bold"), bg=co1, fg=co0)
    history_label.pack(pady=10)

    history_text = Text(history_window, width=35, height=15, font=("Ivy 10"), bg=co1, fg=co0, wrap=WORD)
    history_text.pack(pady=5)

    for entry in bmi_history:
        history_text.insert(END, entry + "\n")

    history_text.config(state=DISABLED)

def show_chart():
    dates = []
    bmi_values = []

    for entry in bmi_history:
        parts = entry.split(", ")
        try:
            date = parts[0].split(": ")[1]
            bmi = float(parts[3].split(": ")[1])  
            dates.append(date)
            bmi_values.append(bmi)
        except (IndexError, ValueError):
            continue

    if dates and bmi_values:
        plt.figure(figsize=(8, 5))
        plt.plot(dates, bmi_values, marker='o', linestyle='-', color='b', label="BMI")
        plt.axhline(18.5, color='green', linestyle='--', label="Normal Lower Bound")
        plt.axhline(24.9, color='green', linestyle='--', label="Normal Upper Bound")
        plt.xticks(rotation=45, ha="right")
        plt.title("BMI History Chart")
        plt.xlabel("Date")
        plt.ylabel("BMI")
        plt.legend()
        plt.tight_layout()
        plt.show()
    else:
        l_result_text['text'] = "No valid data to display in the chart!"


l_weight = Label(down_frame, text="Enter your weight", height=1, padx=0, anchor="center", font=("Ivy 10 bold"), bg=co1, fg=co0)
l_weight.grid(row=0, column=0, columnspan=1, pady=10, padx=3)
e_weight = Entry(down_frame, width=5, font=("Ivy 10 bold"), justify="center", relief=SOLID)
e_weight.grid(row=0, column=1, columnspan=1, pady=10, padx=3)

l_height = Label(down_frame, text="Enter your height", height=1, padx=0, anchor="center", font=("Ivy 10 bold"), bg=co1, fg=co0)
l_height.grid(row=1, column=0, columnspan=1, pady=10, padx=3)
e_height = Entry(down_frame, width=5, font=("Ivy 10 bold"), justify="center", relief=SOLID)
e_height.grid(row=1, column=1, columnspan=1, pady=10, padx=3)

l_result = Label(down_frame, width=5, text="----", height=1, padx=6, pady=12, anchor="center", font=('Ivy 24 bold'), bg=co2, fg=co1)
l_result.place(x=175, y=10)

l_result_text = Label(down_frame, width=37, text="", height=1, padx=6, pady=12, anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_result_text.place(x=0, y=85)

b_calculate = Button(down_frame, text="Calculate", width=34, height=1, bg=co2, fg=co1, font=("Ivy 10 bold"), anchor="center", command=calculate)
b_calculate.grid(row=4, column=0, pady=10, padx=5, columnspan=30)

b_history = Button(down_frame, text="History", width=34, height=1, bg=co2, fg=co1, font=("Ivy 10 bold"), anchor="center", command=show_history)
b_history.grid(row=5, column=0, pady=10, padx=5, columnspan=30)

b_chart = Button(down_frame, text="Show Chart", width=34, height=1, bg=co2, fg=co1, font=("Ivy 10 bold"), anchor="center", command=show_chart)
b_chart.grid(row=6, column=0, pady=10, padx=5, columnspan=30)


def reset_history():
    global bmi_history
    bmi_history = []

    with open(history_file, "w") as file:
        file.write("")  
    
    l_result_text['text'] = "History has been reset!"
    l_result['text'] = "----"

b_reset = Button(down_frame, text="Reset History", width=34, height=1, bg="red", fg=co1, font=("Ivy 10 bold"), anchor="center", command=reset_history)
b_reset.grid(row=7, column=0, pady=10, padx=5, columnspan=30)

window.mainloop()