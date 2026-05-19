# print this pattern
# 1 2 3 4 5
#   1 2 3 4
#     1 2 3
#       1 2
#         1
# for i in range(5, 0, -1):
#     for k in range(5, i, -1):
#         print(" ", end=" ")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# 2
# A B C D E
#   A B C D
#     A B C
#       A B
#         A
for i in range(5, 0, -1):
    ch = 65
    for k in range(5, i, -1):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print(chr(ch), end=" ")
        ch = ch + 1
    print()
