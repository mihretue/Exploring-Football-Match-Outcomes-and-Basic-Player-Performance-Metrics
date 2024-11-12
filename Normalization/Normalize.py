from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd

file_path = 'Preprocessing/refined.csv'

data = pd.read_csv(file_path)
numerical_cols = data.select_dtypes(include=['int64']).columns


scaler_norm = MinMaxScaler()    
scaler_std = StandardScaler()


#Normalization
data_normalized = data.copy()
data_normalized[numerical_cols] = scaler_norm.fit_transform(data[numerical_cols])

data_normalized.to_csv('Normalization/normalized_data.csv')

#Standardization

data_standardized = data.copy()
data_standardized[numerical_cols] = scaler_std.fit_transform(data[numerical_cols])

data_standardized.to_csv('Normalization/standardized_data.csv')

print(data_normalized.head(), data_standardized.head())