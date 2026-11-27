
def validate_data(df):
    """Validate the quality of the cleaned student dataset."""

    required_columns = [
        "student_id",
        "name",
        "study_hours",
        "attendance",
        "sleep_hours",
        "marks"
    ]

    print("\n========== DATA QUALITY VALIDATION ==========")

    # Check 1: Required columns
    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    print("1. Required columns: PASSED")

    # Check 2: Unique student IDs
    if df["student_id"].duplicated().any():
        raise ValueError("Duplicate student IDs found!")

    print("2. Unique student IDs: PASSED")

    # Check 3: Marks between 0 and 100
    if not df["marks"].dropna().between(0, 100).all():
        raise ValueError("Marks must be between 0 and 100!")

    print("3. Marks range (0-100): PASSED")

    # Check 4: Attendance between 0 and 100
    if not df["attendance"].dropna().between(0, 100).all():
        raise ValueError("Attendance must be between 0 and 100!")

    print("4. Attendance range (0-100): PASSED")

    # Check 5: Study hours cannot be negative
    if not df["study_hours"].dropna().ge(0).all():
        raise ValueError("Study hours cannot be negative!")

    print("5. Study hours: PASSED")

    # Check 6: Sleep hours cannot be negative
    if not df["sleep_hours"].dropna().ge(0).all():
        raise ValueError("Sleep hours cannot be negative!")

    print("6. Sleep hours: PASSED")

    print("\nDATA QUALITY VALIDATION SUCCESSFUL!")

    return True

if __name__ == "__main__":
    from src.extract import extract_data
    from src.clean import clean_data

    raw_df = extract_data()
    cleaned_df = clean_data(raw_df)

    validate_data(cleaned_df)
