


"""


Helper functions to load and save CSV data.



This contains a helper function for loading and saving CSV files.

"""


# Import csv
import csv

# Import Path from pathlib
from pathlib import Path 



def load_csv(csvpath):

    """
    Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """

    # Reference the file path the user inputted in app.py
    with open(csvpath, "r") as csvfile:

        # Create an empty list to append filtered data to
        data = []

        # Read the list of all bank loans
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the csv Header
        next(csvreader)

        # Read the csv data
        for row in csvreader:

            # Append rows of qualifying loans to the data list container
            data.append(row)


    # Return the list of qualifying bank loans        
    return data




# Create a new function called save_csv to export a csv file
def save_csv(data):
    bank_data = data


# Create headers for the export file
    header = ["Lender" , "Max Loan", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]


# Create output path for csv file
    csvexportpath = Path("qualifying_loans.csv")


# Open and write the csv file
    with open(csvexportpath, "w", newline = '') as csvfile:

        # Write the csv
        csvwriter = csv.writer(csvfile, delimiter = ",")

        # Write the headers to the csv
        csvwriter.writerow(header)

        # Write the rows of qualifying loans to the csv
        for loan in bank_data:
            csvwriter.writerow(loan)

    # Return the saved csv file
    return data