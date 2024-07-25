import feature_extractor as fe
import xgboost as xgb
import pickle



model=None
# Load the model from the file
with open('/home/harsh-patel/Desktop/projects/phishing_detection_chrome_extension/scripts/xgboost_model.pkl', 'rb') as file:
    model = pickle.load(file)

url="https://www.instagram.com/"

datapoint = fe.extract_features(url)

# Load the fitted scaler from the file
with open('/home/harsh-patel/Desktop/projects/phishing_detection_chrome_extension/scripts/scaler.pkl', 'rb') as f:
    sc = pickle.load(f)

from sklearn.preprocessing import StandardScaler

# Function to predict a single data point
def predict_single_data_point(data_point):
    # Assuming data_point is a list or array of the same length as a single row of X
    # Scale the data point using the same scaler
    data_point_scaled = sc.transform([data_point])
    # Predict the class
    prediction = model.predict(data_point_scaled)
    return prediction[0]





# Make predictions
predictions = model.predict(datapoint)
print(predictions)