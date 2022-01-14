# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv

# Import Path from pathlib
from pathlib import Path 


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
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

        csvwriter = csv.writer(csvfile, delimiter = ",")
        csvwriter.writerow(header)

        for loan in bank_data:
            csvwriter.writerow(loan)

    return data