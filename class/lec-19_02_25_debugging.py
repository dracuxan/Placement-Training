# 1
i = 0
while i < 5:
    print(i)
    i += 1

# 2
for i in range(10, 1, -1):
    print(i)

# 3
for i in range(1, 6):
    print(i)

# 4
# nums = [1, 2, 3, 4, 5]
# for n in nums:
#     if n % 2 == 0:
#         nums.remove(n)
# print(nums)

nums = [1, 2, 3, 4, 5]
# 5
for i in range(len(nums) - 2):
    if nums[i] % 2 == 0:
        nums.pop(i)
print(nums)

# 6
c = 10
while c > 0:
    c -= 1
    print(c)

# 7
for i in range(3):
    for j in range(3):
        print(i, j)

# 8
for n in nums:
    if n % 2 == 0:
        print(n)
    else:
        print("No")


# 9
