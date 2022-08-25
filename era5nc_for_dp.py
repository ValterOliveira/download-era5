import cdsapi
import pandas as pd
from datetime import datetime

datas = pd.date_range(start='07/01/2022', end='07/05/2022')
horas = ["00","03","06","09","12","15","18","21"]
for data in datas:
  dia = data.strftime("%d")
  mes = data.strftime("%m")
  ano = data.strftime("%Y")
  for hora in horas:
    c = cdsapi.Client()

    c.retrieve(
        'reanalysis-era5-pressure-levels',
        {
            'product_type': 'reanalysis',
            'format': 'netcdf',
            'variable': [
                'fraction_of_cloud_cover', 'geopotential', 'relative_humidity',
              'specific_cloud_ice_water_content', 'specific_cloud_liquid_water_content', 'specific_humidity',
              'temperature', 'u_component_of_wind', 'v_component_of_wind',
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
            'pressure_level': [
                '10', '20', '30',
                '50', '100', '150',
                '200', '250', '300',
                '350', '400', '500',
                '550', '600', '650',
                '700', '750', '800',
                '850', '875', '900',
                '925', '950', '975',
                '1000',
            ],
        },
        'era5-'+ano+mes+dia+hora+'.nc')
