# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from extract.RawDataModel import RawData


class Extractor(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    @staticmethod
    def extract(line):
        pass

    @abstractmethod
    @staticmethod
    def merge():
        pass


class TimeExtractor(Extractor):
    @staticmethod

    def extract(line):
        model=RawData(line)
        pass

    @staticmethod
    def merge():
        pass
