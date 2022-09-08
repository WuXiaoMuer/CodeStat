import os
from os import path
import Stat

FilePath = input('请输入统计目录：') # 输入目录
Stat.scaner_file(FilePath, True)
Stat.g_stat()
