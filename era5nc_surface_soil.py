import cdsapi
import pandas as pd
from datetime import datetime

datas = pd.date_range(start='07/06/2022', end='07/07/2022')
horas = ["00","12"]
for data in datas:
  dia = data.strftime("%d")
  mes = data.strftime("%m")
  ano = data.strftime("%Y")
  for hora in horas:

    c = cdsapi.Client()

    c.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type': 'reanalysis',
            'format': 'netcdf',
            'variable': [
                'soil_temperature_level_1', 'soil_temperature_level_2', 'soil_temperature_level_3',
                'soil_temperature_level_4', 'volumetric_soil_water_layer_1', 'volumetric_soil_water_layer_2',
                'volumetric_soil_water_layer_3', 'volumetric_soil_water_layer_4',
            ],
            'year': ano,
            'month': mes,
            'day': dia,
            'time': [
                hora+':00',
            ],
            'area': [
                30, -110, -60,
                0,
            ],
        },
        'era5_surface_soil_'+ano+mes+dia+hora+'.nc')
