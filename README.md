# CodeStat
Count the lines of code in your files.

## 1.Run

>  Python 3.9

> ```python
> import os
> from os import path
> import Stat
> 
> FilePath = input('请输入统计目录：') # 输入目录
> Stat.scaner_file(FilePath, True)
> Stat.g_stat()
> ```

通过scaner_file的第二个参数控制是否遍历子目录；

### Stat

* Stat.py

> ```python
> import Stat
> ```

### function

* Stat.py

> ```python
> def scaner_file(scPath, isDir):
> ```

> ```python
> def g_stat():
> ```

> ```python
> def stat_code(file):
> ```