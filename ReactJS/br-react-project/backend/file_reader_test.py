import os
import json
import datetime

now = datetime.datetime.now()
date_file = now.strftime("%Y%m%d")
time_file = int(now.strftime("%H%M"))
# datetime_filtered = str(int(now.strftime("%Y"))+543) + now.strftime("/%m/%d %H:") + str((int(now.strftime("%M")))).zfill(2) #พ.ศ./ดด/ปป ชช:นน
datetime_filtered = str(int(now.strftime("%Y"))+543) + now.strftime("/%m/%d")


text = open(r'C:\Users\Administrator\Documents\GET\from-meter\meter-{}-{:04d}10.json'.format(date_file, 1600))
data = json.load(text)
# filtered_json = list(filter(lambda x: x["On_Datetime"] == "{} {}".format(datetime_filtered, "16:00"), data))
ec_uscm = data["Sensor"]["EC"] * 1000
# print(filtered_json)
gl = round(ec_uscm * .55 / 1000,2)
print("EC =",ec_uscm)
print("Salinity (g/l) =",gl)