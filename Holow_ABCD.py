# print holo abcd
# A
# A B
# A   C
# A     D
# A B C D E
# for i in range(1, 6):
#     ch = 65
#     for j in range(1, i + 1):
#         if i == 1 or i == 5 or j == 1 or j == i:
#             print(chr(ch), end=" ")
#         else:
#             print(" ", end=" ")
#         ch = ch + 1
#     print()
# 2
# A
# B C
# D   F
# G     J
# K L M N O
ch = 65
for i in range(1, 6):
    for j in range(1, i + 1):
        if i == 1 or i == 5 or j == 1 or j == i:
            print(chr(ch), end=" ")
        else:
            print(" ", end=" ")
        ch = ch + 1
    print()
