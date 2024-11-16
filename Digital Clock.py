import tkinter as tk
from time import strftime
from datetime import datetime


root = tk.Tk()
root.title ("Digital Clock")
def time():
    now = datetime.now()
    string=strftime('%H:%M:%S %p\n')
    current_date = now.strftime("%A, %d %B %Y")
    specific_date = datetime(2024, 11, 16)  # Year, month, and day are mandatory

    label.config(text=string)
    date_label.config(text=current_date)
    label.after(1000,time)
    


label=tk.Label(root, font=('calibri',47,'bold'), background='light blue', foreground='black')
label.pack(anchor='w')
date_label = tk.Label(root, font=("calibri", 20,'bold'), background="light blue", foreground="black")
label.pack(anchor='center')
date_label.pack()

time()



root.mainloop()