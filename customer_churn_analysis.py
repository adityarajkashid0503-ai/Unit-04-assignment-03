import pandas as pd
import numpy as np

# Sample data (stands in for customer_churn.csv)
df = pd.DataFrame({
    'customerID': ['001', '002', '003', '004', '004'],
    'tenure': [1, 34, 2, 45, 45],
    'TotalCharges': ['29.85', '1889.5', ' ', '1840.75', '1840.75'],
    'Churn': ['No', 'No', 'Yes', 'No', 'No']
})
print("Dataset loaded successfully!\n")

print("Shape of the dataset:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].mean())
df.drop_duplicates(inplace=True)

print("\nAfter cleaning:\n", df)
print("Shape now:", df.shape)
