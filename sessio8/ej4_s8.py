nums = [0, -2, -4, -6, -7, -8, -9, 3, 2, 1, 0]

minimum = min(nums)

for i in nums:
    out = ''
    diff = i - minimum
    if i == 0:
        print(' ' * diff + "X")
    elif i < 0:
        print(' ' * diff + "X" + " " * (-i-1) + "|")
    elif i > 0:
        print(' ' * (diff-i) + "|" + " " * (i-1) + "X")

