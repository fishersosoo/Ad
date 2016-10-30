# -*- coding: utf-8 -*-

from Extractor import Extractor
# from Feature_build import RawData
import RawDataModel

class TagExtractor(Extractor):

    @staticmethod
    def extract(line):
        model = RawDataModel.RawData(line)
        Extractor.creat_file("")
        pass

    @staticmethod
    def merge():
        pass