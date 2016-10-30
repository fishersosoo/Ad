import os
import json
import numpy as np
from extract import Extractor
from extract import RawData

class UAExtractor(Extractor):
    raw_cache_name = 'ua_raw_cache_file'
    cache_name = 'ua_cache_file'
    ua_index = 0
    ua_num_index = 0

    @staticmethod
    def __init__(self):
        UAExtractor.fid = Extractor.load_cache(UAExtractor.raw_cache_name)
    
    @staticmethod
    def extract(line):
        model = RawData(line)
        key = model.ip
        fields = list()

        fields.append(model.user_agent)
        Extractor.solid(key, fields, UAExtractor.fid)
    
    @staticmethod
    def merge():
        fid = open(UAExtractor.raw_cache_name, 'r')
        tuple = Extractor.read_line(fid)

        ua_info_dict = dict()

        while tuple != None:
            for ip in tuple:
                if ua_info_dict.has_key(ip):
                    ua_info = ua_info_dict[ip]
                    ua_num = ua_info[UAExtractor.ua_num_index]
                    if ua_num.has_key(ip):
                        ua_num[ip] += 1
                    else:
                        ua_num = 1
                else:
                    ua_info = list()
                    ua_num = dict()
                    ua_info.append(ua_num)
                    ua_num[tuple[ip]] = 1
                    ua_info_dict[ip] = ua_info
        
        fid = open(UAExtractor.cache_name, 'w')
        fid.writelines(json.dumps(ua_info_dict))
    
    @staticmethod
    def get_ua_info_dict():
        fid = open(UAExtractor.cache_name, 'r')
        ua_info_dict = json.loads(fid.readline().replace('\n', ''))
        return ua_info_dict
    
    @staticmethod
    def get_ua_num_info(ip):
        ua_info_dict = UAExtractor.get_ua_info_dict()
        ua_num_info = ua_info_dict[ip][UAExtractor.ua_num_index]
        return ua_num_info
    
    @staticmethod
    def get_avg_click_uas(ip):
        ua_num_info = UAExtractor.get_ua_num_info(ip)
        total_count = 0
        for ua_id in ua_num_info:
            total_count += ua_num_info[ua_id]
        
        return 1.0 / total_count
    
    @staticmethod
    def get_var_click_uas(ip):
        ua_num_info = UAExtractor.get_ua_num_info(ip)
        click_nums = list()
        for ua_id in ua_num_info:
            click_nums.append(ua_num_info[ua_id])
        ua_std = np.reshape(click_nums, (-1, 1)).std()
        return ua_std
    
    @staticmethod
    def get_max_click_uas(ip):
        ua_num_info = UAExtractor.get_ua_num_info(ip)
        max_click = 0
        for ua_id in ua_num_info:
            if max_click < ua_num_info[ua_id]:
                max_click = ua_num_info[ua_id]
        return max_click