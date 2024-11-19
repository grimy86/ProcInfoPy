import wmi

def list_all_processes() -> list:
    """List all processes with their name, PID, and executable path."""
    c = wmi.WMI()
    processes = []
    for process in c.Win32_Process():
        processes.append({
            "PID": process.ProcessId,
            "Name": process.Name or "Unknown",
            "Path": process.ExecutablePath or "Unavailable"
        })
    return processes