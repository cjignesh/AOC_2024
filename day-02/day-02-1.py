with open("input1") as f:
    nums = f.readlines()


def is_safe(row):
    diffs = [abs(row[i + 1] - row[i]) for i in range(len(row) - 1)]
    asc = all(row[i] < row[i+1] for i in range(len(row)-1))
    dsc = all(row[i] > row[i+1] for i in range(len(row)-1))
    safe_diff = all(1 <= diff <= 3 for diff in diffs)
    safe = True if (asc and safe_diff) or (dsc and safe_diff) else False
    return safe


rows = [[int(i) for i in num.split()] for num in nums]
safe = sum(1 for row in rows if is_safe(row))
print(safe)
#402