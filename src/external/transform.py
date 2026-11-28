import pandas as pd


def transform_data(df):

    # create a copy of the clean datasets
    transformed_df = df.copy()

    # Calculate avg students grade

    transformed_df["average_grade"] = transformed_df[
        [ "g1", "g2", "g3"]
        ].mean(axis=1).round(2)


    # classsify students as pass or fail
    transformed_df["result"] = transformed_df["g3"].apply(
        lambda grade: "Pass" if grade >= 10 else "Fail"
    )

    # create student performance categeories

    transformed_df["performance"] = pd.cut(
        transformed_df["g3"],
        bins=[-1, 9, 12, 15, 20],
       labels=[
    "Needs Improvement",
    "Average",
    "Good",
    "Excellent"
]
    )

    print("External dataset transformation successful !")

    return transformed_df
