import pandas as pd


def load(path: str):

    """
    Loads a CSV file and returns a DataFrame.

    :param path: The path to the CSV file.
    :return: DataFrame containing the CSV data.
    """
    try:
        csv_file = pd.read_csv(path)
        csv_dim = csv_file.shape
        print(f'Loading dataset of dimensions {csv_dim}')
        return csv_file

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: File '{path}' is empty.")
    except pd.errors.ParserError:
        print(f"Error: File '{path}' is corrupted or has invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
