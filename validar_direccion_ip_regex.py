import re


input_ip = input('Enter the ip:')

flag = 0

pattern = "^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$"
match = re.match(pattern, input_ip)
if (match):
    field = input_ip.split(".")
    for i in range(0, len(field)):
        if (int(field[i]) < 256):
            flag += 1
        else:
            flag = 0
if (flag == 4):
    print("valid ip")
else:
    print('No match for ip or not a valid ip')
