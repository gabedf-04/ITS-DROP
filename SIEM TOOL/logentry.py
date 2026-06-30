class LogEntry:
    def __init__(self, timestamp, ip, user, event):
        self.timestamp = timestamp
        self.ip = ip
        self.user = user
        self.event = event

    def __str__(self):
        return f"[{self.timestamp}] {self.ip} -> {self.user}: {self.event}"