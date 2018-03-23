#!/usr/bin/python3
#- * -coding: utf - 8 - * -

import os
import re

try:
	import notify2
except ImportError:
	raise ImportError("run pip3 install notify2")

notify2.init('Monitor Sensors')

#def read_sensor_data():
# save output of sensors in data
data = os.popen('sensors').read()

# split data into dict
list_to_parse = data.split()

# save each temp in its variable
# sensors_temp = []
# count = 0
# print(sensors_temp)
# for sensor in list_to_parse:
	# sensors_temp.append(sensor[7])
	# # sensors_temp.append(sensor[16])
	# sensors_temp.append(sensor[25])
	# sensors_temp.append(sensor[37])



# print("This comes from the list {}".format(sensors_temp))
temp1 = list_to_parse[7]
temp2 = list_to_parse[16]
temp3 = list_to_parse[25]
temp4 = list_to_parse[37]

	# init notifications

# parse temp func

def parse_temp(temp1, temp2, temp3, temp4):

	temp1 = re.findall('[^\d](?P<deg>\d+)[^\d]', temp1)
	temp2 = re.findall('[^\d](?P<deg>\d+)[^\d]', temp2)
	temp3 = re.findall('[^\d](?P<deg>\d+)[^\d]', temp3)
	temp4 = re.findall('[^\d](?P<deg>\d+)[^\d]', temp4)

	temp1 = int(str(temp1[0]))
	temp2 = int(str(temp2[0]))
	temp3 = int(str(temp3[0]))
	temp4 = int(str(temp4[0]))

	return temp1, temp2, temp3, temp4


# max temp allowed
max_temp = 75

# temperatures
temp1, temp2, temp3, temp4 = parse_temp(temp1, temp2, temp3, temp4)

# define function to check temp
def check_temp(max_temp, temp1, temp2, temp3, temp4):

	# compare the sensors temp with the max temp, this can be done better with a list.
    if max_temp < temp1 or max_temp < temp2 or max_temp < temp3 or max_temp < temp4:
        n = notify2.Notification("Summary", data, "notification-message-im")
        n.show()
        print("WARNING!", max(temp1, temp2, temp3, temp4))
        print("The max temperature that is allowed {}".format(max_temp))
    else:
        print("well nothing")


def main():
    check_temp(max_temp, temp1, temp2, temp3, temp4)


if __name__ == '__main__':
    main()
