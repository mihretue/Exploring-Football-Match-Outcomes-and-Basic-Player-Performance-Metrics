import matplotlib.pyplot as plt
import pandas as pd

file_pth = 'Catagorized.csv'
data = pd.read_csv(file_pth)
#correlation
corr_matrix = data.corr()
plt.figure(figsize=(16, 12))
#use imhow to display the correlation matrix as a heatmap
plt.imshow(corr_matrix, cmap='coolwarm', interpolation='nearest')
# Add a color bar on the right to interpret values
plt.colorbar(label='Correlation Coefficient')

# Add labels for x and y ticks
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90, fontsize=10)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns, fontsize=10)

# Display correlation values on the heatmap
for i in range(len(corr_matrix.columns)):
    for j in range(len(corr_matrix.columns)):
        plt.text(j, i, f"{corr_matrix.iloc[i, j]:.2f}", ha='center', va='center', color='black', fontsize=9)

# Show the plot
# plt.savefig('Correlation.png', dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.show()
strong_corr = corr_matrix[(corr_matrix > 0.7) | (corr_matrix < -0.7)]
print("Strong Correlations:")
print(strong_corr)