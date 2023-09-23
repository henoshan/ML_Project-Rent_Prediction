# -*- coding: utf-8 -*-
"""ML_Project-Rent_Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12_5S-jf2akktgVq7VBiVIgC0zNIm1c41

# **1. Import Necessary Libraries**


1.   Pandas
2.   NumPy
3. Scikit Learn
4. SeaBorn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

"""# **2. Load and Explore the Dataset**"""

from google.colab import files
uploaded = files.upload()

# Load the dataset
df = pd.read_csv('House_Rent_Dataset.csv')

# Display the first few rows
print(df.head())

# Get basic statistics of numerical columns
print(df.describe())

"""# **3. Data Preprocessing**"""

# Check for missing values
print(df.isnull().sum())

"""So, there is no missing data in the data set. So, we can go futhur to the next step.

# **4. Data Visualization**
"""

# Pair plot for all numerical features
numerical_features = ['Size', 'BHK', 'Bathroom', 'Rent']
sns.pairplot(df[numerical_features])
plt.show()

"""We are able to identify the the existence of outliers."""

# Correlation heatmap for all numerical features
correlation_matrix = df[numerical_features].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

"""# **5. Split the Data into Training and Testing Sets**"""

X = df[['Size', 'BHK', 'Bathroom']]  # Features
y = df['Rent']  # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""# **6. Create and Train the Linear Regression Model**"""

model = LinearRegression()
model.fit(X_train, y_train)

"""# **7. Make Predictions**"""

# Testing data set is applied here to test the model
y_pred = model.predict(X_test)

"""# **8. Evaluate the Model**"""

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

"""# **9. Visualize the Regression Line**"""

plt.scatter(X_test['Size'], y_test, label='Data Points')
plt.plot(X_test['Size'], y_pred, color='red', linewidth=3, label='Regression Line')
plt.xlabel('Size (sq ft)')
plt.ylabel('Rent ($)')
plt.title('Rent Prediction based on Size')
plt.legend()
plt.show()

plt.scatter(X_test['BHK'], y_test, label='Data Points')
plt.plot(X_test['BHK'], y_pred, color='red', linewidth=3, label='Regression Line')
plt.xlabel('BHK')
plt.ylabel('Rent ($)')
plt.title('Rent Prediction based on BHK')
plt.legend()
plt.show()

# Visualize 'Bathroom' vs. 'Rent'
plt.scatter(X_test['Bathroom'], y_test, label='Data Points')
plt.plot(X_test['Bathroom'], y_pred, color='red', linewidth=3, label='Regression Line')
plt.xlabel('Bathroom')
plt.ylabel('Rent ($)')
plt.title('Rent Prediction based on Bathroom')
plt.legend()
plt.show()

"""# **10. Make Predictions on New Data**

You can use the trained model to make predictions on new data by passing the new data to the `model.predict()` function.
"""

# Input feature values for multiple properties
new_data_points = [
    [1000, 2, 1],
    [1100, 3, 2],
    [1200, 2, 2],
    [1300, 4, 2]
]

# Predict the rents for all properties in the list
predicted_rents = model.predict(new_data_points)

# Print the predictions for each property
for i, rent in enumerate(predicted_rents):
    print(f"Predicted Rent for Property {i+1}: ${rent:.2f}")