import json
import os
from tkinter.filedialog import SaveAs



def write_json(filename):
    data = {'name': 'Saurabh', 'age': 22}
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
        print(f'Wrote {filename} successfully')

def read_json(filename):
    with open(filename , 'r' ) as file:
        data = json.load(file)
        print(f'None: {data['name']}, Age: {data['age']}')

def delete_json(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f'{filename} deleted successfully')
    else:
        print(f'{filename} does not exists')

filename = 'myfile.json'
write_json(filename)
print('Data read frokm CSV file:')
(read_json(filename))
delete_json(filename)

