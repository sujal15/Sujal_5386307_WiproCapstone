import pandas as pd

# Creating a sample DataFrame
data = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
})

# Save files
data.to_csv('sample_data.csv', index=False)
data.to_excel('sample_data.xlsx', index=False)   # Use .xlsx instead of .xls
data.to_json('sample_data.json', orient='records')

# Read files back
csv_data = pd.read_csv('sample_data.csv')
print("Data from CSV:\n", csv_data)

excel_data = pd.read_excel('sample_data.xlsx')   # Read .xlsx
print("Data from Excel:\n", excel_data)

json_data = pd.read_json('sample_data.json')
print("Data from JSON:\n", json_data)