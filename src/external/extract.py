import pandas as pd
from pathlib import Path


def extract_data():

    # Locate the main project folder
    project_root = Path(__file__).resolve().parents[2]

    # Locate the external dataset
    file_path = project_root / "data" / "raw" / "student_performance_external.csv"
        # Check if the dataset exists
    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")
        # Read the external dataset
    df = pd.read_csv(file_path)

    print("External dataset extracted successfully!")
    print(f"Dataset shape: {df.shape}")

    return df