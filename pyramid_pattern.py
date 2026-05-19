# print patterns
#     1
#    123
#   12345
#  1234567
# 123456789
# n = 5
# count = 0
# for i in range(1, n + 1):
#     for k in range(n, i, -1):
#         print(" ", end="")
#     for j in range(1, 2 * i):
#         print(j, end="")

#     count += 1
#     print()

# 2
#     A
#    A B
#   A B C
#  A B C D
# A B C D E
# n = 5
# for i in range(1, n + 1):
#     ch = 65
#     # for k in range(n, i, -1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         print(chr(ch), end=" ")
#         ch = ch + 1
#     print()
# 3
#     *
#    * *
#   *   *
#  *     *
# *********
# n = 5
# count = 0
# for i in range(1, n + 1):
#     # for k in range(n, i, -1):
#     print(" " * (n - i), end="")
#     for j in range(1, 2 * i):
#         if i == n or j == 1 or j == count + 1:
#             print(j, end="")
#         else:
#             print(" ", end="")
#     count += 2
#     print()
# 4
# ye apni approch se he
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# n = 5
# count = 0
# for i in range(n, 0, -1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     count += 2
#     print()
# 5
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# same code tushar sir ki approch se he
n = 5
hypen_count = 0
star_count = 0

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(" ", end="")

    for k in range(1, 2 * n - star_count):
        if k % 2 != 0:
            print("*", end="")
        else:
            print(" ", end="")

    hypen_count += 1
    star_count += 2

    print()
