# -*- coding: utf-8 -*-
import time
from multiprocessing import Pool
from tqdm import *

feature_n=0
def do():
    print feature_n

if __name__ == "__main__":
    # process_pool=Pool()
    # for x in range(3):
    #     process_pool.apply_async(do,args=(str(x),))
    # process_pool.close()
    # process_pool.join()
    k=8743
    index=0
    print feature_n
    feature_n=3
    do()
    for x in range(k):
        index += 1
        if index % (k / 100) == 0:
            print "%.2f "%(index/(float(k) / 100))+" %"+str(index)
        # time.sleep(0.1)

#     Context.build()
#     # change the table name to read the raw data from database
#     data_source = "trainset"
#     features_output = open(r"{0}_features.csv".format(data_source), 'w')
#     ip_list = get_all_ip(data_source)
#     for ip in ip_list:
#         features_output.write("{0},".format(str(get_total_click(ip))))
#         features_output.write("{0},".format(str(get_avg_click_sec(ip))))
#         features_output.write("{0},".format(str(get_var_click_sec(ip))))
#         features_output.write("{0},".format(str(get_avg_click_min(ip))))
#         features_output.write("{0},".format(str(get_var_click_min(ip))))
#         features_output.write("{0},".format(str(get_avg_click_hour(ip))))
#         features_output.write("{0},".format(str(get_var_click_hour(ip))))
#         features_output.write("{0},".format(str(get_avg_click_mediaid(ip))))
#         features_output.write("{0},".format(str(get_var_click_mediaid(ip))))
#         features_output.write("{0},".format(str(get_max_click_mediaid(ip))))
#         features_output.write("{0},".format(str(get_avg_click_tag(ip))))
#         features_output.write("{0},".format(str(get_var_click_tag(ip))))
#         features_output.write("{0},".format(str(get_max_click_tag(ip))))
#         features_output.write("{0},".format(str(get_avg_click_cookies(ip))))
#         features_output.write("{0},".format(str(get_var_click_cookies(ip))))
#         features_output.write("{0},".format(str(get_total_dev(ip))))
#         features_output.write("{0},".format(str(get_avg_click_dev(ip))))
#         features_output.write("{0},".format(str(get_var_click_dev(ip))))
#         features_output.write("{0},".format(str(get_max_click_dev(ip))))
#         features_output.write("{0},".format(str(get_total_placement(ip))))
#         features_output.write("{0},".format(str(get_avg_click_placement(ip))))
#         features_output.write("{0},".format(str(get_var_click_placement(ip))))
#         features_output.write("{0},".format(str(get_max_click_placement(ip))))
#         features_output.write("{0},".format(str(get_total_cookies(ip))))
#         features_output.write("{0},".format(str(get_avg_new_cookies_day(ip))))
#         features_output.write("{0},".format(str(get_total_ua(ip))))
#         features_output.write("{0},".format(str(get_avg_click_ua(ip))))
#         features_output.write("{0},".format(str(get_var_click_ua(ip))))
#         features_output.write("{0},".format(str(get_max_click_ua(ip))))
#         features_output.write("{0},".format(str(get_entropy_click_ua(ip))))
#         features_output.write("{0}\n".format(str(get_flag(ip))))
#         features_output.flush()
#     features_output.close()
