import pandas as pd
from netCDF4 import Dataset, date2num
import numpy as np
import os
import sys

def process_drifter_data(csv_file):
    drifter_data = pd.read_csv(csv_file)
    year = 2024
    drifter_data['year'] = year
    drifter_data.rename(columns={'MTH': 'month', 'DAY': 'day', 'HR_GMT': 'hour', 'MIN': 'minute', 'LON': 'lon', 'LAT': 'lat'}, inplace=True)
    drifter_data['time'] = pd.to_datetime(drifter_data[['year', 'month', 'day', 'hour', 'minute']])

    # Split the data by drifter ID
    drifter_data_split = [drifter_data[drifter_data['ID'] == i] for i in drifter_data['ID'].unique()]

    output_dir = os.path.dirname(csv_file)
    files = []

    for df in drifter_data_split:
        nc_file = os.path.join(output_dir, f'{df["ID"].iloc[0]}_CLEANED.nc')
        
        try:
            ds = Dataset(nc_file, 'w', format='NETCDF4')
        except PermissionError:
            os.remove(nc_file)
            ds = Dataset(nc_file, 'w', format='NETCDF4')

        df = df.drop_duplicates(subset='time')
        df.set_index('time', inplace=True)
        df = df.resample('H').mean().dropna()
        df.drop(columns=['month', 'day', 'hour', 'minute', 'YEARDAY', 'DEPTH'], inplace=True)
        ds.close()

        with Dataset(nc_file, 'w', format='NETCDF4') as ds:
            ds.createDimension('time', None)
            dates = pd.to_datetime(df.index.values)
            
            # Create the 'time' variable and set its units attribute explicitly
            time = ds.createVariable('time', np.float64, ('time',))
            time.units = 'hours since 1900-01-01 00:00:00'
            time.calendar = 'gregorian'
            
            # Convert datetime64[ns] to numeric Unix time values
            time_values = date2num(dates.to_pydatetime(), units=time.units, calendar=time.calendar)
            time[:] = time_values
            
            # Create the 'lon' and 'lat' variables
            lon = ds.createVariable('lon', np.float64, ('time',))
            lat = ds.createVariable('lat', np.float64, ('time',))
            
            # Assign longitude and latitude data
            lon[:] = df['lon'].values
            lat[:] = df['lat'].values

            print(f'NetCDF file created: {nc_file}')
            files.append(nc_file)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
        process_drifter_data(csv_file)
    else:
        print("Please provide a CSV file as an argument.")
