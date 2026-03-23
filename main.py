import random
import pandas as pd


def csv_column_randomizer(csv_file: str,
                          number_of_columns: int = 1,
                          prevent_duplicates: bool = True) -> str:
    """Randomly selects columns from a CSV file."""
    csv_selection = []
    csv_data = pd.read_csv(csv_file)

    i = 0
    while i < number_of_columns:
        random_stage = csv_data.columns[random.randint(
            0, len(csv_data.columns) - 1)]
        csv_selection.append(random_stage)
        if prevent_duplicates:
            csv_data.drop(str(random_stage), axis=1)
        i += 1
    return f"Selected Track(s):\n{'\n'.join(csv_selection)}"


SELECTION = csv_column_randomizer("main_tracks.csv", 12, True)
print(SELECTION)
