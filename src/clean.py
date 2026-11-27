
import pandas as pd


def clean_data(df):

   ##### Create a copy so the original data remains unchanged
    
    
    clean_df = df.copy()

###### 1. Clean study hours
    clean_df["study_hours"] = pd.to_numeric(
        clean_df["study_hours"]
        .astype("string")
        .str.replace(" hrs", "", regex=False),
        errors="coerce"
    )

    ##### 2. Fill missing study hours using the median
    median_hours = clean_df["study_hours"].median()

    clean_df["study_hours"] = clean_df["study_hours"].fillna(
        median_hours
    )

    ######3. Clean attendance
    clean_df["attendance"] = pd.to_numeric(
        clean_df["attendance"]
        .astype("string")
        .str.replace("%", "", regex=False),
        errors="coerce"
    )

    ######4. Replace invalid attendance values above 100
    clean_df.loc[
        clean_df["attendance"] > 100,
        "attendance"
    ] = pd.NA

    # 5. Clean marks
    clean_df["marks"] = pd.to_numeric(
        clean_df["marks"]
        .astype("string")
        .str.replace("/100", "", regex=False),
        errors="coerce"
    )

    print("Data cleaning successful!")

    return clean_df


###### Run this file independently for testing
if __name__ == "__main__":

    from src.extract import extract_data

    raw_df = extract_data()

    cleaned_df = clean_data(raw_df)

    print("\nCleaned dataset:")
    print(cleaned_df)

    print("\nMissing values:")
    print(cleaned_df.isnull().sum())

    print("\nDataset shape:", cleaned_df.shape)
