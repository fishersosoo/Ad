# -*- coding: utf-8 -*-
import json
import os
import pickle
import numpy
from extract import Extractor
from extract import RawData


class MinExtractor(Extractor):
    file_name_temp = "click_min.json"
    bin_file = "click_min.bin"

    def __init__(self):
        if os.path.exists(MinExtractor.file_name_temp):
            os.remove(MinExtractor.file_name_temp)
        if os.path.exists(MinExtractor.bin_file):
            os.remove(MinExtractor.bin_file)


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
            bin_file = open(MinExtractor.bin_file, "rb")
            ip_click_min = dict()
            pickle.load(ip_click_min, bin_file)
            for k, v in ip_click_min.items():
                total_click_dict[k] = sum(v)
            # save dict to binary file
            pickle.dump(total_click_dict, total_click_dict_file)
            total_click_dict_file.close()
        return total_click_dict[ip]


    def get_max_click_min(self, ip):
        # type: (str) -> int
        """
        :rtype: numpy.float64
        """
        if os.path.exists("var_click_min"):
            # has calculated
            max_click_min_dict_file = open("var_click_min", "rb")
            max_click_min_dict = pickle.load(file=max_click_min_dict_file)
            if max_click_min_dict.has_key(ip):
                max_click_min_dict_file.close()
                return max_click_min_dict[ip]
            else:
                max_click_min_dict_file.close()
                raise Exception("wrong ip")
        else:
            # calculate variance click for every ip by min
            max_click_min_dict_file = open("var_click_min", "wb")
            max_click_min_dict = dict()
            bin_file = open(MinExtractor.bin_file, "rb")
            ip_click_min = dict()
            pickle.load(ip_click_min, bin_file)
            for k, v in ip_click_min.items():
                max_click_min_dict[k] = numpy.max(v)
            # save dict to binary file
            pickle.dump(max_click_min_dict, max_click_min_dict_file)
            max_click_min_dict_file.close()
        return max_click_min_dict[ip]


    def get_var_click_min(self, ip):
        # type: (str) -> int
        """
        :rtype: numpy.float64
        """
        if os.path.exists("var_click_min"):
            # has calculated
            var_click_min_dict_file = open("var_click_min", "rb")
            var_click_min_dict = pickle.load(file=var_click_min_dict_file)
            if var_click_min_dict.has_key(ip):
                var_click_min_dict_file.close()
                return var_click_min_dict[ip]
            else:
                var_click_min_dict_file.close()
                raise Exception("wrong ip")
        else:
            # calculate variance click for every ip by min
            var_click_min_dict_file = open("var_click_min", "wb")
            var_click_min_dict = dict()
            bin_file = open(MinExtractor.bin_file, "rb")
            ip_click_min = dict()
            pickle.load(ip_click_min, bin_file)
            for k, v in ip_click_min.items():
                var_click_min_dict[k] = numpy.var(v)
            # save dict to binary file
            pickle.dump(var_click_min_dict, var_click_min_dict_file)
            var_click_min_dict_file.close()
        return var_click_min_dict[ip]


    def get_avg_click_min(self, ip):
        # type: (str) -> float
        ip_click_min = dict()
        bin_file = open(MinExtractor.bin_file, "rb")
        pickle.load(ip_click_min, bin_file)
        # noinspection PyTypeChecker
        return numpy.float64(numpy.mean(ip_click_min[ip])) / MinExtractor.get_total_click(ip)


    def extract(self,line):
        model = RawData(line)
        row = [model.ip, model.timestamps]
        if os.path.exists(MinExtractor.file_name_temp):
            _file = open(MinExtractor.file_name_temp, 'a+')
            _file.writelines(json.dumps(row))
            _file.write('\n')
            _file.flush()
        else:
            _file = open(MinExtractor.file_name_temp, 'w')
            _file.writelines(json.dumps(row))
            _file.write('\n')
            _file.flush()


    def merge(self):
        ip_click_min = dict()
        # dict<ip,list<click times>>
        _file = open(MinExtractor.file_name_temp, 'r')
        line = _file.readline()
        while line != "":
            line = line.replace("\n", "")
            row = json.loads(line)
            line = _file.readline()
            if not ip_click_min.has_key(row[1]):
                ip_click_min[row[0]] = (0 for x in range(60480/60))
            ip_click_min[row[0]][row[2]%60] += 1
        bin_file = open(MinExtractor.bin_file, "wb")
        pickle.dump(ip_click_min, bin_file)
        bin_file.close()
