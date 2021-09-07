'''
Gather data from FRED using the FRED API
source: https://lvngd.com/blog/fred-api-python/

FRED IPA:
    Sources - data sources
    Releases - release of data from a source
    Series (time series)
    Series observation values
    Categories
    Tags
'''

import requests

fred_key = 'a1ae8901952eee6f396bb591555c0687'

endpoint = 'https://api.stlouisfed.org/fred/sources'

params = {'api_key':fred_key,
        'file_type':'json'
        }

res = requests.get(endpoint, params)
res.json()
