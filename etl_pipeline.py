# Import required libraries
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler

# ----------------------------
# EXTRACT STEP
# ----------------------------

print("Loading dataset...")

data = pd.read_csv("data/sample_data.csv")

print("\nOriginal Dataset:")
print(data)

# ----------------------------
# TRANSFORM STEP
# ----------------------------

print("\nHandling missing values...")

# Fill missing numerical values
num_imputer = SimpleImputer(strategy='mean')

data[['Age', 'Salary']] = num_imputer.fit_transform(
    data[['Age', 'Salary']]
)

# Fill missing categorical values
cat_imputer = SimpleImputer(strategy='most_frequent')

data[['Department']] = cat_imputer.fit_transform(
    data[['Department']]
)

print("\nEncoding categorical values...")

# Encode text values
encoder = LabelEncoder()

data['Department'] = encoder.fit_transform(
    data['Department']
)

print("\nScaling numerical values...")

# Scale numeric columns
scaler = StandardScaler()

data[['Age', 'Salary']] = scaler.fit_transform(
    data[['Age', 'Salary']]
)

# ----------------------------
# LOAD STEP
# ----------------------------

output_path = "data/processed_data.csv"

data.to_csv(output_path, index=False)

print("\nProcessed Dataset:")
print(data)

print(f"\nProcessed file saved at: {output_path}")


import matplotlib.pyplot as plt

# Create bar chart
data.plot(x='Name', y='Salary', kind='bar')

plt.title("Employee Salary Chart")
plt.xlabel("Employee Name")
plt.ylabel("Salary")

plt.show()

data.to_csv("data/processed_data.csv", index=False)

print("\nProcessed data saved successfully!")
