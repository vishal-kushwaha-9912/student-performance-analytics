
from pathlib import Path
import pandas as pd


def extract_data():
    # Find the main project folder
    project_root = Path(__file__).resolve().parents[1]

    # Define the raw CSV file location
    file_path = project_root / "data" / "raw" / "student_performance_messy.csv"

    # Check whether the file exists
    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    # Read the CSV file
    df = pd.read_csv(file_path)

    print("Data extraction successful!")
    print("Dataset shape:", df.shape)

    return df


if __name__ == "__main__":
    extract_data()
