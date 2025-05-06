class ProcessManager:
    def __init__(self):
        self.active_processes = {
            "system_idle": {"pid": 0, "cpu": "0%", "memory": "0MB"},
            "kron_kernel": {"pid": 1, "cpu": "1%", "memory": "24MB"},
            "user_interface": {"pid": 2, "cpu": "2%", "memory": "156MB"}
        }
        
    def list_processes(self):
        return self.active_processes
