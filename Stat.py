import os
from os import path

g_count = 0
g_len = 0
count = -1


def scaner_file(scPath, isDir):
    global g_len, g_count
    len = 0
    file = os.listdir(scPath)
    for f in file:
        real = path.join(scPath, f)
        if path.isfile(real):  # 文件遍历
            len += 1
            g_len += 1
            stat_code(real)  # print(real)  # scaner_file(real)
        elif path.isdir(real):  # 目录遍历
            if isDir:
                scaner_file(real, isDir)
        else:
            pass
    g_count += count
    print(scPath, '\t总代码量：', count, '\t访问到文件数：', len)


def g_stat():
    global g_count, g_len
    print('\t代码总量：', g_count, '文件总量：', g_len)


def stat_code(file):
    global count
    for count, line in enumerate(open(file, 'rb')):
        pass
    count += 1
