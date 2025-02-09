s = "learning string manupulations for python coding"
# print(s.startswith("learning"))
# print(s.endswith("coding"))


# Reverse of a string
# print(s)
# print("".join(reversed(s)))

# Reverse the string without using functions
# l = s.split(" ")

# for i in range(1, len(s) + 1):
#     j = len(s) - i
#     print(s[j], end="")
# print()

# for i in range(1, len(l) + 1):
#     j = len(l) - i
#     print(l[j], end=" ")
# for i in range(len(l)):
#     ns = l[i]
#     for i in range(1, len(ns) + 1):
#         x = len(ns) - i
#         print(ns[x], end="")
#     print(end=" ")
#
# print()
#
# for i in range(len(l)):
#     ns = l[i]
#     print(ns[::-1], end=" ")

# rel = ""
#
# for i in s:
#     if i not in rel:
#         rel += i + ""
#     continue
# print(rel)


# mob = input("Enter a valid number: ")
# starts = ["6", "7", "8", "9"]
#
# if not mob.isdigit():
#     print("Not a valid number")
#
# elif mob[0] not in starts:
#     print("mobile number not an indian number")
#
# elif len(mob) != 10:
#     print("Number not of 10 digits")
#
# else:
#     print("The number is valid")

# st1 = "Listen"
# st2 = "silent"
# st1 = st1.lower()
# st2 = st2.lower()
# new1 = list(st1)
# new2 = list(st2)
# new1 = sorted(new1)
# new2 = sorted(new2)
#
# if new1 == new2:
#     print("Anagram")
# else:
#     print("Not an Anagram")


# a, b = "heeel23o", "hello"
#
# na, nb = sorted(a), sorted(b)
# print(na, nb)
# opps = 0
# if len(na) == len(nb):
#     if na == nb:
#         print(opps)
#     else:
#         diff = ""
#         for i in nb:
#             if i not in na:
#                 diff += i
#                 opps += 1
#             continue
#         print(opps)
# else:
#     opps += abs(len(na) - len(nb))
#     print(opps)

# Pangram

l = "the quick brown fox jumps over the lazy dog"
st = ord("a")

for i in range(26):
    if l.count(chr(st)) > 0:
        st += 1
        continue
    print("Not all aplhabets")
    break

print("ALl alphabets present")
