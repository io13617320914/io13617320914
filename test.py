  import os
  import numpy as np
  import matplotlib.pyplot as plt
  from datetime import datetime

-# 如果没有文件夹就创建一个文件夹
-# sample_dir = 'hoework4.9'
-# if not os.path.exists(sample_dir)
-#      os.makedirs(sample_dir)
+# test修改文件

  #增加子文件夹和时间戳
  now_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%s')
  son_sample_dir = 'samples//{}',format(now_time)
  if not os.path.exists(son_sample_dir):