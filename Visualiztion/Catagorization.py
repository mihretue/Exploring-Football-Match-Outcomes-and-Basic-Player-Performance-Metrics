import pandas as pd
# import xlsxwriter

data = pd.read_csv('Normalization/standardized_data.csv')
# getting the non numeric data in one object
string_columns = data.select_dtypes(include=['object']).columns
for i in string_columns:
    # print(i)
    data[i] = pd.factorize(data[i])[0]

print("\n modified data:")
print(data)

data.to_csv("Catagorized.csv", index=False )

