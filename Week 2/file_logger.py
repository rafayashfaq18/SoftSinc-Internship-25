from datetime import datetime

class Logger:
    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        with open(self.filename, 'a') as f:
            f.write(f"{datetime.now()} - {message}\n")
