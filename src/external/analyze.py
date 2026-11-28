import pandas as pd


def analyze_data(transformed_df):

    # Create a copy of the transformed dataset
    analysis_df = transformed_df.copy()

    

    # Calculate the total no of the students
    
    total_students = len(analysis_df)
    print(f"Total no of  stuents :{total_students}")
    
    #Calculate the average final grade 
    
    
    average_final_grade = analysis_df["g3"].mean().round(2)
    print(f"Average final grade :{ average_final_grade}")
    
    #Calculate pass and teh fail students 
    
    pass_count = (analysis_df["result"] == "Pass").sum()
    fail_count = (analysis_df["result"] == "Fail").sum()
    
    print(f"Passed students: {pass_count}")
    print(f"Failed students: {fail_count}")
    
    
    #Calculate student performance categories
    performance_count = analysis_df["performance"].value_counts()
    
    print("\n Students performance categories :")
    print(performance_count)    
    
    
    # Calculate average final grade by performance category
    average_by_performance = analysis_df.groupby(
    "performance", observed=False
   )["g3"].mean().round(2)

    print("\nAverage grade by performance category:")
    print(average_by_performance)
    
    # Calculate the final grade statistics 
    highest_grade = analysis_df["g3"].max()
    lowest_grade = analysis_df["g3"].min()
    median_grade = analysis_df["g3"].median()
    
 
    print("\nFinal grade statistics:")
    print(f"Highest grade: {highest_grade}")
    print(f"Lowest grade: {lowest_grade}")
    print(f"Median grade: {median_grade}")
    
     # Calculate average final grade by school
    school_performance = analysis_df.groupby("school")["g3"].mean().round(2)

    print("\nAverage final grade by school:")
    print(school_performance)
         # Create a structured performance summary
    summary_data = {
        "metric": [
            "Total Students",
            "Average Final Grade",
            "Passed Students",
            "Failed Students",
            "Highest Grade",
            "Lowest Grade",
            "Median Grade"
        ],
        "value": [
            total_students,
            average_final_grade,
            pass_count,
            fail_count,
            highest_grade,
            lowest_grade,
            median_grade
        ]
    }

    summary_df = pd.DataFrame(summary_data)

    return summary_df
    