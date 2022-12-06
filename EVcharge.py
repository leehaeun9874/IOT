import folium
from folium import Marker, Icon
import pandas as pd
from pandas import json_normalize
import numpy as np
import requests
import json


url = 'https://api.odcloud.kr/api/15102458/v1/uddi:d8bd25c5-4b89-437a-a0de-b688a44f02af'
evString = {
    'serviceKey': 'zIzbsGXwyMNoGllkI5MJexp2SLhEd0787v8im/HMzxhd8j3kQLHMilaKjm06OUalx2hx7ZU9sUUgw7l96vNe8w==',
    'pageNo': '10',
    'perPage': '9999'
}

response = requests.get(url, evString)
contents = response.text

data = json.loads(contents)
stat = data['data']

df = json_normalize(stat)

m = df[['시도', '충전소명', '경도', '위도']]
print(m)

lat = []  # 위도
lng = []  # 경도
name = []  # 충전소명
local = []  # 시도

for i in range(2647):  # ()괄호값은 데이터 갯수, 총 4778 중 최대 2647
    lat.append(m.iloc[i, 2])
    lng.append(m.iloc[i, 3])
    name.append(m.iloc[i, 1])
    local.append(m.iloc[i, 0])

ev_map = folium.Map(
    location=(37.557945, 126.99419),
    default_zoom_start=7,
    tiles='openstreetmap'
)
for i in range(2647):
    S = lat[i], lng[i]
    L = '<pre>-------------충전소명-------------</pre>'
    N = local[i], name[i]

    folium.Marker(
        S,
        popup=f'{L}{N}',
        icon=Icon(color='blue', icon='info-sign')
    ).add_to(ev_map)

ev_map.save(
    'C:/Users/하은/Desktop/A41915066_이하은_기말IOT응용/EVcharging_station.html')
print('Save OK!')
