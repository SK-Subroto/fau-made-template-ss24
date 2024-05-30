import pandas as pd
import sqlite3
import requests
import io

# Download the CSV file from the URL
url = "https://data.cityofchicago.org/api/views/i7zz-iiza/rows.csv"
response = requests.get(url)
data = response.content.decode('utf-8')

# Read the CSV data into a pandas DataFrame
df = pd.read_csv(io.StringIO(data))

# Drop the 'YTD' column
df = df.drop(columns=['YTD'])

# Define the columns for months
month_columns = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE',
                 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']

# Sum the visitor values for each month
monthly_sums = df[month_columns].sum()

# Create a new DataFrame with 'month' and 'visitors' columns
monthly_data = pd.DataFrame({
    'month': monthly_sums.index.str.title().str[:3],
    'visitors': monthly_sums.values
})

# Connect to SQLite database
conn = sqlite3.connect('library_visitors.db')

# Save the new DataFrame to SQLite database
monthly_data.to_sql('monthly_visitors', conn, if_exists='replace', index=False)

# Close the database connection
conn.close()

print("Monthly visitor data has been saved to SQLite database.")
