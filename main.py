import pinfo
import tkinter as tk

def FillListBox(listBox : tk.Listbox):
    processes = pinfo.list_all_processes()
    for process in processes:
        pid = process["PID"]
        name = process["Name"]
        path = process["Path"]
        listBox.insert(tk.END, f"{pid:<10}{name:<30}{path}")

#STYLING
t1 : tuple = ("Arial", 14)
t2 : tuple = ("Arial", 11)
rpadx : int = 20 #str | float
rpady : int = 20

#ROOTCONFIG
root = tk.Tk()
root.geometry("500x650") #width, height
root.title("ProcInfoPy")
root.iconbitmap("icon.ico")
root.grid_columnconfigure(0, minsize=100 , weight=1)
root.grid_columnconfigure(1, weight=1)  # Column 1 grows twice as much as column 0
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

# Title Label
lblt = tk.Label(root, text="Processes", font=t1)
lblt.grid(row=0, column=0, columnspan=2, pady=rpady)

#LISTBOX & SCROLLBAR
scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=1, column=1, sticky="ns", padx=(0, rpadx))
lbox = tk.Listbox(root, yscrollcommand=scrollbar.set, font=t2)
lbox.grid(row=1, column=0, sticky="nsew", padx=rpadx, pady=rpady)
scrollbar.config(command=lbox.yview)
# Add headers to Listbox
lbox.insert(tk.END, f"{'PID':<10}{'Name':<30}{'Path'}")
lbox.insert(tk.END, "-" * 70)

FillListBox(lbox)
root.mainloop()

