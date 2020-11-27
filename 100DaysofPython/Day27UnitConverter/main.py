from tkinter import *

window = Tk()

window.title("Miles to KM Converter")
window.minsize(height=100, width=200)
window.config(padx=20, pady=20)

is_equal = Label(text="is equal to")
is_equal.grid(row=1, column=0)


result = Label(text="0")
result.grid(row=1, column=1)


miles = Label(text="Miles")
miles.grid(row=0, column=2)


km = Label(text="Km")
km.grid(row=1, column=2)


def button_clicked():
    miles = float(input.get())
    km = round(miles * 1.609344, 2)
    result["text"] = km


button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

input = Entry(width=10)
input.grid(row=0, column=1)

window.mainloop()
