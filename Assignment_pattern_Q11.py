# print the pattern
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
# n = 5
# for i in range(1, n + 1):
#     for k in range(n, i, -1):
#         print("  ", end="")
#     for j in range(1, 2 * i):
#         print("* ", end="")
#     print("")
# for i in range(n - 1, 0, -1):
#     for k in range(n, i, -1):
#         print("  ", end="")
#     for j in range(1, 2 * i):
#         print("* ", end="")
#     print("")
# 2
#         1
#       1 2 3
#     1 2 3 4 5
#   1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8 9
#   1 2 3 4 5 6 7
#     1 2 3 4 5
#       1 2 3
#         1
# n = 5
# for i in range(1, n + 1):
#     for k in range(n, i, -1):
#         print("  ", end="")
#     for j in range(1, 2 * i):
#         print(j, end=" ")
#     print("")
# for i in range(n - 1, 0, -1):
#     for k in range(n, i, -1):
#         print("  ", end="")
#     for j in range(1, 2 * i):
#         print(j, end=" ")
#     print("")
# 3
# 1 2 3 4 5 6 7 8 9
#   1 2 3 4 5 6 7
#     1 2 3 4 5
#       1 2 3
#         1
#       1 2 3
#     1 2 3 4 5
#   1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8 9
# n = 5
# for i in range(n + 1 - 1, 0, -1):
#     for k in range(n, i, -1):
#         print("  ", end="")
#     for j in range(1, 2 * i):
#         print(j, end=" ")
#     print("")
# for i in range(2, n + 1):
#     for k in range(n, i, -1):
#         print("  ", end="")
#     for j in range(1, 2 * i):
#         print(j, end=" ")
#     print("")
# 4
# A B C D E F G H I
#   A B C D E F G
#     A B C D E
#       A B C
#         A
#       A B C
#     A B C D E
#   A B C D E F G
# A B C D E F G H I
n = 5
for i in range(n + 1 - 1, 0, -1):
    ch = 65
    for k in range(n, i, -1):
        print("  ", end="")
    for j in range(1, 2 * i):
        print(chr(ch), end=" ")
        ch += 1
    print("")
for i in range(2, n + 1):
    ch = 65
    for k in range(n, i, -1):
        print("  ", end="")
    for j in range(1, 2 * i):
        print(chr(ch), end=" ")
        ch += 1
    print("")
