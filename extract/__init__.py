# -*- coding: utf-8 -*-
import os
from abc import ABCMeta, abstractmethod
from extract.RawDataModel import RawData
import pickle
import json
import numpy


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

