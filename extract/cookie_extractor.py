# -*- coding: utf-8 -*-

from extract import Extractor
from extract import RawData

class CookieExtractor(Extractor):

    file_name = "cookie_cache_file"

    @staticmethod
    def init():
        Extractor.create_file(file_name)

    @staticmethod
    def extract(line):
        model = RawData(line)
        key = model.ip
        

    @staticmethod
    def merge():
        pass