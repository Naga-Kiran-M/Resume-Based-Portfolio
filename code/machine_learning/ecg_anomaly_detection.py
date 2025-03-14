# Anomaly Detection in ECG Data using Autoencoders

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from sklearn.preprocessing import MinMaxScaler

# Load ECG Data
data = np.loadtxt("assets/datasets/ecg_data.csv", delimiter=',')
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)

# Split Data into Normal and Anomalous Sets
normal_data = data_scaled[:8000]
anomalous_data = data_scaled[8000:]

# Define Autoencoder Model
input_dim = normal_data.shape[1]
input_layer = Input(shape=(input_dim,))
encoded = Dense(64, activation='relu')(input_layer)
encoded = Dense(32, activation='relu')(encoded)
decoded = Dense(64, activation='relu')(encoded)
decoded = Dense(input_dim, activation='sigmoid')(decoded)

autoencoder = Model(input_layer, decoded)
autoencoder.compile(optimizer='adam', loss='mse')

# Train Autoencoder on Normal Data
autoencoder.fit(normal_data, normal_data, epochs=50, batch_size=32, validation_split=0.2)

# Save Model
autoencoder.save("assets/models/ecg_autoencoder.h5")
