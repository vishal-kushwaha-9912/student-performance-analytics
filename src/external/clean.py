
import pandas as pd


def clean_data(df):

    # Create a copy of the original dataset
    cleaned_df = df.copy()

    # Standardize column names
    cleaned_df.columns = cleaned_df.columns.str.strip().str.lower()

    # Remove extra spaces from text columns
    for column in cleaned_df.select_dtypes(
        include=["object", "str"]
    ).columns:
        cleaned_df[column] = cleaned_df[column].str.strip()

    # Check missing values
    missing_values = cleaned_df.isnull().sum()

    print("Missing values before handling:")
    print(missing_values[missing_values > 0])

    # Check duplicate records
    duplicate_count = cleaned_df.duplicated().sum()

    print(f"Duplicate records found: {duplicate_count}")

    return cleaned_df
