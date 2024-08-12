import pandas as pd

data = pd.read_csv('data/aapl_data.csv')

data['timestamp'] = pd.to_datetime(data['timestamp'])

data.set_index('timestamp', inplace=True)

print(data.head())
print(data.dtypes)
print(data.isnull().sum())