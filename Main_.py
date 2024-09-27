from data_collection import collect_data
from data_preprocessing import preprocess_data,detect_anomalies
from feature_engineering import feature_engineering,save_features_to_csv


def main():
    # Path to your CSV file
    file_path = "C:/Users/amarj/OneDrive/Desktop/Hexaware_Projects/Energy_Project/Week-2/energy_consumption_data.csv"

    # Step 1: Collect data
    df = collect_data(file_path)

    # Step 2: Preprocess the data
    df = preprocess_data(df)

    anomalies=detect_anomalies(df)

    print("Anomalies detected and stored in the SQL Server database")

    # Step 3: Perform feature engineering
    df = feature_engineering(df)
    save_features_to_csv(df, "C:/Users/amarj/OneDrive/Desktop/Hexaware_Projects/Energy_Project/Week-2/energy_consumption_data.csv")

    # Display the final DataFrame
    print(df.head())


if __name__ == "__main__":
    main()