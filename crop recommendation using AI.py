import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


data = pd.read_csv('crop_data.csv')


X = data[['soil_type', 'temperature', 'humidity', 'rainfall']]
y = data['crop']


X = pd.get_dummies(X)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

def predict_crop(soil_type, temperature, humidity, rainfall):
    input_data = pd.DataFrame({
        'soil_type': [soil_type],
        'temperature': [temperature],
        'humidity': [humidity],
        'rainfall': [rainfall]
    })
    input_data = pd.get_dummies(input_data)
    crop_prediction = model.predict(input_data)
    return crop_prediction[0]


predicted_crop = predict_crop('sandy', 25, 60, 100)
print("Predicted Crop:", predicted_crop)
