import os
import ctypes
from ctypes import wintypes

class ProcessInfo:
    def __init__(self, pid):
        """Initialize with the process ID."""
        self.pid = pid

    def get_name(self):
        """Retrieve the process name."""
        h_process = ctypes.windll.kernel32.OpenProcess(0x1000, False, self.pid)
        if not h_process:
            return "Unable to access process"

        exe_name = (ctypes.c_char * 260)()
        if ctypes.windll.psapi.GetModuleBaseNameA(h_process, None, exe_name, ctypes.sizeof(exe_name)):
            ctypes.windll.kernel32.CloseHandle(h_process)
            return exe_name.value.decode()
        else:
            ctypes.windll.kernel32.CloseHandle(h_process)
            return "Unknown Process"

    def get_exe_path(self):
        """Retrieve the executable path of the process."""
        h_process = ctypes.windll.kernel32.OpenProcess(0x1000, False, self.pid)
        if not h_process:
            return "Unable to access process"

        exe_path = (ctypes.c_char * 260)()
        if ctypes.windll.psapi.GetModuleFileNameExA(h_process, None, exe_path, ctypes.sizeof(exe_path)):
            ctypes.windll.kernel32.CloseHandle(h_process)
            return exe_path.value.decode()
        else:
            ctypes.windll.kernel32.CloseHandle(h_process)
            return "Unknown Path"
        
@staticmethod
def list_all_processes():
    """List all processes with their name and executable path."""
    processes = []
    process_ids = (wintypes.DWORD * 1024)()  # Buffer for process IDs
    count = wintypes.DWORD()  # Actual number of process IDs

    # Get process IDs
    if ctypes.windll.psapi.EnumProcesses(ctypes.byref(process_ids), ctypes.sizeof(process_ids), ctypes.byref(count)):
        for pid in process_ids[:count.value // ctypes.sizeof(wintypes.DWORD)]:
            process = ProcessInfo(pid)
            name = process.get_name()
            path = process.get_exe_path()
            processes.append({"PID": pid, "Name": name, "Path": path})
    return processes