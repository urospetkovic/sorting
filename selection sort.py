num_list = [12, 45 ,75, 3, 88, 96, 21, 46, 79, 4]
sort_list = []
print(num_list)

i = min(num_list)
for re in range(len(num_list)):
    for x in num_list:
        if x == i:
            sort_list.append(x)
            num_list.remove(x)
            if len(num_list) == 0:
                break
        i = min(num_list)

print(sort_list)
