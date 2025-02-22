# n = 123
# a = 0
# while n != 0:
#     a *= 10
#     a += n % 10
#     n //= 10
# print(a)

n = 123
for i in range(1, n):
    n //= 10
    if n == 0:
        print(i)
        break
