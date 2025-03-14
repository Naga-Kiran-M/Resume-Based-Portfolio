# Real-Time Air Quality Prediction using LSTM

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

# Step 1: Load and Preprocess Dataset
df = pd.read_csv("assets/datasets/air_quality_data.csv")
df.fillna(df.mean(), inplace=True)

# Select relevant columns
features = ['Temperature', 'Humidity', 'PM2.5', 'NO2']
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(df[features])

# Step 2: Create Time-Series Data
def create_sequences(data, time_steps=10):
    X, y = [], []
    for i in range(len(data) - time_steps):
        X.append(data[i:i + time_steps])
        y.append(data[i + time_steps, -1])  # Predicting AQI
    return np.array(X), np.array(y)

time_steps = 10
X, y = create_sequences(data_scaled, time_steps)

# Split into Train & Test
split = int(0.8 * len(X))
X_train, X_test, y_train, y_test = X[:split], X[split:], y[:split], y[split:]

# Step 3: Build LSTM Model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(time_steps, len(features))),
    LSTM(50),
    Dense(25, activation='relu'),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

# Step 4: Evaluate Model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.4f}")

# Step 5: Plot Predictions
plt.figure(figsize=(8, 6))
plt.plot(y_test, label="Actual AQI")
plt.plot(y_pred, label="Predicted AQI", linestyle="dashed")
plt.xlabel("Time Steps")
plt.ylabel("AQI Level")
plt.legend()
plt.show()
