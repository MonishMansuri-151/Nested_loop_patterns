# this pattern
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# for i in range(1, 6):
#     for k in range(5, i, -1):
#         print(" ", end="")
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()
# 2
#     *
#    * *
#   *   *
#  *     *
# * * * * *
for i in range(1, 6):
    for k in range(5, i, -1):
        print(" ", end="")
    for j in range(1, i + 1):
        if i == 1 or i == 5 or j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
