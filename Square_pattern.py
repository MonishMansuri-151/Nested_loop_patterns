# 1. Square Pattern

# 👉 ऐसा output print करो:

# * * *
# * * *
# * * *
# for i in range(1, 4):
#     for j in range(1, 4):
#         print("*", end=" ")
#     print(" ")
# .............................................
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(1, end=" ")
#     print(" ")
# ..........................................................
# for i in range(1, 4):
#     for j in range(1, 6):
#         print(j, end=" ")
#     print(" ")
# ...........................................................

# for i in range(1, 4):
#     for j in range(4, 0, -1):
#         print(j, end=" ")
#     print(" ")
# ...................................................

# for i in range(1, 5):
#     for j in range(1, 5):
#         print(i, end=" ")
#     print(" ")
# ..............................................................

# for i in range(5, 1, -1):
#     for j in range(1, 4):
#         print(i, end=" ")
#     print(" ")
# ..................................................................
# n = 1
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(n, end=" ")
#         n = n + 1
#     print(" ")
# ..............................................................
# n = 9
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(n, end=" ")
#         n = n - 1
#     print(" ")
# ............................................................

# ch = 65
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(chr(ch), end=" ")
#     print(" ")
#     ch = ch + 1

# ................................................................


ch = 65
for i in range(1, 4):
    for j in range(1, 4):
        print(chr(ch), end=" ")
    print(" ")
    ch = ch + 1
