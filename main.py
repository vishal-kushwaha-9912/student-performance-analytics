from src.pipeline import run_pipeline as run_original_pipeline
from src.external.pipeline import run_pipeline as run_external_pipeline


def display_menu():

    print("\n====================================")
    print("   STUDENT PERFORMANCE ANALYTICS")
    print("====================================")

    print("1. Run Original ETL Pipeline")
    print("2. Run External ETL Pipeline")
    print("3. Exit")

    print("====================================")



def main():

    while True:

        display_menu()

        choice = input("Enter your choice (1-3): ")

        if choice == "1":

            print("\nRunning Original ETL Pipeline...\n")
            run_original_pipeline()

        elif choice == "2":

            print("\nRunning External ETL Pipeline...\n")
            run_external_pipeline()

        elif choice == "3":

            print("\nThank you for using Student Performance Analytics!")
            break

        else:

            print("\nInvalid choice! Please select 1, 2, or 3.")
            
            
if __name__ == "__main__":    
    main()
