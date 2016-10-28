# -*- coding: utf-8 -*-
import json
class RawData:
    def __init__(self, line):
        line.replace("\n", "")
        line = line.split(",")
        self.rank = int(line[0])
        self.dt = int(line[1])
        self.cookie = line[2]
        self.ip = line[3]
        self.mobile_idfa = line[4]
        self.mobile_imei = line[5]
        self.mobile_android_id = line[6]
        self.mobile_openudid = line[7]
        self.mobile_mac = line[8]
        self.timestamps = int(line[9])
        self.camp_id = int(line[10])
        self.creativeid = int(line[11])
        self.mobile_os = line[12]
        self.mobile_type = line[13]
        self.mobile_app_key = line[14]
        self.mobile_app_name = line[15]
        self.placement_id = line[16]
        self.user_agent = line[17]
        self.media_id = int(line[18])
        self.os = line[19]
        self.born_time = int(line[20])
        self.flag = bool(line[21])

    def __str__(self):
        return json.dumps(self.__dict__)
