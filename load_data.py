import pandas as pd
import datetime as dt
import holidays


class Dataset:
    def __init__(self, file):
        self.data = pd.read_csv(file)
        self.data['Date'] = self.data.apply(
            lambda row: dt.date.fromisoformat(row['Date']), axis=1)
        self.data['year'] = self.data.apply(
            lambda row: row['Date'].year, axis=1)
        self.data['month'] = self.data.apply(
            lambda row: row['Date'].month, axis=1)
        self.data['day'] = self.data.apply(
            lambda row: row['Date'].day, axis=1)
        self.data['week_day'] = self.data.apply(
            lambda row: row['Date'].weekday(), axis=1)
        self.data['business_day_before'] = self.data.apply(
            lambda row: Dataset.is_business_day(row['Date'] + dt.timedelta(days=-1)), axis=1)

    @staticmethod
    def is_business_day(date):
        return (date not in holidays.US()) and (date.weekday() not in [5, 6])

    def get_year(self, year):
        return self.data[self.data['year'] == year]

    def get_subset(self, start='2000-01-01', end='2018-12-31'):
        start = dt.date.fromisoformat(start)
        end = dt.date.fromisoformat(end)
        return self.data[(self.data['Date'] >= start) & (self.data['Date'] <= end)]
