import pandas as pd


def feature_engineering(df):
    # Example feature engineering
    df['hour_of_day'] = pd.to_datetime(df['timestamp'], format='%d-%m-%Y %H:%M').dt.hour
    df['is_peak_hour'] = df['hour_of_day'].apply(
        lambda x: 1 if 18 <= x <= 23 else 0)
    return df


def save_features_to_csv(df, output_file):
    try:
        df.to_csv(output_file, index=False)
        print(f"Feature-engineered data saved to {output_file}")
    except Exception as e:
        print(f"Error saving features to CSV: {e}")