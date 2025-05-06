class SecurityMonitor:
    def __init__(self):
        self.firewall_status = "Active"
        self.threat_level = "Low"
        self.last_scan = "2024-01-20 12:00:00"
        
    def scan_system(self):
        return "No threats found"
        
    def update_definitions(self):
        return "Definitions up to date"
