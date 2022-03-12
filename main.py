import json
import time
from datetime import datetime

with open("north_station.json", "r") as n_station:
    n_data = n_station.read()
n_data_json = json.loads(n_data)

for data in n_data_json:

    #路線名稱
    route_name = data["SubRouteName"]["Zh_tw"]

    timetables = data["Timetables"]
    for time in timetables:

        #出發時間
        bus_time_text = time["StopTimes"][0]["ArrivalTime"]

        #出發站點
        depart_station = time["StopTimes"][0]["StopName"]["Zh_tw"]

        # 平日 or 假日
        weekday = 0
        weekend = 0
        if time["ServiceDay"]["Sunday"] == 1:
            weekend = 1
        if time["ServiceDay"]["Monday"] == 1:
            weekday = 1

        print(route_name, bus_time_text, depart_station, weekday, weekend)




