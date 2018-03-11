#!/usr/bin/python3

import os
import notify2

# save output of sensors in data
data = os.popen('sensors').read()

# split data into dict
list_to_parse = data.split()

# save each temp in its variable
temp1 = list_to_parse[7]
temp2 = list_to_parse[16]
temp3 = list_to_parse[25]
temp4 = list_to_parse[37]

# we define max temp
max_temp = 75

# TODO, before if need to convert temp to floats

if max_temp > int(temp1) or max_temp > int(temp2) or max_temp > int(
        temp3) or max_temp > int(temp4):
    print("WARNING!")

# init notifications
notify2.init('app name')

# create notification
n = notify2.Notification("Summary", data, "notification-message-im")

#for i in list_to_parse:
#    print("This is an item {}".format(i))

counter = 0

#for i in list_to_parse:
#    print(counter,i)
#    counter = counter + 1

print(list_to_parse[7])
print(list_to_parse[16])
print(list_to_parse[25])
print(list_to_parse[37])
print(data)


def main():
    n.show()


if __name__ == '__main__':
    main()
