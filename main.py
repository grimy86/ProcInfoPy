import pinfo
import tkinter as tk
from tkinter import ttk

#PINFO
def FillTreeView(treeview) -> None:
        """Fills the treeview with the list of processes."""
        processes = pinfo.list_all_processes()  # Get the list of processes
        for process in processes:
            treeview.insert("", "end", values=(process["PID"], process["Name"], process["Path"]))

# STYLING
t1 = ("Arial", 14)
rpadx = 10
rpady = 10

# ROOT CONFIG
root = tk.Tk()
root.geometry("500x575")  # widthxheight
root.title("ProcInfoPy")
root.iconbitmap("icon.ico")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

# Title Label
lblt = tk.Label(root, text="Processes", font=t1)
lblt.grid(row=0, column=0, pady=rpady)

# TREEVIEW CONFIG
columns = ("PID", "Name", "Path")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.grid(row=1, column=0, sticky="nsew", padx=rpadx, pady=rpady)

# Scrollbar for Treeview
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.grid(row=1, column=1, sticky="ns")
tree.configure(yscrollcommand=scrollbar.set)

# Define headings
tree.heading("PID", text="PID", anchor="w")
tree.heading("Name", text="Name", anchor="w")
tree.heading("Path", text="Path", anchor="w")

# Adjust column widths
tree.column("PID", width=100, anchor="center")
tree.column("Name", width=200, anchor="w")
tree.column("Path", width=400, anchor="w")

# Run the application
FillTreeView(tree)
root.mainloop()
