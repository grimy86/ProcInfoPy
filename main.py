import pinfo
import tkinter as tk
from tkinter import ttk

def FillTreeView(treeview):
    """Populate the Treeview with process information."""
    processes = pinfo.list_all_processes()
    for process in processes:
        pid = process["PID"]
        name = process["Name"]
        path = process["Path"]
        treeview.insert("", "end", values=(pid, name, path))

# STYLING
t1 = ("Arial", 14)
rpadx = 10
rpady = 10

# ROOT CONFIG
root = tk.Tk()
root.geometry("700x500")  # Adjusted dimensions
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
tree.heading("PID", text="PID")
tree.heading("Name", text="Name")
tree.heading("Path", text="Path")

# Adjust column widths
tree.column("PID", width=100, anchor="center")
tree.column("Name", width=200, anchor="w")
tree.column("Path", width=400, anchor="w")

# Populate the Treeview
FillTreeView(tree)

# Run the application
root.mainloop()
