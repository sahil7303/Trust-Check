from . import feature_extractor as fe
import xgboost as xgb
import pickle
import numpy as np
import warnings

# Suppress all warnings
warnings.filterwarnings('ignore')

def get_phishing_status(url):
    # Load the model from the file
    with open('/home/harsh-patel/Desktop/projects/phishing_detection_chrome_extension/scripts/xgboost_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Extract features from the URL
    datapoint = fe.extract_features(url)
    if datapoint is None :
        return 1
    datapoint = datapoint[1:]  # Adjust if necessary

    # Convert datapoint to numpy array and ensure it is numeric
    datapoint = np.array(datapoint, dtype=float).reshape(1, -1)

    # Load the fitted scaler from the file
    try:
        with open('/home/harsh-patel/Desktop/projects/phishing_detection_chrome_extension/scripts/scaler.pkl', 'rb') as f:
            sc = pickle.load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Scaler file not found: {e}")
    except Exception as e:
        raise Exception(f"An error occurred while loading the scaler: {e}")

    # Function to predict a single data point
    def predict_single_data_point(data_point):
        try:
            # Scale the data point using the same scaler
            data_point_scaled = sc.transform(data_point)
            # Predict the class
            prediction = model.predict(data_point_scaled)
            return prediction[0]
        except Exception as e:
            raise Exception(f"An error occurred during prediction: {e}")

    # Scale the datapoint using the loaded scaler
    try:
        datapoint_scaled = sc.transform(datapoint)
    except Exception as e:
        raise Exception(f"An error occurred while scaling the datapoint: {e}")

    # Make predictions
    try:
        prediction = predict_single_data_point(datapoint_scaled)
        return prediction
    except Exception as e:
        raise Exception(f"An error occurred while making the prediction: {e}")