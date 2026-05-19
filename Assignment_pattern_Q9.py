# print this pattern
#    *
#   **
#  ***
# ****
#  ***
#   **
#    *
# for i in range(1, 4):
#     for k in range(4, i, -1):
#         print(" ", end="")
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()
# for i in range(4, 0, -1):
#     for k in range(4, i, -1):
#         print(" ", end="")
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()
# 2
# print this pattern
# but pirnt odd number
# *******
# -*****
# --***
# ---*
# n = 4
# for i in range(n, 0, -1):

#     for k in range(n, i, -1):
#         print("-", end="")
#     for j in range(1, 2 * i):
#         print("*", end="")
#     print()
#  3
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
n = 4
for i in range(1, n):
    # for k in range(n, i, -1):
    print(" " * (n - i), end="")
    for j in range(1, 2 * i):
        print("*", end="")

    print()

for i in range(n, 0, -1):
    # for k in range(n, i, -1):
    print(" " * (n - i), end="")
    for j in range(1, 2 * i):
        print("*", end="")

    print()
