import os
from datetime import datetime

def summarize_logs(log_dir):
    errors = []
    for file in os.listdir(log_dir):
        if file.endswith(".log") or file.endswith(".txt"):
            with open(os.path.join(log_dir, file)) as f:
                for line in f:
                    if "ERROR" in line:
                        errors.append(line.strip())
    with open("log_summary.txt", "w") as report:
        report.write(f"Log Summary ({datetime.now()}):\n")
        for err in errors:
            report.write(err + "\n")

if __name__ == "__main__":
    summarize_logs("logs")