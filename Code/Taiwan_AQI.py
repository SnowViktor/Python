from requests import get
from csv import writer

url = 'https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON'
data = get(url).json()

with open('./AQI.csv', mode='w', encoding='utf-8', newline='') as csv_file:
    csv_write = writer(csv_file, delimiter='\t')
    csv_write.writerow(['縣市', '測站名稱', 'AQI', '空氣品質', 'O3_8h(ppb)', 'O3(ppb)', 'PM2.5(μg/m3)', 'PM10(μg/m3)', 'CO_8h(ppm)', 'SO2(ppb)', 'NO2(ppb)'])
    for i in data['records']:
        csv_write.writerow([i['county'], i['sitename'], i['aqi'], i['status'], i['o3_8hr'], i['o3'], i['pm2.5'], i['pm10'], i['co_8hr'], i['so2'], i['no2']])
