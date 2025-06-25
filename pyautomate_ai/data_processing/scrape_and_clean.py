import requests
import pandas as pd
from bs4 import BeautifulSoup
import psycopg2
import os

def scrape_table(url, table_index=0):
    print(f"Scraping table from {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table')
    df = pd.read_html(str(tables[table_index]))[0]
    return df

def clean_data(df):
    print("Cleaning data...")
    # Example: drop rows with any missing values
    df_clean = df.dropna()
    return df_clean

def save_to_postgres(df, table_name, db_url):
    print(f"Saving DataFrame to PostgreSQL table '{table_name}'...")
    import sqlalchemy
    engine = sqlalchemy.create_engine(db_url)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print("Saved!")

def main():
    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
    df = scrape_table(url)
    print("Raw scraped data:")
    print(df.head())
    df_clean = clean_data(df)
    print("\nCleaned data:")
    print(df_clean.head())
    # Uncomment and set your DB URL to save to PostgreSQL
    # db_url = 'postgresql://user:password@localhost:5432/yourdb'
    # save_to_postgres(df_clean, 'gdp_table', db_url)

if __name__ == '__main__':
    main() 