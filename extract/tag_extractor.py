# -*- coding: utf-8 -*-

from extract import Extractor
from extract import RawData
from extract import Context

import json
import numpy as np


class TagExtractor(Extractor):
    raw_cache_name = "tag_raw_cache_file"
    cache_name = "tag_cache_file"
    fid = None
    tag_index = 0
    tag_num_info_index = 0

    @staticmethod
    def init():
        TagExtractor.fid = Extractor.create_file(TagExtractor.raw_cache_name)

    @staticmethod
    def extract(line):
        model = RawData(line)
        key = model.ip

        # SECOND_TAG
        fields = list()
        fields.append(Context.media_info_table[key][2])

        Extractor.solid(key, fields, TagExtractor.fid)

    @staticmethod
    def finish_extract():
        TagExtractor.fid.close()

    @staticmethod
    def merge():
        fid = open(TagExtractor.raw_cache_name, 'r')
        tag_tuple = Extractor.read_line(fid)

        tag_info_dict = dict()

        while tag_tuple is not None:
            for ip in tag_tuple:
                tag = tag_tuple[ip][TagExtractor.tag_index]
                if ip in tag_info_dict.keys():
                    tag_info = tag_info_dict[ip]
                    tag_num_info = tag_info[TagExtractor.tag_num_info_index]
                    if tag in tag_num_info.keys():
                        tag_num_info[tag] += 1
                    else:
                        tag_num_info[tag] = 1
                else:
                    tag_info = list()
                    tag_num_info = dict()
                    tag_info.append(tag_num_info)
                    tag_num_info[tag] = 1
                    tag_info_dict[ip] = tag_info

            tag_tuple = Extractor.read_line(fid)

        fid = open(TagExtractor.cache_name, 'w')
        fid.writelines(json.dumps(tag_info_dict))

    @staticmethod
    def get_tag_num_info(ip):
        tag_info_dict = Extractor.read_cache(TagExtractor.cache_name)
        tag_num_info = tag_info_dict[ip][TagExtractor.tag_num_info_index]
        return tag_num_info

    @staticmethod
    def get_avg_click_tag(ip):
        tag_num_info = TagExtractor.get_tag_num_info(ip)
        total_count = 0
        for tag in tag_num_info:
            total_count += tag_num_info[tag]

        return 1.0 / total_count

    @staticmethod
    def get_var_click_tag(ip):
        tag_num_info = TagExtractor.get_tag_num_info(ip)
        click_nums = list()
        for tag in tag_num_info:
            click_nums.append(tag_num_info[tag])

        tag_std = np.reshape(click_nums, (-1, 1)).std()
        return tag_std

    @staticmethod
    def get_max_click_tag(ip):
        tag_num_info = TagExtractor.get_tag_num_info(ip)
        max_click = -1
        total = 0
        for tag in tag_num_info:
            tag_click = tag_num_info[tag]
            total += tag_click
            if tag_click > max_click:
                max_click = tag_click

        return max_click / total
