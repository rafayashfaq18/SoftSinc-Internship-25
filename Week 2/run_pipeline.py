import pandas as pd
from clean_data import clean_data
from visualize_data import visualize_data
from report_generator import generate_report

def run_pipeline(filepath):
    df = pd.read_csv(filepath)
    df_clean, log = clean_data(df)
    visualize_data(df_clean)
    txt, csv = generate_report(df_clean, log)
    print(f"Reports saved to {txt} and {csv}")

if __name__ == "__main__":
    run_pipeline("sample_data.csv")
