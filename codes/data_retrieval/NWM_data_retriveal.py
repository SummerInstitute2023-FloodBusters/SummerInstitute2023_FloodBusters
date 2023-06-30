# Modified based on this source code:
# Abdelkader, M., J. H. Bravo Mendez (2023). NWM version 2.1 model output data retrieval, HydroShare, https://doi.org/10.4211/hs.c4c9f0950c7a42d298ca25e4f6ba5542

import multiprocessing
import os
import fsspec
import pandas as pd
import xarray as xr
from tqdm import tqdm

# https://noaa-nwm-retro-v2-zarr-pds.s3.amazonaws.com/index.html
# https://noaa-nwm-retrospective-2-1-zarr-pds.s3.amazonaws.com/index.html
#         noaa-nwm-retrospective-2-1-zarr-pds/
# https://noaa-nwm-retrospective-2-1-pds.s3.amazonaws.com/index.html



#%%
NWM_FeatureIDs = pd.read_csv(
# change the path to the path of the excel file
    'C:/Users/Berina/OneDrive - stevens.edu/Documents/Summer_Institute/Project/HAND/NWM_extract/nwm_reachid.csv')
#NWM_FeatureIDs['USGS_ID'] = NWM_FeatureIDs['USGS_ID'].apply(lambda x: '{:0>8}'.format(x))
#%%
fs = fsspec.filesystem('s3', anon=True)
_file = fs.glob('noaa-nwm-retrospective-2-1-zarr-pds/chrtout.zarr')

ds = xr.open_dataset(fs.get_mapper(_file[0]), engine='zarr', backend_kwargs={'consolidated': True})

#%%
s_date = '2016-08-10T00:00'
e_date = '2016-08-17T23:00'

ds2 = ds.sel(time = slice(s_date, e_date))


#%%
def download_nwm_stations(row):
    try:
        print('\nRunning station row : ', row, ' | NWM_ID : ', NWM_FeatureIDs.loc[row, 'NWM_ID'],'...')
        Forecast_point = ds2['streamflow'].sel(feature_id=int(NWM_FeatureIDs.loc[row, 'NWM_ID']))
        #Forecast_point = ds2['velocity'].sel(feature_id=int(NWM_FeatureIDs.loc[row, 'NWM_ID']))
        Forecast_point = Forecast_point.to_pandas().to_frame()
        Forecast_point.columns = [NWM_FeatureIDs.loc[row, 'NWM_ID']]
        # Forecast_point.to_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data',
        #                                    str(NWM_FeatureIDs.loc[row, 'NWM_ID']) + '.csv'))
        Forecast_point.to_csv(os.path.join('C:/Users/Berina/OneDrive - stevens.edu/Documents/Summer_Institute/Project/HAND/NWM_extract/', str(NWM_FeatureIDs.loc[row, 'NWM_ID']) + '.csv'))
        
    except:
        print('\nError with station row : ', row, ' | NWM_ID : ', NWM_FeatureIDs.loc[row, 'NWM_ID'])
        pass
    return 0


def run(NWM_FeatureIDs):
    print('Getting list of files...')
    files = [e for e in NWM_FeatureIDs.index]
    pool = multiprocessing.Pool(processes=6)
    print('Downloading NWM Stations ...')
    _stats = tqdm(pool.map(download_nwm_stations, files), desc='Processing rows', total=len(files))
    #_stats = [e for e in _stats if e]
    # _stats = pd.DataFrame(_stats, columns=['id', 'rmse', 'corr', 'bias']).set_index(['id'])
    # final = pd.concat([NWM_FeatureIDs, _stats], axis=1)
    # final.to_csv('/home/ismart/final_output.csv')


if __name__ == '__main__':
    run(NWM_FeatureIDs)

# %%
