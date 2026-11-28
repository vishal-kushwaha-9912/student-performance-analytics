
import pandas as pd
import pytest
from pathlib import Path
from src.external.load import load_data
from src.external.pipeline import run_pipeline

from src.external.extract import extract_data
from src.external.clean import clean_data
from src.external.validate import validate_data
from src.external.transform import transform_data
from src.external.analyze import analyze_data


# Test 1: External data extraction
def test_external_extract_data():

    df = extract_data()

    # Check dataset dimensions
    assert df.shape == (395, 33)

    # Check dataset is not empty
    assert not df.empty

    # Check important columns
    assert "G3" in df.columns
    assert "G1" in df.columns
    assert "G2" in df.columns


# Test 2: External data cleaning
def test_external_clean_data():

    df = extract_data()

    cleaned_df = clean_data(df)

    # Check lowercase column names
    assert all(
        column == column.lower()
        for column in cleaned_df.columns
    )

    # Check dataset shape remains unchanged
    assert cleaned_df.shape == df.shape

    # Check original dataset is not modified
    assert "G3" in df.columns
    assert "g3" in cleaned_df.columns


# Test 3: External data validation
def test_external_validate_data():

    df = clean_data(extract_data())

    # Valid dataset should pass validation
    result = validate_data(df)

    assert result is True
    
# Test 4: External data transformation
def test_external_transform_data():

    df = clean_data(extract_data())

    transformed_df = transform_data(df)

    # Check transformed dataset dimensions
    assert transformed_df.shape == (395, 36)

    # Check newly created columns
    assert "average_grade" in transformed_df.columns
    assert "result" in transformed_df.columns
    assert "performance" in transformed_df.columns

    # Check average grades are within valid range
    assert transformed_df["average_grade"].between(0, 20).all()

    # Check result values
    assert set(transformed_df["result"].unique()).issubset(
        {"Pass", "Fail"}
    )



# Test 5: External data analysis
def test_external_analyze_data():

    df = clean_data(extract_data())

    transformed_df = transform_data(df)

    summary_df = analyze_data(transformed_df)

    # Check summary columns
    assert list(summary_df.columns) == ["metric", "value"]

    # Check number of summary metrics
    assert len(summary_df) == 7

    # Check total student count
    total_students = summary_df.loc[
        summary_df["metric"] == "Total Students", "value"
    ].iloc[0]

    assert total_students == 395

    # Check average final grade
    average_grade = summary_df.loc[
        summary_df["metric"] == "Average Final Grade", "value"
    ].iloc[0]

    assert average_grade == 10.42

    
    
# Test 6: External data loading
def test_external_load_data():

    df = clean_data(extract_data())

    transformed_df = transform_data(df)

    summary_df = analyze_data(transformed_df)

    # Load all processed datasets
    load_data(df, transformed_df, summary_df)

    # Locate the output folder
    project_root = Path(__file__).resolve().parents[1]

    output_folder = (
        project_root / "data" / "processed" / "external"
    )

    # Check whether all output files exist
    assert (output_folder / "student_performance_cleaned.csv").exists()

    assert (output_folder / "student_performance_transformed.csv").exists()

    assert (output_folder / "performance_summary.csv").exists()

    
    
# Test 7: Complete external ETL pipeline
def test_external_pipeline():

    # Run the complete ETL pipeline
    result = run_pipeline()

    # Check that the pipeline completes
    assert result is None

    # Check that all output files are generated
    project_root = Path(__file__).resolve().parents[1]

    output_folder = (
        project_root / "data" / "processed" / "external"
    )

    assert (output_folder / "student_performance_cleaned.csv").exists()
    assert (output_folder / "student_performance_transformed.csv").exists()
    assert (output_folder / "performance_summary.csv").exists()
