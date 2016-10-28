# -*- coding: utf-8 -*-

class Context:
    table_name="trainset"
    ip_total = None
    media_info_file=open("media_info.csv")
    media_info=dict()
    def __init__(self):
        pass

    @staticmethod
    def build():
        line=Context.media_info_file.readline()
        while line != "":
            line = line.replace("\n","")
            line = line .split(",")
            Context.media_info[line[0]]=line[3]
            line=Context.media_info_file.readline()

