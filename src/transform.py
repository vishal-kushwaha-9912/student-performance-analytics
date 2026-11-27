
import pandas as pd


def transform_data(clean_df):

    # Create a copy of cleaned data
    transformed_df = clean_df.copy()

    # 1. Create performance categories
    transformed_df["performance"] = pd.cut(
        transformed_df["marks"],
        bins=[-1, 49, 69, 84, 100],
        labels=[
            "Needs Improvement",
            "Average",
            "Good",
            "Excellent"
        ]
    )

    # 2. Create attendance groups
    transformed_df["attendance_group"] = pd.cut(
        transformed_df["attendance"],
        bins=[-1, 59, 74, 89, 100],
        labels=[
            "Low",
            "Moderate",
            "Good",
            "Excellent"
        ]
    )

    print("Data transformation successful!")

    return transformed_df


# Test the transformation module
if __name__ == "__main__":

    from src.extract import extract_data
    from src.clean import clean_data

    raw_df = extract_data()

    cleaned_df = clean_data(raw_df)

    transformed_df = transform_data(cleaned_df)

    print("\nTransformed dataset:")
    print(transformed_df)

    print("\nPerformance distribution:")
    print(transformed_df["performance"].value_counts())

    print("\nAttendance group distribution:")
    print(transformed_df["attendance_group"].value_counts())

    print("\nDataset shape:", transformed_df.shape)
