import csv, requests

url = 'https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON'
data = requests.get(url)
data_json = data.json()

with open('...\...\AQI.csv', mode='w', encoding='utf-8', newline='') as csv_file:
    csv_write = csv.writer(csv_file, delimiter='\t')
    csv_write.writerow(['縣市', '測站名稱', 'AQI', '空氣品質', 'PM₂.₅(μg/m³)', 'PM₁₀(μg/m³)', 'O₃(ppb)'])
    for i in data_json['records']:
        csv_write.writerow([i['county'], i['sitename'], i['aqi'], i['status'], i['pm2.5'], i['pm10'], i['o3']])