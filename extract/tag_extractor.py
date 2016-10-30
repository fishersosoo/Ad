# -*- coding: utf-8 -*-

from extract import Extractor
from extract import RawData

class TagExtractor(Extractor):

    file_name = "tag_cache_file"

    @staticmethod
    def init():
        Extractor.create_file(file_name)

    @staticmethod
    def extract(line):
        model = RawData(line)
        key = model.ip

        # MEDIA_ID 
        fields = list()
        fields.append(model.media_id)

    @staticmethod
    def merge():
        pass

    
    if __name__ == '__main__':
        TagExtractor.init()