# -*- coding: utf-8 -*-

from Feature_builder.RawDataModel import RawData
from Feature_builder.Helper import Context
import mysql.connector
import os
import pickle

raw_data_file="tainset"

def get_all_ip(table):
    """
    :param table: str
    :rtype: list
    :return: list of ip
    """
    ip_list = list()
    conn = mysql.connector.connect(user='root', password='1995', database='admaster', use_unicode=True)
    cursor = conn.cursor()
    cursor.execute(r"select distinct(%s.ip) from %s", (table, table))
    result = cursor.fetchall()
    for one in result:
        ip_list.append(one)
    conn.commit()
    cursor.close()
    return ip_list


def line_to_model(line):
    """
    :param line: str
    :rtype: RawData
    """
    model = RawData(line)
    return model


def get_total_click(ip):
    """
    :param ip: str
    :rtype: int
    """
    if Context.ip_total==None:
        if os.path.exists("ip_click"):
            # has calculated ip_click, load
            Context.ip_total=dict()
            file=open("ip_click",'rb')
            Context.ip_total=pickle.loads(file)
            return Context.ip_total[ip]
        else:
            # has not calculated the
            Context.ip_total = dict()
            a=dict()
            file=open(raw_data_file)
            line  = file.readline()
            index=0
            while line!="":
                model=RawData(line)
                if Context.ip_total.has_key(model.ip):
                    Context.ip_total[ip]=1
                else:
                    Context.ip_total[ip]+=1
                line=line.readlines
    else:
        return Context.ip_total[ip]



    pass


def get_avg_click_sec(ip):
    """
    :param ip: str
    :rtype: float
    :return: percentage
    """
    pass


def get_var_click_sec(ip):
    """
    :param ip: str
    :rtype: float
    :return: number
    """
    pass


def get_avg_click_min(ip):
    """
    :param ip: str
    :rtype: float
    :return: percentage
    """
    pass


def get_var_click_min(ip):
    """
    :param ip: str
    :rtype: float
    :return: num
    """
    pass


def get_avg_click_hour(ip):
    """
    :param ip: str
    :rtype: float
    :return: percentage
    """
    pass


def get_var_click_hour(ip):
    """
    :param ip: str
    :rtype: float
    :return: num
    """
    pass


def get_avg_click_mediaid(ip):
    """
    :param ip: str
    :rtype: float
    :return: percentage
    """
    pass


def get_var_click_mediaid(ip):
    """
    :param ip: str
    :rtype: float
    :return: num
    """
    pass


def get_max_click_mediaid(id):
    """
    :param ip: str
    :rtype: float
    :return: percentage
    """
    pass


def get_avg_click_tag(id):
    """
    :param ip: str
    :rtype: float
    :return: percentage
    """
    pass


def get_var_click_tag(id):
    """
    :param ip: str
    :rtype: float
    :return: num
    """
    pass


def get_max_click_tag(id):
    """
    :param ip: str
    :rtype: float
    :return: percentage
    """
    pass


def get_avg_click_cookies(ip):
    """
    :param ip: str
    :rtype: float
    :return: percentage
    """
    pass


def get_var_click_cookies(ip):
    """
    :param ip: str
    :rtype: float
    :return: num
    """
    pass


def get_total_dev(ip):
    """
    :param ip: str
    :rtype: float
    :return: num
    """
    pass


def get_avg_click_dev(ip):
    """
    :param ip: str
    :rtype: float
    :return: percentage
    """
    pass


def get_var_click_dev(ip):
    """
    :param ip: str
    :rtype: float
    :return: num
    """
    pass


def get_max_click_dev(ip):
    """
    :param ip: str
    :rtype: float
    :return: percentage
    """
    pass


def get_total_placement(ip):
    """
    :param ip: str
    :rtype: float
    :return: num
    """
    pass


def get_avg_click_placement(ip):
    """
    :param ip: str
    :rtype: float
    :return: percentage
    """
    pass


def get_var_click_placement(ip):
    """
    :param ip: str
    :rtype: float
    :return: num
    """
    pass


def get_max_click_placement(ip):
    """
    :param ip: str
    :rtype: float
    :return: percentage
    """
    pass


def get_total_cookies(ip):
    """
    :param ip: str
    :rtype: float
    :return: num
    """
    pass


def get_avg_new_cookies_day(ip):
    """
    :param ip: str
    :rtype: float
    :return: percentage
    """
    pass


def get_total_ua(ip):
    """
    :param ip: str
    :rtype: float
    :return: num
    """
    pass


def get_avg_click_ua(ip):
    """
    :param ip: str
    :rtype: float
    :return: percentage
    """
    pass


def get_var_click_ua(ip):
    """
    :param ip: str
    :rtype: float
    :return: num
    """
    pass


def get_max_click_ua(ip):
    """
    :param ip: str
    :rtype: float
    :return: percentage
    """
    pass


def get_entropy_click_ua(ip):
    """
    :param ip: str
    :rtype: float
    :return: num
    """
    pass


def get_flag(ip):
    """
    :param ip: str
    :rtype: bool
    """
    pass
