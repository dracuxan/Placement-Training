# # 1
# for i in range(10):
#     print(i + 1)
#
# # 2
# for i in range(10):
#     print((i + 1) ** 2)
#
# # 3
# n = int(input("::"))
# sum1 = 0
# for i in range(n + 1):
#     sum1 += i
# print(sum1)
#
# # 4
# for i in range(1, n + 1):
#     prod = i * n
#     print(f"{n} * {i} = ", prod)
#
# # 5
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)
#
# # 6
# v = list("aeiou")
# st = input("::")
# number = 0
# present = []
# for k in st:
#     if k in v and k not in present:
#         number += st.count(k)
#         present.append(k)
# print(number)
#
# # 7
# for i in range(1, 21):
#     if i % 2 != 0:
#         print(i)
#
# # 8
# name_l = ["nisarg", "jayesh", "niraj"]
# for x in name_l:
#     print(f"{x} - len: {len(x)}")
#
# # 9
# l = len(st)
# for i in range(1, len(st) + 1):
#     print(st[l - i], end="")
# print()
#
# # 10
# word = input("Enter a Palindrome:")
# rev_word = ""
# for i in range(1, len(word) + 1):
#     j = len(word) - i
#     rev_word += word[j]
# if word == rev_word:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")
#
#
# # 11 & 12
# n = 10
# i = 0
# while i < n:
#     print(f"forward: {i+1}")
#     print(f"backward: {n-i}")
#     i += 1
#
# # 13
# n1 = "123"
# i = 0
# sumn = 0
# while i < len(n1):
#     sumn += int(n1[i])
#     i += 1
# print(sumn)

# # 14
# n = 6
# fact = n
# for i in range(1, n):
#     fact *= i
# print(fact)
#
# # 15
# while True:
#     q = input("Enter exit:")
#     if q == "exit":
#         break
#
# # 16
# for i in range(4):
#     for j in range(4):
#         print("*", end="")
#     print()

# 17
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
print()

# 19
for i in range(2, 4):
    for j in range(1, i + 1):
        print("*" * j)
