import os
import json
import numpy as np
from extract import Extractor
from extract import RawData

class PlacementExtractor(Extractor):
    raw_cache_name = 'placement_raw_cache_file'
    cache_name = 'placement_cache_file'
    placement_index = 0
    placement_num_index = 0

    @staticmethod
    def __init__(self):
        PlacementExtractor.fid = Extractor.load_cache(PlacementExtractor.raw_cache_name)
    
    @staticmethod
    def extract(line):
        model = RawData(line)
        key = model.ip
        fields = list()

        fields.append(model.placement_id)
        Extractor.solid(key, fields, PlacementExtractor.fid)
    
    @staticmethod
    def merge():
        fid = open(PlacementExtractor.raw_cache_name, 'r')
        placement_tuple = Extractor.read_line(fid)

        placement_info_dict = dict()

        while placement_tuple is not None:
            for ip in placement_tuple:
                if placement_info_dict.has_key(ip):
                    placement_info = placement_info_dict[ip]
                    placement_num = placement_info[PlacementExtractor.placement_num_index]
                    if placement_num.has_key(ip):
                        placement_num[ip] += 1
                    else:
                        placement_num = 1
                else:
                    placement_info = list()
                    placement_num = dict()
                    placement_info.append(placement_num)
                    placement_num[tuple[ip]] = 1
                    placement_info_dict[ip] = placement_info
        
        fid = open(PlacementExtractor.cache_name, 'w')
        fid.writelines(json.dumps(placement_info_dict))
    
    @staticmethod
    def get_placement_info_dict():
        fid = open(PlacementExtractor.cache_name, 'r')
        placement_info_dict = json.loads(fid.readline().replace('\n', ''))
        return placement_info_dict
    
    @staticmethod
    def get_placement_num_info(ip):
        placement_info_dict = PlacementExtractor.get_placement_info_dict()
        placement_num_info = placement_info_dict[ip][PlacementExtractor.placement_num_index]
        return placement_num_info
    
    @staticmethod
    def get_avg_click_placements(ip):
        placement_num_info = PlacementExtractor.get_placement_num_info(ip)
        total_count = 0
        for placement_id in placement_num_info:
            total_count += placement_num_info[placement_id]
        
        return 1.0 / total_count
    
    @staticmethod
    def get_var_click_placements(ip):
        placement_num_info = PlacementExtractor.get_placement_num_info(ip)
        click_nums = list()
        for placement_id in placement_num_info:
            click_nums.append(placement_num_info[placement_id])
        placement_std = np.reshape(click_nums, (-1, 1)).std()
        return placement_std
    
    @staticmethod
    def get_max_click_placements(ip):
        placement_num_info = PlacementExtractor.get_placement_num_info(ip)
        max_click = 0
        for placement_id in placement_num_info:
            if max_click < placement_num_info[placement_id]:
                max_click = placement_num_info[placement_id]
        return max_click