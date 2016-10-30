# -*- coding: utf-8 -*-

from extract import Extractor
from extract import RawData

import json
import numpy as np


class CookieExtractor(Extractor):
    raw_cache_name = "cookie_raw_cache_file"
    cache_name = "cookie_cache_file"
    fid = None
    cookie_index = 0
    cookie_num_index = 0

    @staticmethod
    def init():
        CookieExtractor.fid = Extractor.load_cache(CookieExtractor.raw_cache_name)

    @staticmethod
    def extract(line):
        model = RawData(line)
        key = model.ip
        fields = list()

        # cookie
        fields.append(model.cookie)
        Extractor.solid(key, fields, CookieExtractor.fid)

    @staticmethod
    def finish_extract():
        CookieExtractor.fid.close()

    @staticmethod
    def merge():
        fid = open(CookieExtractor.raw_cache_name, 'r')
        cookie_tuple = Extractor.read_line(fid)

        cookie_info_dict = dict()

        while cookie_tuple is not None:
            # 统计该 IP 的所有点击的 cookie 以及其数量
            for ip in tuple:
                cookie = cookie_tuple[ip][CookieExtractor.cookie_index]
                if ip in cookie_info_dict.keys():
                    cookie_info = cookie_info_dict[ip]
                    cookie_num = cookie_info[CookieExtractor.cookie_num_index]
                    if cookie in cookie_num.kyes():
                        cookie_num[cookie] += 1
                    else:
                        cookie_num[cookie] = 1
                else:
                    cookie_info = list()
                    cookie_num = dict()
                    cookie_info.append(cookie_num)
                    cookie_num[cookie] = 1
                    cookie_info_dict[ip] = cookie_info

            # next line
            cookie_tuple = Extractor.read_line(fid)

        fid = open(CookieExtractor.cache_name, 'w')
        fid.writelines(json.dumps(cookie_info_dict))

    @staticmethod
    def get_cookie_num_info(ip):
        cookie_info_dict = Extractor.read_cache(CookieExtractor.cache_name)
        cookie_num_info = cookie_info_dict[ip][CookieExtractor.cookie_num_index]
        return cookie_num_info

    @staticmethod
    def get_avg_click_cookies(ip):
        cookie_num_info = CookieExtractor.get_cookie_num_info(ip)
        total_count = 0
        for cookie_id in cookie_num_info:
            total_count += cookie_num_info[cookie_id]

        return 1.0 / total_count

    @staticmethod
    def get_var_click_cookies(ip):
        cookie_num_info = CookieExtractor.get_cookie_num_info(ip)
        click_nums = list()
        for cookie_id in cookie_num_info:
            click_nums.append(cookie_num_info[cookie_id])

        cookie_std = np.reshape(click_nums, (-1, 1)).std()
        return cookie_std

