from api_key import av_key
from alpha_vantage.timeseries import TimeSeries

ts = TimeSeries(key='av_key')

data,meta_data = ts.get_intraday('GOOGL')

print(data)
print(meta_data)