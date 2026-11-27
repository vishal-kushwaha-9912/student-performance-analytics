import pandas as pd
from pathlib import Path
import pytest

from src.load import load_data
from src.extract import extract_data
from src.clean import clean_data
from src.transform import transform_data
from src.analyze import analyze_data
from src.validate import validate_data

def test_extract_data():
    """Check whether the raw dataset is extracted correctly."""

    df = extract_data()

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (10, 6)
    assert "student_id" in df.columns
    assert "marks" in df.columns


def test_clean_data():
    """Check whether messy data is cleaned correctly."""

    raw_df = extract_data()
    cleaned_df = clean_data(raw_df)

    # Check the missing study hours were filled
    assert cleaned_df.loc[3, "study_hours"] == 2.5

    # Check the text value was converted to a number
    assert cleaned_df.loc[1, "study_hours"] == 1.8

    # Check invalid attendance was handled
    assert pd.isna(cleaned_df.loc[2, "attendance"])

    # Check marks were converted correctly
    assert cleaned_df.loc[2, "marks"] == 55

    # Check the dataset still has 10 rows
    assert cleaned_df.shape == (10, 6)




from src.transform import transform_data
from src.analyze import analyze_data


def test_transform_data():
    """Check whether performance and attendance groups are correct."""

    raw_df = extract_data()
    cleaned_df = clean_data(raw_df)
    transformed_df = transform_data(cleaned_df)

    # Check the transformed dataset shape
    assert transformed_df.shape == (10, 8)

    # Check performance categories
    assert transformed_df.loc[0, "performance"] == "Excellent"
    assert transformed_df.loc[2, "performance"] == "Average"
    assert transformed_df.loc[6, "performance"] == "Needs Improvement"

    # Check attendance categories
    assert transformed_df.loc[0, "attendance_group"] == "Excellent"
    assert transformed_df.loc[2, "attendance_group"] is pd.NA or pd.isna(
        transformed_df.loc[2, "attendance_group"]
    )


def test_analyze_data():
    """Check whether the analysis produces correct summary statistics."""

    raw_df = extract_data()
    cleaned_df = clean_data(raw_df)
    transformed_df = transform_data(cleaned_df)

    summary_df = analyze_data(transformed_df)

    # Check the performance summary
    assert len(summary_df) == 4

    # Check student counts in each performance category
    assert summary_df["student_count"].tolist() == [1, 2, 1, 6]

    # Check average marks for each category
    assert summary_df["average_marks"].tolist() == [48.0, 60.0, 78.0, 89.83]

    # Check overall average marks
    assert transformed_df["marks"].mean() == 78.5

    # Check highest and lowest marks
    assert transformed_df["marks"].max() == 96
    assert transformed_df["marks"].min() == 48



def test_load_data():
    """Check whether all processed CSV files are saved correctly."""

    raw_df = extract_data()
    cleaned_df = clean_data(raw_df)
    transformed_df = transform_data(cleaned_df)
    summary_df = analyze_data(transformed_df)

    # Run the loading function
    load_data(cleaned_df, transformed_df, summary_df)

    # Locate the processed data folder
    project_root = Path(__file__).resolve().parents[1]
    output_folder = project_root / "data" / "processed"

    # Check whether all three CSV files exist
    cleaned_file = output_folder / "student_performance_cleaned.csv"
    transformed_file = output_folder / "student_performance_transformed.csv"
    summary_file = output_folder / "performance_summary.csv"

    assert cleaned_file.exists()
    assert transformed_file.exists()
    assert summary_file.exists()

    # Read the exported files
    exported_cleaned = pd.read_csv(cleaned_file)
    exported_transformed = pd.read_csv(transformed_file)
    exported_summary = pd.read_csv(summary_file)

    # Verify exported data
    assert exported_cleaned.shape == (10, 6)
    assert exported_transformed.shape == (10, 8)
    assert exported_summary.shape == (4, 5)

    assert exported_cleaned["marks"].mean() == 78.5


# ==========================================
# TEST 6: VALID DATA VALIDATION
# ==========================================

def test_validate_data():
    """Check whether valid cleaned data passes validation."""

    raw_df = extract_data()
    cleaned_df = clean_data(raw_df)

    result = validate_data(cleaned_df)

    assert result is True


# ==========================================
# TEST 7: DUPLICATE STUDENT ID
# ==========================================

def test_validate_duplicate_student_id():
    """Check whether duplicate student IDs are rejected."""

    raw_df = extract_data()
    cleaned_df = clean_data(raw_df)

    invalid_df = cleaned_df.copy()
    invalid_df.loc[1, "student_id"] = invalid_df.loc[0, "student_id"]

    with pytest.raises(ValueError, match="Duplicate student IDs"):
        validate_data(invalid_df)


# ==========================================
# TEST 8: INVALID MARKS
# ==========================================

def test_validate_invalid_marks():
    """Check whether marks above 100 are rejected."""

    raw_df = extract_data()
    cleaned_df = clean_data(raw_df)

    invalid_df = cleaned_df.copy()
    invalid_df.loc[0, "marks"] = 150

    with pytest.raises(ValueError, match="Marks must be between 0 and 100"):
        validate_data(invalid_df)


# ==========================================
# TEST 9: NEGATIVE STUDY HOURS
# ==========================================

def test_validate_negative_study_hours():
    """Check whether negative study hours are rejected."""

    raw_df = extract_data()
    cleaned_df = clean_data(raw_df)

    invalid_df = cleaned_df.copy()
    invalid_df.loc[0, "study_hours"] = -5

    with pytest.raises(ValueError, match="Study hours cannot be negative"):
        validate_data(invalid_df)