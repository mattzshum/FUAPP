import pytrends
from pytrends.request import TrendReq
import pandas as pd
import numpy as np

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ['Blockchain']
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')


df = pytrends.trending_searches(pn='united_states')
print(df)