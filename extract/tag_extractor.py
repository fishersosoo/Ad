# -*- coding: utf-8 -*-

from extract import Extractor
from extract import RawData
from extract import Context


class TagExtractor(Extractor):
    raw_cache_name = "cookie_raw_cache_file"
    cache_name = "cookie_cache_file"
    fid = None

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
    def merge():
        cache_file = open(TagExtractor.file_name, 'r')
        pair = Extractor.read_line(cache_file)

    if __name__ == '__main__':
        print('xixi')
