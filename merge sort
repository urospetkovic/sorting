import random
import time

list1 = []
list2 = []
for x in range(10000):
    list1.append(random.randint(1, 10000))
    list2.append(random.randint(1, 10000))
list1 = sorted(list1)
list2 = sorted(list2)
list3 = list1 + list2
test = sorted(list3)
list4 = []
lo = 0
mid = (int(len(list3)))/2
hi = int(len(list3))-1
i = lo
j = int(mid)
k = 0

start = time.time()
while k < hi:
    if list1[len(list1)-1] <= list2[0]:  # if already sorted
        list4 = list3
        print('Already sorted')
        break
    if list3[i] > list3[j]:
        list4.append(list3[j])
        j += 1
        k += 1
    elif list3[i] < list3[j] or list3[i] == list3[j]:
        list4.append(list3[i])
        i += 1
        k += 1
    if i == mid:
        list4.extend(list3[j:])
        break
    if j == hi+1:
        list4.extend(list3[i:int(mid)])
        break

end = time.time()
elapsed = float(end - start).__round__(3)
print('Time:', elapsed)

if test == list4:
    print(True)
else:
    print(False)
