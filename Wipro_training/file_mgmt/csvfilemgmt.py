import csv
import os
from tkinter.filedialog import SaveAs
columnnames = ['name', 'age']
data = {'name': 'Saurabh', 'age': 22}

def write_csv(filename):
    with open(filename, 'w', newline='\n') as file:
        writer = csv.DictWriter(file, fieldnames=columnnames)
        writer.writeheader()
        writer.writerow(data)

def read_csv(filename):
    with open(filename , 'r' , newline='\n') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f'None: {row['name']}, Age: {row['age']}')

def delete_csv(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f'{filename} deleted successfully')
    else:
        print(f'{filename} does not exists')

filename = 'myfile.csv'
write_csv(filename)
print('Data read frokm CSV file:')
read_csv(filename)
delete_csv(filename)

