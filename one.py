# reverse of 3 digits numbers


a = 123456
rev = 0
l = a % 10
rev += l
rev *= 10
a = a // 10

l = a % 10
rev += l
rev *= 10
a = a // 10

l = a % 10
rev += l
rev *= 10
a = a // 10

l = a % 10
rev += l
rev *= 10
a = a // 10

l = a % 10
rev += l
rev *= 10
a = a // 10
l = a % 10
rev += l
a = a // 10

print(rev)

print("")


a = 123456788
l = a % 10
f = a // 10**8
print(l + f)

a = eval(input("Abc:"))
print(type(a))
