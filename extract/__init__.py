# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Extractor(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    @staticmethod
    def extract(raw_data):
        pass

    @abstractmethod
    @staticmethod
    def merge():
        pass
