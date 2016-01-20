#something to do every two minutes

import time
import datetime
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

file_obj = open('/home/pi/crontest/crontest.txt', 'a')
file_obj.write(st)
file_obj.write(' timestamp test \n')
file_obj.close()


