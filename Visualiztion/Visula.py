import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns

file_pth = 'Normalization/standardized_data.csv'

data = pd.read_csv(file_pth)
numerical_cols = data.select_dtypes(include=['int64'])
data.hist(bins=20, figsize=(15,10))
plt.show()

plt.figure(figsize=(15, 6))
plt.boxplot(numerical_cols.values, vert=False, patch_artist=True, showfliers=True)
plt.yticks(range(1, len(numerical_cols.columns) + 1), numerical_cols.columns)  
plt.xlabel("Values")
plt.title("Boxplot with Outliers")
plt.show()
