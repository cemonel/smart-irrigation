import pandas
import numpy
import datetime
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
%matplotlib qt

MIN_MOISTURE = 1024

## Retrieve Data from Csv File
irrigation_data = pandas.read_csv('data/3.csv',sep='\t', encoding="ISO-8859-1")

# Time Preparation
irrigation_data['time'] = irrigation_data['time'].apply(lambda ts: ts//1000)
irrigation_data['time'] = irrigation_data['time'].apply(lambda ts: datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
# irrigation_data.set_index(irrigation_data['time'], inplace=True)
irrigation_data.set_index(pandas.DatetimeIndex(irrigation_data['time']), inplace=True)
del irrigation_data['time']

# Soil-Mosutire Percantage Calculation
irrigation_data['soil_moisture'] = irrigation_data['soil_moisture'].apply(lambda x: MIN_MOISTURE - x)
max_soil_moisture = irrigation_data['soil_moisture'].max()
irrigation_data['soil_moisture'] = irrigation_data['soil_moisture'].apply(lambda x: (x/max_soil_moisture)*100)

irrigation_data

# register_matplotlib_converters()
plt.rcParams['figure.figsize'] = (24,6)   # Change the plot size
irrigation_data.resample('3M').sum()
irrigation_data.plot(grid=True, title="Temperature-SoilHUM-AirHUM", kind="line").set_ylabel("Temperature(Celcius) -- SoilHUM(%) -- AirHUM(%)")
