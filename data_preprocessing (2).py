import pandas as pd
import pyodbc
def preprocess_data(df):
    df.ffill(inplace=True)
    df['energy_consumed_normalized'] = (df['energy_consumed'] - df['energy_consumed'].min()) / (
                df['energy_consumed'].max() - df['energy_consumed'].min())
    return df

def detect_anomalies(df, threshold=0.8):
    anomalies = df[df['energy_consumed'] > 10 ]
    anomalies.to_csv('C:/Users/amarj/OneDrive/Desktop/Hexaware_Projects/Energy_Project/Week-2/energy_consumption_data.csv', index=False)

    return anomalies

def store_anomalies_in_db(anomalies):

    # SQL Server connection string
    conn_str = (
        'DRIVER={SQL Server};'
        'SERVER=Amarj;'
        'DATABASE=EnergyProjectDB'
    )

    # Connect to the SQL Server database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Insert each row of anomalies into the database
    for index, row in anomalies.iterrows():
        cursor.execute("""
            INSERT INTO EnergyAnomalies (device_id, timestamp, energy_consumed, energy_consumed_normalized)
            VALUES (?, ?, ?, ?)
        """, row['device_id'], row['timestamp'], row['energy_consumed'], row['energy_consumed_normalized'])

    # Commit the transaction and close the connection
    conn.commit()
    cursor.close()
    conn.close()