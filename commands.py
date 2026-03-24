import random
import os
import pandas as pd


def csv_column_randomizer(csv_file: str = "main_tracks.csv",
                          number_of_items: int = 1,
                          prevent_duplicates: bool = True,
                          return_string: bool = False) -> list | str:
    """Randomly selects all items from a column of a CSV file, allowing for duplicate selection and returning them as a list or a formatted string.."""

    try:
        if not os.path.exists(csv_file):
            if return_string:
                return f"Error: File '{csv_file}' does not exist."
            return []
      
        csv_data = pd.read_csv(csv_file)

        # Additional checks if needed...
        # if csv_data.empty:
        #     if return_string:
        #         return f"Error: File '{csv_file}' is empty."
        #     return []
      
        # Logic
        csv_selection = []

        if number_of_items > len(csv_data.columns) and prevent_duplicates:
            if return_string:
                return f"Error: Cannot select {number_of_items} unique items from {len(csv_data.columns)} available."
            return []

        i = 0
        while i < number_of_items:
            random_stage = csv_data.columns[random.randint(
                0, len(csv_data.columns) - 1)]
            csv_selection.append(random_stage)
            if prevent_duplicates:
                csv_data.drop(str(random_stage), axis=1)
            i += 1
        if return_string:
            return f"🎲 **Random Track Selection:**\n\n{', '.join(csv_selection)}"
        return csv_selection

    except pd.errors.EmptyDataError:
        if return_string:
            return f"Error: File '{csv_file}' is empty."
        return []
    except pd.errors.ParserError:
        if return_string:
            return f"Error: File '{csv_file}' has invalid CSV format."
        return []
    except Exception as e:
        if return_string:
            return f"Error reading CSV file: {str(e)}"
        print(f"Error reading CSV file: {str(e)}")
        return []


testing = csv_column_randomizer(
            csv_file='main_tracks.csv',
            number_of_items=12,
            prevent_duplicates=False,
            return_string=True
        )
print(testing)
