# -*- coding: utf-8 -*-

import RawDataModel as rdm

file_name = '/Users/ASH/Desktop/Ad/dataExtract/read.csv'
fid = open(file_name, 'r')

def avg_tag_click_percent(ip):
    line = fid.readline();
    while line != '':
        # convert to model
        model = rdm.RawData(line)

        print model.ip

        #  next line
        line = fid.readline()


if __name__ == '__main__':
    avg_tag_click_percent('')