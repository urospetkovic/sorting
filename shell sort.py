import random
import time

num_list = []
for x in range(100000):
    num_list.append(random.randint(1, 1000))
test = sorted(num_list)


def shell_compare(x, h):  # compares two neighbour numbers
    while x + h < len(num_list) and num_list[x] > num_list[x + h]:
        num_list[x], num_list[x + h] = num_list[x + h], num_list[x]  # swap places if needed
        if x - h >= 0:
            x -= h  # if not first in list, compare with one behind


def shell_sort(num_list):
    h = 1
    h_list = []
    while h < len(num_list):
        h_list.append(h)
        h = h * 3 + 1
    h_list = h_list[::-1]
    for h in h_list:
        for x in range(len(num_list) - 1):
            shell_compare(x, h)


start = time.time()
shell_sort(num_list)
end = time.time()
elapsed = float(end - start).__round__(3)
print('Shell sort time:', elapsed)
if test == num_list:
    print(True)
else:
    print(False)

