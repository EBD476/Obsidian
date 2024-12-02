import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Function to load GPS data from a CSV file
def load_gps_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Function to preprocess the data
def preprocess_data(df):
    # Convert timestamps to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Sort by timestamp
    df = df.sort_values('timestamp')
    
    # Calculate time difference in seconds between consecutive points
    df['time_diff'] = df['timestamp'].diff().dt.total_seconds().fillna(0)
    
    # Calculate distance traveled between consecutive points (in meters)
    df['distance'] = np.sqrt((df['latitude'].diff() * 111320) ** 2 + (df['longitude'].diff() * 111320 * np.cos(np.radians(df['latitude'])) ** 2) ** 2).fillna(0)
    
    return df

# Function to extract features for anomaly detection
def extract_features(df):
    features = pd.DataFrame()
    features['total_distance'] = [df['distance'].sum()]
    features['average_speed'] = [df['distance'].sum() / df['time_diff'].sum()] if df['time_diff'].sum() > 0 else [0]
    features['num_stops'] = [(df['time_diff'] > 300).sum()]  # Count stops longer than 5 minutes (300 seconds)
    
    return features

# Function to detect anomalies using Isolation Forest
def detect_anomalies(features):
    model = IsolationForest(contamination=0.1)  # Adjust contamination based on expected anomaly rate
    model.fit(features)
    
    # Predict anomalies (-1 for anomaly, 1 for normal)
    predictions = model.predict(features)
    
    return predictions

# Main execution
if __name__ == "__main__":
    # Load your GPS data here (CSV format with columns: timestamp, latitude, longitude)
    gps_file_path = 'path_to_your_gps_data.csv'  # Replace with your CSV file path
    gps_data = load_gps_data(gps_file_path)

    # Preprocess the data
    processed_data = preprocess_data(gps_data)

    # Extract features for anomaly detection
    features = extract_features(processed_data)

    # Detect anomalies
    anomalies = detect_anomalies(features)

    # Output results
    if anomalies[0] == -1:
        print("Anomaly detected: Potential fake route.")
    else:
        print("No anomalies detected: Route appears legitimate.")

    # Optional: Visualize the route and anomalies (if you have multiple routes)
    plt.figure(figsize=(10, 6))
    plt.scatter(processed_data['longitude'], processed_data['latitude'], c=anomalies, cmap='coolwarm', marker='o')
    plt.title('Street Sweeper Route with Anomalies')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.colorbar(label='Anomaly Status (-1: Anomaly, 1: Normal)')
    plt.show()
