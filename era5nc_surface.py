import cdsapi
import pandas as pd
from datetime import datetime

datas = pd.date_range(start='07/01/2022', end='07/05/2022')
for data in datas:
  dia = data.strftime("%d")
  mes = data.strftime("%m")
  ano = data.strftime("%Y")
  horas = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
  for hora in horas:
    c = cdsapi.Client()

    c.retrieve(
      'reanalysis-era5-single-levels',
      {
          'product_type': 'reanalysis',
          'format': 'netcdf',
          'variable': [
              '100m_u_component_of_wind', '100m_v_component_of_wind', '10m_u_component_of_neutral_wind',
              '10m_u_component_of_wind', '10m_v_component_of_neutral_wind', '10m_v_component_of_wind',
              '2m_dewpoint_temperature', '2m_temperature', 'convective_precipitation',
              'high_cloud_cover', 'low_cloud_cover', 'medium_cloud_cover',
              'sea_surface_temperature', 'surface_latent_heat_flux', 'surface_net_solar_radiation',
              'surface_net_thermal_radiation', 'surface_pressure', 'surface_sensible_heat_flux',
              'surface_solar_radiation_downwards', 'surface_thermal_radiation_downwards', 'top_net_solar_radiation',
              'top_net_thermal_radiation', 'total_cloud_cover', 'total_column_cloud_ice_water',
              'total_column_cloud_liquid_water', 'total_precipitation',
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
      'era5_surface_'+ano+mes+dia+hora+'.nc')
