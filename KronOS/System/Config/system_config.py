class SystemConfiguration:
    def __init__(self):
        self.version = "1.0.0"
        self.build = "2024.01.R2"
        self.registry = {
            "SYSTEM": {"LastBoot": "2024-01-20",
                      "Architecture": "x64",
                      "License": "KR0N-0S-2024"},
            "USER": {"Theme": "Default",
                    "Permissions": "Admin"}
        }

    def get_system_info(self):
        return "System information unavailable"
