# print this pattern
# A
# AB
# ABC
# ABCD
# ABCDE

# 1
# for i in range(1, 6):
#     ch = 65
#     for j in range(1, i + 1):
#         print(chr(ch), end="")
#         ch = ch + 1
#     print()

# A
# BB
# CCC
# DDDD
# EEEEE

# 2
# .....................................................
# ch = 65
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(chr(ch), end="")
#     ch = ch + 1
#     print()

# print this pattern
# E
# D E
# C D E
# B C D E
# A B C D E

# 3
for i in range(1, 6):
    ch = 69 - i + 1
    for j in range(1, i + 1):
        s = chr(ch)
        print(s, end=" ")
        ch = ch + 1
    print()
