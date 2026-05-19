# print this pattern
#     * * * * *
#    * * * * *
#   * * * * *
#  * * * * *
# * * * * *
# for i in range(1, 6):
#     for k in range(5, i, -1):
#         print(" ", end="")
#     for j in range(1, 6):
#         print("*", end=" ")
#     print(" ")
# 2
#     1 2 3 4 5
#    1 2 3 4 5
#   1 2 3 4 5
#  1 2 3 4 5
# 1 2 3 4 5
# for i in range(1, 6):
#     for k in range(5, i, -1):
#         print(" ", end="")
#     for j in range(1, 6):
#         print(j, end=" ")
#     print(" ")
# 3
#     A B C D E
#    A B C D E
#   A B C D E
#  A B C D E
# A B C D E
for i in range(1, 6):
    ch = 65
    for k in range(5, i, -1):
        print(" ", end="")
    for j in range(1, 6):
        print(chr(ch), end=" ")
        ch = ch + 1
    print(" ")
