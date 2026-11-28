
from src.external.extract import extract_data
from src.external.clean import clean_data
from src.external.validate import validate_data
from src.external.transform import transform_data
from src.external.analyze import analyze_data
from src.external.load import load_data


def run_pipeline():

    # Step 1: Extract data
    raw_df = extract_data()

    # Step 2: Clean data
    cleaned_df = clean_data(raw_df)

    # Step 3: Validate data
    validate_data(cleaned_df)

    # Step 4: Transform data
    transformed_df = transform_data(cleaned_df)

    # Step 5: Analyze data
    summary_df = analyze_data(transformed_df)

    # Step 6: Load data
    load_data(cleaned_df, transformed_df, summary_df)

    print("\nExternal ETL pipeline completed successfully!")


# Execute the pipeline when this file is run directly
if __name__ == "__main__":
    run_pipeline()
