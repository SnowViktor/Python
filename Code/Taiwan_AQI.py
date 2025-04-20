"""
需要會員 API Key 才能取用資料。(https://data.moenv.gov.tw/paradigm)
"""

from requests import get
from csv import writer

url = "https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=540e2ca4-41e1-4186-8497-fdd67024ac44&limit=1000&sort=ImportDate%20desc&format=JSON"
response = get(url)
response.raise_for_status()
data = response.json()

with open("./AQI.csv", mode="w", encoding="utf-8", newline="") as csv_file:
    csv_write = writer(csv_file)
    csv_write.writerow(
        [
            "縣市",
            "測站名稱",
            "AQI",
            "空氣品質",
            "O3_8h(ppb)",
            "O3(ppb)",
            "PM2.5(μg/m3)",
            "PM10(μg/m3)",
            "CO_8h(ppm)",
            "SO2(ppb)",
            "NO2(ppb)",
        ]
    )
    for i in data.get("records", []):
        csv_write.writerow(
            [
                i.get("county"),
                i.get("sitename"),
                i.get("aqi"),
                i.get("status"),
                i.get("o3_8hr"),
                i.get("o3"),
                i.get("pm2.5"),
                i.get("pm10"),
                i.get("co_8hr"),
                i.get("so2"),
                i.get("no2"),
            ]
        )
