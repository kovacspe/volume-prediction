from load_data import Dataset
import os
file_name = 'SandP_data.csv'
file_name = os.path.join('data', file_name)

dataset = Dataset(file_name)
print(dataset.data)
