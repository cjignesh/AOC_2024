with open("input1") as f:
    nums = f.readlines()
col1 = [int(i.split()[0]) for i in nums]
col2 = [int(i.split()[1]) for i in nums]
total_sum = sum(i*col2.count(i) for i in col1)
print(total_sum)
#23082277
