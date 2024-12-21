with open("input1") as f:
    nums = f.readlines()

col1 = [int(i.split()[0]) for i in nums]
col2 = [int(i.split()[1]) for i in nums]
col1.sort()
col2.sort()
total_sum = sum(abs(col1[i] - col2[i]) for i in range(len(col1)))
print(total_sum)

#2375403
