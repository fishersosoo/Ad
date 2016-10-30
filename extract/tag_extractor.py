# -*- coding: utf-8 -*-

from extract import Extractor
from extract import RawData


class TagExtractor(Extractor):
    file_name = "tag_cache_file"

    @staticmethod
    def init():
        Extractor.create_file(TagExtractor.file_name)

    @staticmethod
    def extract(line):
        model = RawData(line)
        key = model.ip

        # MEDIA_ID 
        fields = list()
        fields.append(model.media_id)

    @staticmethod
    def merge():
        cache_file = open(TagExtractor.file_name, 'r')
        pair = Extractor.read_line(cache_file)

    if __name__ == '__main__':
        print('xixi')
