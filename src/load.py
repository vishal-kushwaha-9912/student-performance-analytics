
from pathlib import Path


def load_data(cleaned_df, transformed_df, summary_df):

    # Find the main project folder
    project_root = Path(__file__).resolve().parents[1]

    # Create processed folder path
    output_folder = project_root / "data" / "processed"

    # Create the folder if it does not exist
    output_folder.mkdir(parents=True, exist_ok=True)

    # Save cleaned dataset
    cleaned_df.to_csv(
        output_folder / "student_performance_cleaned.csv",
        index=False
    )

    # Save transformed dataset
    transformed_df.to_csv(
        output_folder / "student_performance_transformed.csv",
        index=False
    )

    # Save performance summary
    summary_df.to_csv(
        output_folder / "performance_summary.csv",
        index=False
    )

    print("\n========== DATA LOADING ==========")

    print("Cleaned dataset saved successfully!")
    print("Transformed dataset saved successfully!")
    print("Performance summary saved successfully!")

    print("\nOutput folder:", output_folder)


# Test the loading module
if __name__ == "__main__":

    from src.extract import extract_data
    from src.clean import clean_data
    from src.transform import transform_data
    from src.analyze import analyze_data

    raw_df = extract_data()

    cleaned_df = clean_data(raw_df)

    transformed_df = transform_data(cleaned_df)

    summary_df = analyze_data(transformed_df)

    load_data(cleaned_df, transformed_df, summary_df)
