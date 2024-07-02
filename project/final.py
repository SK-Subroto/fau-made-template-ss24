import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def read_from_sqlite(db_path, table_name):
    print(f"Reading data from {table_name} table in {db_path}...")
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df

def categorize_season(month):
    if month in ['Dec', 'Jan', 'Feb']:
        return 'Winter'
    elif month in ['Mar', 'Apr', 'May']:
        return 'Spring'
    elif month in ['Jun', 'Jul', 'Aug']:
        return 'Summer'
    elif month in ['Sep', 'Oct', 'Nov']:
        return 'Fall'
    else:
        return 'Unknown'

def plot_season_wise_library_visitors(library_df):
    print("Generating season-wise violin plots for library visitors...")
    
    library_df['season'] = library_df['month'].apply(categorize_season)
    
    plt.figure(figsize=(10, 6))
    sns.violinplot(x='season', y='visitors', data=library_df, palette='muted')
    plt.xlabel('Season')
    plt.ylabel('Number of Visitors')
    plt.title('Season-wise Library Visitors (2018)')
    plt.show()

def main():
    db_path = '../data/MADE.sqlite'
    
    # Read data from SQLite database
    library_df = read_from_sqlite(db_path, 'library')
    
    # Generate season-wise violin plots for library visitors
    plot_season_wise_library_visitors(library_df)

if __name__ == "__main__":
    main()
