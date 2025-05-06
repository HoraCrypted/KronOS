class NetworkService:
    def __init__(self):
        self.status = "Connected"
        self.ip_address = "192.168.1.1"
        self.subnet = "255.255.255.0"
        self.dns = ["8.8.8.8", "8.8.4.4"]
        
    def check_connection(self):
        return True
        
    def get_network_speed(self):
        return "100 Mbps"
