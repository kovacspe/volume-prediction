from load_data import Dataset
import matplotlib.pyplot as plt
import sklearn.preprocessing
import statistics
import os
file_name = 'SandP_data.csv'
file_name = os.path.join('data', file_name)


def normalize(row, maximums, minimums):
    return (row['Volume']-minimums[row['year']])/(maximums[row['year']]-minimums[row['year']])


dataset = Dataset(file_name)
by_day_x = []
by_day_y = []
data = dataset.data
# normalize Volume by year
maximums = {}
minimums = {}
for year in range(2000, 2019):
    data_from_year = dataset.get_year(year)['Volume']
    minimums[year] = min(data_from_year)
    maximums[year] = max(data_from_year)
print(data)
data['normalized_volume'] = data.apply(
    lambda row: normalize(row, maximums, minimums), axis=1)
print(data.columns)
for month in range(1, 13):
    for day in range(1, 32):
        data_by_day = data[data['month'] == month]
        data_by_day = data_by_day[data_by_day['day'] == day]
        if len(data_by_day) > 0:
            by_day_y.append(statistics.mean(data_by_day['normalized_volume']))
            by_day_x.append(f'{month}-{day}')
plt.plot(by_day_x, by_day_y)
print('weak days')
for day, mean_volume in zip(by_day_x, by_day_y):
    if mean_volume < 0.35:
        print(day)
print('peak days')
for day, mean_volume in zip(by_day_x, by_day_y):
    if mean_volume > 0.55:
        print(day)

plt.show()
