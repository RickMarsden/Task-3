import pandas as pd
# Read the dataset into a pandas dataframe
df = pd.read_csv('dataset.csv')
# Find the missing values in the dataframe
mask = df.isnull()

# Select the missing values and replace them with 0
df[mask] = 0
# Replace missing values with 0
df.fillna(0, inplace=True)