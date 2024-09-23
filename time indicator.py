# import datetime

# def get_greeting():
#     current_time= datetime.datetime.now()
#     hour =current_time.hour

#     if hour < 12:
#         return "Good Morning!"
#     elif hour < 15:
#         return "Good Afternoon!"
#     else:
#         return "Good Evening!"

# # print(f"{get_greeting()} Current time is {current_time.strftime('%I:%M %p')}")
import time
import tkinter as tk

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")

clock_label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
clock_label.pack(fill='both', expand=1)

update_time()
root.mainloop()
