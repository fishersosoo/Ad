# -*- coding: utf-8 -*-

import RawDataModel as rdm

file_name = '/Users/ASH/Desktop/Ad/dataExtract/read.csv'
fid = open(file_name, 'r')

# context data

tag_click_dic = dict()
totoal_click = 0

def avg_tag_click_percent(want):
    init_tag_context(fid, want)

    tags = tag_click_dic.keys()
    num_tag = len(tags)

    return 1 / num_tag

def var_tag_click_percent(want):
    pass

# file open

def repoen():
    fid = open(file_name, 'r')

# helper 

def init_tag_context(fid, want):
    get_tag_click_dict(fid, want)


def get_tag_click_dict(fid, want):

    global totoal_click
    global  totoal_click


    line = fid.readline();

    while line != '':
        # convert to model
        model = rdm.RawData(line)

        if model.ip == want:
            # increment click count
            totoal_click += 1

            # record tag click
            tag_id = '' #Context.media_info(model.media_id)
            if tag_click_dic.has_key(tag_id):
                tag_click_dic[tag_id] += 1
            else:
                tag_click_dic[tag_id] = 1

        #  next line
        line = fid.readline()

if __name__ == '__main__':
    avg_tag_click_percent(' 61.9.156.247')