import subprocess

def main():
    options = {
        "1": "calculator.py",
        "2": "unit_converter.py",
        "3": "file_organizer.py",
        "4": "password_generator.py",
        "5": "oop_chat_structure.py",
        "6": "parse_csv_report.py",
        "7": "log_summarizer.py",
        "8": "pandas_analysis.py"
    }

    print("Softsinc Week 1 Launcher")
    for key, script in options.items():
        print(f"{key}. Run {script}")

    choice = input("Enter your choice: ").strip()
    script = options.get(choice)

    if script:
        subprocess.run(["python3", script], check=False)
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()