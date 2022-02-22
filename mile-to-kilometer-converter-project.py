from tkinter import *


def value_in_miles():
    mile_value = miles_entry.get()
    mile_into_km = float(mile_value) * 1.609344
    km_value_label.config(text=f"{mile_into_km}")


window = Tk()
window.title("Mile to Kilometer converter")
window.minsize(width=250, height=100)
window.config(padx=40, pady=40)

miles_entry = Entry(width=10)
miles_entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

km_value_label = Label(text="0")
km_value_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=value_in_miles)
calculate_button.grid(row=2, column=1)

window.mainloop()
