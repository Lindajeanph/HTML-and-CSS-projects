import shutil
import os
import time
import sys
import datetime
import glob
from datetime import timedelta
destination = 'C:/Users/bposs/Documents/MonitoredFiles/'
source = 'C:/Users/bposs/Documents/DailyFiles/'


a = os.listdir(source)

for i in a:
    b = os.path.join(source, i)
    c = datetime.datetime.now() - timedelta(hours=24)
    d = os.path.getmtime(b)
    e = datetime.datetime.fromtimestamp(d)
    if e >= c:
        shutil.move(b, destination)
        print(i)
        





    



