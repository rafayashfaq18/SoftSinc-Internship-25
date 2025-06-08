import pandas as pd

def clean_data(df):
    changes = []
    # Drop rows with missing values
    missing_before = df.isnull().sum().sum()
    df = df.dropna()
    changes.append(f"Dropped rows with missing values: {missing_before} entries removed")
    # Convert column types if needed
    for col in df.select_dtypes(include=['object']).columns:
        try:
            df[col] = pd.to_datetime(df[col])
            changes.append(f"Converted {col} to datetime")
        except Exception:
            continue
    return df, changes
