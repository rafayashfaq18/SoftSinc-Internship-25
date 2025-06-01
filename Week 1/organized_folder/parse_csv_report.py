import csv
from datetime import datetime

def parse_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        missing = 0
        unique = {key: set() for key in reader.fieldnames}
        for row in reader:
            for key in row:
                if not row[key]:
                    missing += 1
                unique[key].add(row[key])
    with open("report.txt", "w") as report:
        report.write(f"Report Generated: {datetime.now()}\n")
        report.write(f"Missing values: {missing}\n")
        for key, values in unique.items():
            report.write(f"{key}: {len(values)} unique entries\n")

if __name__ == "__main__":
    parse_csv("sample.csv")