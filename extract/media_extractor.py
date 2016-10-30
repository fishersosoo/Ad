# -*- coding: utf-8 -*-
import json
import os
import pickle
import numpy
from extract import Extractor
from extract import RawData


class MediaExtractor(Extractor):
    file_name_temp = "click_media.json"
    bin_file = "click_media.bin"

    def __init__(self):
        if os.path.exists(MediaExtractor.file_name_temp):
            os.remove(MediaExtractor.file_name_temp)
        if os.path.exists(MediaExtractor.bin_file):
            os.remove(MediaExtractor.bin_file)

    @staticmethod
    def get_total_click(self, ip):
        # type: (str) -> int
        """
        :rtype: numpy.float64
        """
        if os.path.exists("total_click_dict_file"):
            # has calculated
            total_click_dict_file = open("total_click_dict_file", "rb")
            total_click_dict = pickle.load(file=total_click_dict_file)
            if total_click_dict.has_key(ip):
                total_click_dict_file.close()
                return total_click_dict[ip]
            else:
                total_click_dict_file.close()
                raise Exception("wrong ip")
        else:
            # calculate total click for every ip
            total_click_dict_file = open("total_click_dict_file", "wb")
            total_click_dict = dict()
            bin_file = open(MediaExtractor.bin_file, "rb")
            ip_click_sec = dict()
            pickle.load(ip_click_sec, bin_file)
            for k, v in ip_click_sec.items():
                total_click_dict[k] = sum(v)
            # save dict to binary file
            pickle.dump(total_click_dict, total_click_dict_file)
            total_click_dict_file.close()
        return total_click_dict[ip]

    @staticmethod
    def get_max_click_media(self, ip):
        # type: (str) -> int
        """
        :rtype: numpy.float64
        """
        if os.path.exists("var_click_sec"):
            # has calculated
            max_click_media_dict_file = open("var_click_media", "rb")
            max_click_media_dict = pickle.load(file=max_click_media_dict_file)
            if max_click_media_dict.has_key(ip):
                max_click_media_dict_file.close()
                return max_click_media_dict[ip]
            else:
                max_click_media_dict_file.close()
                raise Exception("wrong ip")
        else:
            # calculate variance click for every ip by sec
            max_click_media_dict_file = open("var_click_media", "wb")
            max_click_media_dict = dict()
            bin_file = open(MediaExtractor.bin_file, "rb")
            ip_click_sec = dict()
            pickle.load(ip_click_sec, bin_file)
            for k, v in ip_click_sec.items():
                max_click_media_dict[k] = numpy.max(v.values())
            # save dict to binary file
            pickle.dump(max_click_media_dict, max_click_media_dict_file)
            max_click_media_dict_file.close()
        return max_click_media_dict[ip]

    @staticmethod
    def get_var_click_media(self, ip):
        # type: (str) -> int
        """
        :rtype: numpy.float64
        """
        if os.path.exists("var_click_media"):
            # has calculated
            var_click_sec_dict_file = open("var_click_media", "rb")
            var_click_sec_dict = pickle.load(file=var_click_sec_dict_file)
            if var_click_sec_dict.has_key(ip):
                var_click_sec_dict_file.close()
                return var_click_sec_dict[ip]
            else:
                var_click_sec_dict_file.close()
                raise Exception("wrong ip")
        else:
            # calculate variance click for every ip by sec
            var_click_sec_dict_file = open("var_click_media", "wb")
            var_click_sec_dict = dict()
            bin_file = open(MediaExtractor.bin_file, "rb")
            ip_click_sec = dict()
            pickle.load(ip_click_sec, bin_file)
            for k, v in ip_click_sec.items():
                var_click_sec_dict[k] = numpy.var(v.values())
            # save dict to binary file
            pickle.dump(var_click_sec_dict, var_click_sec_dict_file)
            var_click_sec_dict_file.close()
        return var_click_sec_dict[ip]

    @staticmethod
    def get_avg_click_media(self, ip):
        # type: (str) -> float
        ip_click_sec = dict()
        bin_file = open(MediaExtractor.bin_file, "rb")
        pickle.load(ip_click_sec, bin_file)
        # noinspection PyTypeChecker
        return numpy.float64(numpy.mean(ip_click_sec[ip].values())) / MediaExtractor.get_total_click(ip)

    @staticmethod
    def get_count_media(self,ip):
        if os.path.exists("count_click_media"):
            # has calculated
            var_click_sec_dict_file = open("count_click_media", "rb")
            var_click_sec_dict = pickle.load(file=var_click_sec_dict_file)
            if var_click_sec_dict.has_key(ip):
                var_click_sec_dict_file.close()
                return var_click_sec_dict[ip]
            else:
                var_click_sec_dict_file.close()
                raise Exception("wrong ip")
        else:
            # count media_id for every ip
            var_click_sec_dict_file = open("count_click_media", "wb")
            var_click_sec_dict = dict()
            bin_file = open(MediaExtractor.bin_file, "rb")
            ip_click_sec = dict()
            pickle.load(ip_click_sec, bin_file)
            for k, v in ip_click_sec.items():
                var_click_sec_dict[k] = len(v)
            # save dict to binary file
            pickle.dump(var_click_sec_dict, var_click_sec_dict_file)
            var_click_sec_dict_file.close()
        return var_click_sec_dict[ip]

    @staticmethod
    def extract(line):
        model = RawData(line)
        row = [model.ip, model.media_id]
        if os.path.exists(MediaExtractor.file_name_temp):
            _file = open(MediaExtractor.file_name_temp, 'a+')
            _file.writelines(json.dumps(row))
            _file.write('\n')
            _file.flush()
        else:
            _file = open(MediaExtractor.file_name_temp, 'w')
            _file.writelines(json.dumps(row))
            _file.write('\n')
            _file.flush()

    @staticmethod
    def merge():
        ip_click_media = dict()
        # dict<ip,dict<media_id, click times>>
        _file = open(MediaExtractor.file_name_temp, 'r')
        line = _file.readline()
        while line != "":
            line = line.replace("\n", "")
            row = json.loads(line)
            line = _file.readline()
            if not ip_click_media.has_key(row[1]):
                ip_click_media[row[0]] = dict()
            if not ip_click_media[row[0]].has_key(row[2]):
                ip_click_media[row[0]][row[2]] = 0
            ip_click_media[row[0]][row[2]] += 1
        bin_file = open(MediaExtractor.bin_file, "wb")
        pickle.dump(ip_click_media, bin_file)
        bin_file.close()
