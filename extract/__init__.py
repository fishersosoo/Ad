# -*- coding: utf-8 -*-
import os
from abc import ABCMeta, abstractmethod
from extract import RawDataModel
from RawDataModel import RawData


import pickle
import json
import numpy


class Context:
    media_info_file = None
    media_info_table = dict()

    # dict<media_id,list>
    def __init__(self):
        pass

    @staticmethod
    def load_media_info_file(self, csv_file):
        line = csv_file.readline()
        while line != "":
            line = line.replace("\n", "")
            line = line.splite(",")
            Context.media_info_table[line[0]] = [line[1], line[2], line[3], line[4]]
            line = csv_file.readline


class Extractor(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def extract(line):
        pass

    @abstractmethod
    def merge(self):
        pass

    @abstractmethod
    # 当第一次使用 Extractor 时应该调用该方法，创建本地缓存文件
    def init(self):
        # create_file(file_name)
        pass

    @staticmethod
    def solid(key, field_list, fid):
        # 将 field_list 作为值构造一个 dict, append 到本地文件中（不是二进制，一行一个 dict 的 json ）
        key_value = dict()
        key_value[key] = field_list
        fid.writelines(json.dumps(key_value))
        fid.write("\n")

    @staticmethod
    def load_cache(file_name):
        # 判断文件是否存在，不存在则打开
        return open(file_name,'a+')

    @staticmethod
    def read_line(fid):
        # 从文件中读取一行并返回 dict
        line = fid.readline()
        if line == "":
            fid.close()
            return None
        return json.loads(line.replace("\n",""))

    @staticmethod
    def read_cache(file_name):
        # 从文件中读取一行并返回 cache
        fid = open(file_name, 'r')
        cache = json.loads(fid.readline().replace("\n",""))
        fid.close()
        return cache


class TimeExtractor(Extractor):
    @staticmethod
    def extract(line):
        model=RawData(line)
        pass

    @staticmethod
    def merge():
        pass
