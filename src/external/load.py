
from pathlib import Path
import pandas as pd


def load_data(cleaned_df, transformed_df, summary_df):

    # Locate the main project folder
    project_root = Path(__file__).resolve().parents[2]

    # Create the external output folder
    output_folder = project_root / "data" / "processed" / "external"
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

    # Save analysis summary
    summary_df.to_csv(
        output_folder / "performance_summary.csv",
        index=False
    )

    print("External datasets saved successfully!")
    print(f"Output folder: {output_folder}")
   
   
    
def example():
    print("Inside function")  # Runs when function is called

print("Outside function")     # Runs independently
