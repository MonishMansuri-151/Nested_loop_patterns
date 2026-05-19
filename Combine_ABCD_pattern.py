# print pattern
# - - - A
# - - B C
# - C D E
# D E F G

# for i in range(1, 5):
#     ch = 65 + i - 1
#     for k in range(4, i, -1):
#         print("-", end=" ")
#     for j in range(1, i + 1):
#         print(chr(ch), end=" ")
#         ch = ch + 1
#     print()
# 2
# A B C D E
# A B C D 1
# A B C 1 2
# A B 1 2 3
# A 1 2 3 4
for i in range(5, 0, -1):
    ch = 65
    for j in range(1, i + 1):
        print(chr(ch), end=" ")
        ch = ch + 1
        n = 1
    for k in range(5, i, -1):
        print(n, end=" ")
        n = n + 1
    print()
