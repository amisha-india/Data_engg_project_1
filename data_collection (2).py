import pandas as pd

def collect_data(file_path):
    df = pd.read_csv("C:/Users/amarj/OneDrive/Desktop/Hexaware_Projects/Energy_Project/Week-2/energy_consumption_data.csv")
    return df