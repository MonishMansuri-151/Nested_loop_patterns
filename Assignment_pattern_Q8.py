# print the
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# for i in range(5, 0, -1):
#     for k in range(5, i, -1):
#         print(" ", end="")
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()
# 2
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")

    print()
for i in range(5, 0, -1):
    for j in range(2, i + 1):
        print("*", end="")
    print()
