import pandas as pd
import sqlite3
import requests
from io import BytesIO
import gzip

# Download the CSV file from the URL
url = "https://bulk.meteostat.net/v2/hourly/72534.csv.gz"
response = requests.get(url)

# Read the gzip-compressed CSV data
data = gzip.decompress(response.content)

# Specify the column indices to select
selected_columns = [0, 3, 4, 5, 8]

# Convert bytes data to pandas DataFrame, selecting columns by index
df = pd.read_csv(BytesIO(data), header=None, usecols=selected_columns)

# Assign column names
df.columns = ['date', 'tavg', 'snow', 'prcp', 'wspd']

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Filter rows where year is 2018
df_2018 = df[df['date'].dt.year == 2018]

# Drop rows with any null values
df_2018 = df_2018.dropna()

# Group by month and calculate mean
df_2018['month'] = df_2018['date'].dt.strftime('%b')
monthly_avg = df_2018.groupby('month').mean().reset_index()
print(monthly_avg)

# Reorder the months
months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_avg['month'] = pd.Categorical(monthly_avg['month'], categories=months_order, ordered=True)
monthly_avg = monthly_avg.sort_values('month')

# Remove the 'date' field from the final DataFrame
monthly_avg = monthly_avg.drop(columns=['date'], errors='ignore')

# Format the specified columns to two decimal places
monthly_avg[['tavg', 'snow', 'prcp', 'wspd']] = monthly_avg[['tavg', 'snow', 'prcp', 'wspd']].round(2)

# Connect to SQLite database
conn = sqlite3.connect('weather_data.db')

# Save DataFrame to SQLite database
monthly_avg.to_sql('monthly_weather', conn, if_exists='replace', index=False)

# Close database connection
conn.close()

print("Monthly averaged data for the year 2018 has been saved to SQLite database.")
