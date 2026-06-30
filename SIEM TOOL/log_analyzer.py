from datetime import datetime
from logentry import LogEntry

class LogAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.entries = []

    def parse_line(self, line):
        pezzi = line.split("|")

        timestamp_raw = pezzi[0].strip()
        ip_raw = pezzi[1].strip()
        user_raw = pezzi[2].strip()
        event_raw = pezzi[3].strip()

        ip_pezzi = ip_raw.split(":")
        user_pezzi = user_raw.split(":")
        event_pezzi = event_raw.split(":")

        ip = ip_pezzi[1]
        user = user_pezzi[1]
        event = event_pezzi[1]

        timestamp = datetime.strptime(timestamp_raw, "%Y-%m-%d %H:%M:%S")

        return LogEntry(timestamp, ip, user, event)

    def load_logs(self):
        with open(self.filepath, "r") as f:
            for line in f:
                if line.strip() == "":
                    continue  # salta le righe vuote
                entry = self.parse_line(line)
                self.entries.append(entry)