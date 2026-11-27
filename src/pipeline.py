
from src.extract import extract_data
from src.clean import clean_data
from src.transform import transform_data
from src.analyze import analyze_data
from src.load import load_data
from src.validate import validate_data


def run_pipeline():

    print("\n========== STUDENT PERFORMANCE ETL PIPELINE ==========")

    # Step 1: Extract
    raw_df = extract_data()

    # Step 2: Clean
    cleaned_df = clean_data(raw_df)

    # Step 3: Validate
    validate_data(cleaned_df)

    # Step 4: Transform
    transformed_df = transform_data(cleaned_df)

    # Step 5: Analyze
    summary_df = analyze_data(transformed_df)

    # Step 6: Load
    load_data(cleaned_df, transformed_df, summary_df)

    print("\n========== PIPELINE COMPLETED SUCCESSFULLY ==========")


if __name__ == "__main__":
    run_pipeline()
