import pandas as pd
from datetime import datetime

def generate_report(df, log):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    summary = df.describe(include='all')
    file_txt = f"summary_{timestamp}.txt"
    file_csv = f"summary_{timestamp}.csv"

    with open(file_txt, 'w') as f:
        f.write("Summary Report\n")
        f.write(str(summary))
        f.write("\n\nChange Log:\n")
        f.write("\n".join(log))

    summary.to_csv(file_csv)
    return file_txt, file_csv
