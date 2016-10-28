# -*- coding: utf-8 -*-

from Feature_builder.RawDataModel import RawData
import mysql.connector
import os
import pickle
from Helper import Context

raw_data_file = "tainset"


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
