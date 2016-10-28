# -*- coding: utf-8 -*-
from extract import RawDataModel

if __name__=="__main__":
    raw_data_file=open("file")
    # TODO: replace file name
    extractor_list=list()
    # TODO: put thing into list
    line = raw_data_file.readline()
    while line != "":
        raw_data_model= RawDataModel.RawData(line)
        line=raw_data_file.readline()
        for x in extractor_list:
            x.extract(raw_data_model)
            x.merge()

