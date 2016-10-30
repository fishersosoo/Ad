# -*- coding: utf-8 -*-
import os
from abc import ABCMeta, abstractmethod
from extract.RawDataModel import RawData
import pickle
import json
import numpy


class Context:
    media_info_file = None
    media_info_table = dict()

    # dict<media_id,list>
    def __init__(self):
        pass

    @staticmethod
    def load_media_info_file(self, csv_file):
        line = csv_file.readline()
        while line != "":
            line = line.replace("\n", "")
            line = line.splite(",")
            Context.media_info_table[line[0]] = [line[1], line[2], line[3], line[4]]
            line = csv_file.readline


class Extractor(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def extract(self, line):
        pass

    @abstractmethod
    def merge(self):
        pass
