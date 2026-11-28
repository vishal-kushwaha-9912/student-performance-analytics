import pandas as pd 


def validate_data(df):

    # Define required columns
    required_columns = [
        "school", "sex", "age", "address", "famsize",
        "pstatus", "medu", "fedu", "mjob", "fjob",
        "reason", "guardian", "traveltime", "studytime",
        "failures", "schoolsup", "famsup", "paid",
        "activities", "nursery", "higher", "internet",
        "romantic", "famrel", "freetime", "goout",
        "dalc", "walc", "health", "absences",
        "g1", "g2", "g3"
    ]    
    
        # Check for missing required columns
    missing_columns = set(required_columns) - set(df.columns)

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
        # Define columns that must contain numeric values
    numeric_columns = [
        "age", "medu", "fedu", "traveltime", "studytime",
        "failures", "famrel", "freetime", "goout",
        "dalc", "walc", "health", "absences",
        "g1", "g2", "g3"
    ]

    # Check numeric data types
    for column in numeric_columns:
        if not pd.api.types.is_numeric_dtype(df[column]):
            raise ValueError(f"Column '{column}' must contain numeric values")
        
            # Validate student grade ranges
    grade_columns = ["g1", "g2", "g3"]

    for column in grade_columns:
        if not df[column].between(0, 20).all():
            raise ValueError(
                f"Invalid grades found in column '{column}'. Expected range: 0–20"
            )
            
                # Validate student age
    if not df["age"].between(15, 22).all():
        raise ValueError("Invalid student age found. Expected range: 15–22")
        # Validate ordinal and rating columns
    ordinal_ranges = {
        "medu": (0, 4),
        "fedu": (0, 4),
        "traveltime": (1, 4),
        "studytime": (1, 4),
        "failures": (0, 3),
        "famrel": (1, 5),
        "freetime": (1, 5),
        "goout": (1, 5),
        "dalc": (1, 5),
        "walc": (1, 5),
        "health": (1, 5)
    }

    for column, (minimum, maximum) in ordinal_ranges.items():
        if not df[column].between(minimum, maximum).all():
            raise ValueError(
                f"Invalid values in '{column}'. Expected range: {minimum}–{maximum}"
            )
                # Validate student absences
    if (df["absences"] < 0).any():
        raise ValueError("Negative absence values found")
        print("External dataset validation successful!")

    return True