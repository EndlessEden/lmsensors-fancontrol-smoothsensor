#!/usr/bin/python3

import time, os

# temperature smoothener for fancontrol

dt = 0.3    # time interval between measurement points
points = 10 # smoothing decay time in points

sensors = ["/sys/class/hwmon/hwmon5/temp3_input ",
           "/sys/class/hwmon/hwmon7/temp2_input",
           "/sys/class/hwmon/hwmon7/temp4_input",
           "/sys/class/hwmon/hwmon7/temp5_input",
           "/sys/class/hwmon/hwmon7/hwmon2/temp1_input"
           "/sys/class/hwmon/hwmon7/hwmon3/temp1_input"
           "/sys/class/hwmon/hwmon7/hwmon4/temp1_input"
           "/sys/class/hwmon/hwmon7/hwmon8/temp1_input"
           "/sys/class/hwmon/hwmon7/hwmon9/temp1_input"
           "/sys/class/hwmon/hwmon7/hwmon10/temp1_input"
	   "/sys/class/hwmon/hwmon7/hwmon11/temp1_input"
	   "/sys/class/hwmon/hwmon7/hwmon12/temp1_input"
	   "/tmp/gputemp1_input"]

outfile = os.path.expanduser("/etc/smoothtemp.txt")

if __name__ == "__main__":
    temp = int(open(sensors[0]).read())
    k = 1. / points
    K = 1 - k
    k = k / len(sensors)
    print(K, k)
    if not os.path.exists(outfile):
        open(outfile, "w").close()
    myfile = open(outfile,'r+')
    while True:
        time.sleep(dt)
        t = 0
        for s in sensors:
            t += int(open(s).read())
        temp = temp * K + t * k
        myfile.seek(0)
        myfile.write(str(int(temp)) + "\n\n")
        myfile.truncate()
