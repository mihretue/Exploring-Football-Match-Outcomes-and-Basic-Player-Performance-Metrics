import pandas as pd


data = pd.read_csv('E1.csv')

# Drop columns from index 25 to the end
data = data.drop(data.columns[24:], axis=1)
Refined_data = data.drop(data.columns[0:3], axis=1)

# print(data)

Refined_data.to_csv('refined.csv', index=False)

missing_values = Refined_data.isnull()

print(missing_values.sum())