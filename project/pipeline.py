import pandas as pd
import sqlite3
import requests
import io
import gzip
from io import BytesIO
import os

def fetch_data(url, compressed=False):
    print(f"Fetching data from {url}...")
    response = requests.get(url)
    if compressed:
        print("Decompressing data...")
        return gzip.decompress(response.content)
    else:
        return response.content.decode('utf-8')

def save_to_sqlite(df, db_path, table_name):
    print(f"Saving data to {table_name} table in {db_path}...")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create table without auto-incremented primary key
    if table_name == 'library':
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            month TEXT,
            visitors INTEGER
        );
        """)
    elif table_name == 'weather':
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            month TEXT,
            tavg REAL,
            snow REAL,
            prcp REAL,
            wspd REAL
        );
        """)
    
    # Insert data into table
    for row in df.itertuples(index=False):
        if table_name == 'library':
            cursor.execute(f"""
            INSERT INTO {table_name} (month, visitors) VALUES (?, ?)
            """, (row.month, row.visitors))
        elif table_name == 'weather':
            cursor.execute(f"""
            INSERT INTO {table_name} (month, tavg, snow, prcp, wspd) VALUES (?, ?, ?, ?, ?)
            """, (row.month, row.tavg, row.snow, row.prcp, row.wspd))
    
    conn.commit()
    conn.close()


def transform_library_data(data):
    print("Transforming library data...")
    df = pd.read_csv(io.StringIO(data))
    df = df.drop(columns=['YTD'])
    month_columns = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE',
                     'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
    monthly_sums = df[month_columns].sum()
    monthly_data = pd.DataFrame({
        'month': monthly_sums.index.str.title().str[:3],
        'visitors': monthly_sums.values
    })
    return monthly_data

def transform_weather_data(data):
    print("Transforming weather data...")
    selected_columns = [0, 3, 4, 5, 8]
    df = pd.read_csv(BytesIO(data), header=None, usecols=selected_columns)
    df.columns = ['date', 'tavg', 'snow', 'prcp', 'wspd']
    df['date'] = pd.to_datetime(df['date'])
    df_2018 = df[df['date'].dt.year == 2018]
    df_2018 = df_2018.dropna()
    df_2018['month'] = df_2018['date'].dt.strftime('%b')
    monthly_avg = df_2018.groupby('month').mean().reset_index()
    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthly_avg['month'] = pd.Categorical(monthly_avg['month'], categories=months_order, ordered=True)
    monthly_avg = monthly_avg.sort_values('month')
    monthly_avg = monthly_avg.drop(columns=['date'], errors='ignore')
    monthly_avg[['tavg', 'snow', 'prcp', 'wspd']] = monthly_avg[['tavg', 'snow', 'prcp', 'wspd']].round(2)
    return monthly_avg

def main():
    # Ensure the ../data directory exists
    os.makedirs('../data', exist_ok=True)
    
    db_path = '../data/MADE.sqlite'
    
    # Process library data
    library_url = "https://data.cityofchicago.org/api/views/i7zz-iiza/rows.csv"
    library_data = fetch_data(library_url)
    library_df = transform_library_data(library_data)
    save_to_sqlite(library_df, db_path, 'library')
    print("Monthly visitor data for the year 2018 has been saved to SQLite database.")
    
    # Process weather data
    weather_url = "https://bulk.meteostat.net/v2/hourly/72534.csv.gz"
    weather_data = fetch_data(weather_url, compressed=True)
    weather_df = transform_weather_data(weather_data)
    save_to_sqlite(weather_df, db_path, 'weather')
    print("Monthly averaged data for the year 2018 has been saved to SQLite database.")

if __name__ == "__main__":
    main()
