# -*- coding: utf-8 -*-
from multiprocessing import Pool
import getLines
from extract import SecExtractor


def preprocess(file_name, preprocess_function, lines_num,feature_n):
    # type: (str, function) -> void
    file = open(file_name)
    line = file.readline()
    index = 0
    while line != "":
        preprocess_function(line)
        index += 1
        if index % (lines_num / 100) == 0:
            print "feature"+str(feature_n)+"  :%.2f " % (index / (float(lines_num) / 100)) + " %"


if __name__ == "__main__":
    feature_n = 0
    process_pool = Pool()
    file_name = ""
    # TODO: replace file name
    extractor_list = list()
    # TODO: put concrete_extractor into list
    for concrete_extractor in extractor_list:
        feature_n+=1
        process_pool.apply_async(preprocess, args=(file_name, concrete_extractor.extract, getLines.getLines(file_name),feature_n))
    process_pool.close()
    process_pool.join()
    process_pool = Pool()
    for concrete_extractor in extractor_list:
        process_pool.apply_async(concrete_extractor.merge)
    process_pool.close()
    process_pool.join()
