# -*- coding: utf-8 -*-

from extract import Extractor
from extract import RawData

import json
import numpy as np


class DevExtractor(Extractor):
    raw_cache_name = "dev_raw_cache_file"
    cache_name = "dev_cache_file"
    fid = None
    dev_id_index = 0
    dev_num_info_index = 0

    @staticmethod
    def init():
        DevExtractor.fid = Extractor.create_file(DevExtractor.raw_cache_name)

    @staticmethod
    def extract(line):
        model = RawData(line)
        key = model.ip

        # DEVICE ID
        fields = list()
        fields.append(model.mobile_imei + model.mobile_idfa + model.mobile_android_id + model.mobile_mac)

        Extractor.solid(key, fields, DevExtractor.fid)

    @staticmethod
    def finish_extract():
        DevExtractor.fid.close()

    @staticmethod
    def merge():
        fid = open(DevExtractor.raw_cache_name, 'r')
        dev_tuple = Extractor.read_line(fid)

        dev_info_dict = dict()

        while dev_tuple is not None:
            for ip in dev_tuple:
                dev = dev_tuple[ip][DevExtractor.dev_id_index]
                if ip in dev_info_dict.keys():
                    dev_info = dev_info_dict[ip]
                    dev_num_info = dev_info[DevExtractor.dev_num_info_index]
                    if dev in dev_num_info.keys():
                        dev_num_info[dev] += 1
                    else:
                        dev_num_info[dev] = 1
                else:
                    dev_info = list()
                    dev_num_info = dict()
                    dev_info.append(dev_num_info)
                    dev_num_info[dev] = 1
                    dev_info_dict[ip] = dev_info

            # next line
            dev_tuple = Extractor.read_line(fid)

        fid = open(DevExtractor.cache_name, 'w')
        fid.writelines(json.dumps(dev_info_dict))

    @staticmethod
    def get_dev_num_info(ip):
        dev_info_dict = Extractor.read_cache(DevExtractor.cache_name)
        dev_num_info = dev_info_dict[ip][DevExtractor.dev_num_info_index]
        return dev_num_info

    @staticmethod
    def get_total_dev(ip):
        dev_num_info = DevExtractor.get_dev_num_info(ip)
        return len(dev_num_info.keys())

    @staticmethod
    def get_avg_click_dev(ip):
        dev_num_info = DevExtractor.get_dev_num_info(ip)
        total_count = 0
        for dev in dev_num_info:
            total_count += dev_num_info[dev]

        return total_count

    @staticmethod
    def get_max_click_dev(ip):
        dev_num_info = DevExtractor.get_dev_num_info(ip)
        max_click = -1
        total = 0
        for dev in dev_num_info:
            dev_click = dev_num_info[dev]
            total += dev_click
            if dev_click > max_click:
                max_click = dev_click

        return max_click / total

    @staticmethod
    def get_var_click_dev(ip):
        dev_num_info = DevExtractor.get_dev_num_info(ip)
        click_list = list()
        for dev in dev_num_info:
            click_list.append(dev_num_info[dev])

        dev_click_std = np.reshape(click_list, (-1, 1)).std()
        return dev_click_std
