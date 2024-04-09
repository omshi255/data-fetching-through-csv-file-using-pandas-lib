import sqlite3
import pandas as pd

# CSV file ka path specify karein
csv_file_path = 'C:\\Users\\swati sen\\fetch_data\\data.csv'
# CSV file ko read karein aur DataFrame mein store karein
df = pd.read_csv('C:\\Users\\swati sen\\fetch_data\\data.csv')
# DataFrame ko Excel file mein save karein
excel_path = 'output.xlsx'
df.to_excel(excel_path, index=False)
# Output message
print(f'Data has been successfully fetched from the CSV file and stored in {excel_path}')
