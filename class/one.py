# # reverse of 3 digits numbers
#
#
# a = 123456
# rev = 0
# l = a % 10
# rev += l
# rev *= 10
# a = a // 10
#
# l = a % 10
# rev += l
# rev *= 10
# a = a // 10
#
# l = a % 10
# rev += l
# rev *= 10
# a = a // 10
#
# l = a % 10
# rev += l
# rev *= 10
# a = a // 10
#
# l = a % 10
# rev += l
# rev *= 10
# a = a // 10
# l = a % 10
# rev += l
# a = a // 10
#
# print(rev)
#
# print("")
#
#
# a = 123456788
# l = a % 10
# f = a // 10**8
# print(l + f)
#
# # a = eval(input("Abc:"))
# # print(type(a))
#
# a, b, c, d, e = 1, 2, 3, 4, 5
#
# gr = b
#
# if a > b:
#     gr = a
#
# if c > gr:
#     gr = c
#
# if d > gr:
#     gr = d
#
# if e > gr:
#     gr = e
#
# print(gr)
# print(ord("0"))
# print("世界")
#
# ch = "a"
#
# rel = ord(ch)
#
# if rel >= 65 and rel <= 90:
#     print("Upper Case")
# elif rel >= 97 and rel <= 122:
#     print("Lower Case")
# elif rel >= 48 and rel <= 57:
#     print("Digits")
# else:
#     print("Special Char")
#
# a = 12344
# rev = 0
#
# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10
#
# print(rev)
#
# sum = 0
# while rev > 0:
#     sum = sum + rev % 10
#     rev = rev // 10
# print(sum)
#
# a = 12300
# counter = 0
# while a > 0:
#     counter += 1
#     a = a // 10
# print(counter)
#
# orig = 153
# arm = 153
# sum1 = 0
# l = len(str(orig))
#
# while arm > 0:
#     sum1 = sum1 + (arm % 10) ** l
#     arm = arm // 10
#
# print(sum1)
# if sum1 == orig:
#     print("Number is armstrong")
# else:
#     print("Number is not armstrong")


# Peterson Number
a = 145
orig = 145
sum1 = 0
while a > 0:
    l = a % 10
    fact = 1
    while l > 0:
        fact *= l
        l -= 1
    sum1 += fact
    a = a // 10

if sum1 == orig:
    print("Number is Peterson")
else:
    print("Not Peterson")


# Tech Number
a = 2025
l = a % 100
f = a // 100
print((f + l) * (f + l))
if a == (f + l) * (f + l):
    print("It is a tech number")
else:
    print("Not a tech number")


# accept an ammount - generate its change [denomination]
print()
