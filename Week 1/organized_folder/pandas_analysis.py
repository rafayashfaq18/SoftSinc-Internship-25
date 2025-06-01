import pandas as pd

def analyze():
    df = pd.read_csv("titanic.csv")
    df = df.drop_duplicates().dropna()
    print("Average survival by gender:")
    print(df.groupby("Sex")["Survived"].mean())

if __name__ == "__main__":
    analyze()