from log_analyzer import LogAnalyzer

analyzer = LogAnalyzer("auth.log")
analyzer.load_logs()

for entry in analyzer.entries:
    print(entry)

contatori = {}

for entry in analyzer.entries:
    if entry.event == "LOGIN_FAILED":
        if entry.ip in contatori:
            contatori[entry.ip] = contatori[entry.ip] + 1
        else:
            contatori[entry.ip] = 1

print(contatori)