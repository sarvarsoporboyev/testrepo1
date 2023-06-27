import glob
import pandas as pd
from datetime import datetime

## Imports

# Import any additional libraries you may need here.


## Extract

### JSON Extract Function

# This function will extract JSON files.
def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process)
    return dataframe


## Extract Function

# Define the extract function that finds JSON file `bank_market_cap_1.json` and calls the function created above to extract data from them.
# Store the data in a pandas dataframe. Use the following list for the columns.

columns = ['Name', 'Market Cap (US$ Billion)']

def extract():
    json_files = glob.glob('bank_market_cap_*.json')
    dataframes = []
    for file in json_files:
        df = extract_from_json(file)
        dataframes.append(df)
    extracted_data = pd.concat(dataframes, ignore_index=True)
    return extracted_data[columns]


## Question 1

# Load the file exchange_rates.csv as a dataframe and find the exchange rate for British pounds with the symbol GBP.
# Store it in the variable exchange_rate.
# Hint: set the parameter index_col to 0.

exchange_rates = pd.read_csv('exchange_rates.csv', index_col=0)
exchange_rate = exchange_rates.loc['GBP', 'Exchange Rate']


## Transform

# Using exchange_rate and the exchange_rates.csv file, find the exchange rate of USD to GBP.
# Write a transform function that:
# 1. Changes the 'Market Cap (US$ Billion)' column from USD to GBP
# 2. Rounds the 'Market Cap (US$ Billion)' column to 3 decimal places
# 3. Rename 'Market Cap (US$ Billion)' to 'Market Cap (GBP$ Billion)'

def transform(dataframe, exchange_rate):
    dataframe['Market Cap (US$ Billion)'] = dataframe['Market Cap (US$ Billion)'] * exchange_rate
    dataframe['Market Cap (US$ Billion)'] = dataframe['Market Cap (US$ Billion)'].round(3)
    dataframe.rename(columns={'Market Cap (US$ Billion)': 'Market Cap (GBP$ Billion)'}, inplace=True)
    return dataframe


## Load

# Create a function that takes a dataframe and loads it to a csv named 'bank_market_cap_gbp.csv'.
# Make sure to set index to False.

def load(dataframe):
    dataframe.to_csv('bank_market_cap_gbp.csv', index=False)


## Logging Function

# Write the logging function log to log your data.

def log(message):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'[{current_time}] {message}')


## Running the ETL Process

# Log the process accordingly using the following "ETL Job Started" and "Extract phase Started"

log("ETL Job Started")
log("Extract phase Started")

## Extract
# Question 2: Use the function extract, and print the first 5 rows

extracted_data = extract()
print(extracted_data.head(5))

log("Extract phase Ended")

## Transform

# Log "Transform phase Started"

log("Transform phase Started")

# Question 3: Use the function transform and print the first 5 rows of the output

transformed_data = transform(extracted_data, exchange_rate)
print(transformed_data.head(5))

log("Transform phase Ended")

## Load

# Log "Load phase Started"

log("Load phase Started")

# Call the load function

load(transformed_data)

log("Load phase Ended")
