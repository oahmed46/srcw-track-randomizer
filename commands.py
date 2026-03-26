import random
import os  # default module
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

MAIN_COURSES_CSV = os.getenv("MAIN_COURSES_CSV")


def validate_csv_file(csv_file: str) -> bool:
    """Validates that the specified CSV file exists and is readable."""
    if not os.path.exists(csv_file):
        print(f"Error: File '{csv_file}' does not exist.")
        return False
    try:
        pd.read_csv(csv_file, nrows=1)  # Try reading just the header
        return True
    except pd.errors.EmptyDataError:
        print(f"Error: File '{csv_file}' is empty.")
        return False
    except pd.errors.ParserError:
        print(f"Error: File '{csv_file}' has invalid CSV format.")
        return False
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}")
        return False


def csv_column_randomizer(csv_file: str = MAIN_COURSES_CSV,
                          number_of_items: int = 1,
                          prevent_duplicates: bool = True,
                          return_string: bool = True) -> list | str:
    """Randomly selects all items from a column of a CSV file, allowing for duplicate selection and returning them as a list or a formatted string."""
    # Validate the CSV file before attempting to read it
    if not validate_csv_file(csv_file):
        if return_string:
            return "Error: Invalid CSV file."
        if not return_string:
            return []
    csv_columns = pd.read_csv(csv_file).columns.tolist()
    csv_selection = []
    if number_of_items > len(csv_columns) and prevent_duplicates:
        if return_string:
            return f"Error: Cannot select {number_of_items} unique items from {len(csv_columns)} available."
        return []
    i = 0
    while i < number_of_items:
        random_stage = csv_columns[random.randint(
            0, len(csv_columns) - 1)]
        csv_selection.append(random_stage)
        if prevent_duplicates:
            csv_columns.remove(str(random_stage))
        i += 1
    if return_string:
        return "\n".join(f"- {course}" for course in csv_selection)
    return csv_selection


def csv_column_length(csv_file: str = MAIN_COURSES_CSV) -> int:
    """Returns the number of columns in a CSV file."""
    if not validate_csv_file(csv_file):
        return 0
    csv_data = pd.read_csv(csv_file)
    return len(csv_data.columns)


# Testing the functions
# testing_randomizer = csv_column_randomizer(number_of_items=12)
# print(testing_randomizer)

# testing_validate = validate_csv_file(MAIN_COURSES_CSV)
# print(testing_validate)

# testing_length = csv_column_length(MAIN_COURSES_CSV)
# print(testing_length)
