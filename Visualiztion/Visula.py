import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns

file_pth = 'Normalization/standardized_data.csv'

data = pd.read_csv(file_pth)
numerical_cols = data.select_dtypes(include=['int64'])
data.hist(bins=20, figsize=(15,10))
plt.savefig('histogram.png', dpi=300)
plt.close()




plt.figure(figsize=(15, 6))
plt.boxplot(numerical_cols.values, vert=False, patch_artist=True, showfliers=True)
plt.yticks(range(1, len(numerical_cols.columns) + 1), numerical_cols.columns)  
plt.xlabel("Values")
plt.title("Boxplot with Outliers")
plt.savefig('outliers.png', dpi=300)
plt.close()


#correlation
# corr_matrix = data.corr()
# plt.figure(figsize=(12, 8))
# #use imhow to display the correlation matrix as a heatmap
# plt.imshow(corr_matrix, cmap='coolwarm', interpolation='nearest')
# # Add a color bar on the right to interpret values
# plt.colorbar(label='Correlation Coefficient')

# # Add labels for x and y ticks
# plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
# plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)

# # Display correlation values on the heatmap
# for i in range(len(corr_matrix.columns)):
#     for j in range(len(corr_matrix.columns)):
#         plt.text(j, i, f"{corr_matrix.iloc[i, j]:.2f}", ha='center', va='center', color='black')

# # Show the plot
# plt.show()