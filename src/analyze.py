
import pandas as pd


def analyze_data(transformed_df):

    # 1. Calculate key performance metrics
    average_marks = transformed_df["marks"].mean()
    average_study_hours = transformed_df["study_hours"].mean()
    average_attendance = transformed_df["attendance"].mean()

    highest_marks = transformed_df["marks"].max()
    lowest_marks = transformed_df["marks"].min()

    # 2. Display overall metrics
    print("\n========== STUDENT PERFORMANCE ANALYSIS ==========")

    print(f"Total students: {len(transformed_df)}")
    print(f"Average marks: {average_marks:.2f}")
    print(f"Average study hours: {average_study_hours:.2f}")
    print(f"Average attendance: {average_attendance:.2f}%")
    print(f"Highest marks: {highest_marks}")
    print(f"Lowest marks: {lowest_marks}")

    # 3. Create performance summary
    performance_summary = (
        transformed_df
        .groupby("performance", observed=False)
        .agg(
            student_count=("student_id", "count"),
            average_marks=("marks", "mean"),
            highest_marks=("marks", "max"),
            lowest_marks=("marks", "min")
        )
        .reset_index()
    )

    performance_summary["average_marks"] = (
        performance_summary["average_marks"].round(2)
    )

    print("\n========== PERFORMANCE SUMMARY ==========")
    print(performance_summary)

    # 4. Calculate correlation
    numeric_columns = [
        "study_hours",
        "attendance",
        "sleep_hours",
        "marks"
    ]

    correlation = transformed_df[numeric_columns].corr()

    print("\n========== CORRELATION MATRIX ==========")
    print(correlation.round(2))

    print("\nData analysis successful!")

    return performance_summary


# Test the analysis module
if __name__ == "__main__":

    from src.extract import extract_data
    from src.clean import clean_data
    from src.transform import transform_data

    raw_df = extract_data()

    cleaned_df = clean_data(raw_df)

    transformed_df = transform_data(cleaned_df)

    summary_df = analyze_data(transformed_df)
