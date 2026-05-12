from tkinter import *
import datetime

# CONNECT TO GOOGLE SHEETS
from google_auth import worksheet

root = Tk()
root.title("Age Calculator")
root.geometry("400x250")

NameVariable = StringVar()
YearVariable = StringVar()
MonthVariable = StringVar()
DayVariable = StringVar()

output_label = Label(root, text="")
output_label.grid(row=6, column=1, columnspan=2)

error_label = Label(root, text="", fg="red")
error_label.grid(row=7, column=1, columnspan=2)


def calculateage():

    error_label.config(text="")
    output_label.config(text="")

    if (YearVariable.get().strip() == "" or
        MonthVariable.get().strip() == "" or
        DayVariable.get().strip() == ""):
        error_label.config(text="Please fill all date fields")
        return

    name = NameVariable.get().strip()
    year = int(YearVariable.get())
    month = int(MonthVariable.get())
    day = int(DayVariable.get())

    birthdate = datetime.datetime(year, month, day)
    today = datetime.datetime.now()

    age_years = round((today - birthdate).days / 365, 2)

    output_label.config(text=f"{name}, your age is {age_years} years")

    # SAVE TO GOOGLE SHEET
    try:
        worksheet.append_row([
            name,
            year,
            month,
            day,
            age_years,
            today.strftime("%Y-%m-%d %H:%M:%S")
        ])
    except Exception as e:
        error_label.config(text=f"Error: {e}")


Label(root, text="Your Name").grid(row=1, column=1)
Label(root, text="Year").grid(row=2, column=1)
Label(root, text="Month").grid(row=3, column=1)
Label(root, text="Day").grid(row=4, column=1)

Entry(root, textvariable=NameVariable).grid(row=1, column=2)
Entry(root, textvariable=YearVariable).grid(row=2, column=2)
Entry(root, textvariable=MonthVariable).grid(row=3, column=2)
Entry(root, textvariable=DayVariable).grid(row=4, column=2)

Button(root, text="Submit", command=calculateage).grid(row=5, column=1)

root.mainloop()
