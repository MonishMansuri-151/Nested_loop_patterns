# print pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# n = 6
# for i in range(1, n):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print(" ")

# 2
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# n = 5
# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print(" ")

# 3
# 1
# 1 2
# 1   3
# 1     4
# 1 2 3 4 5
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if i == 1 or i == n or j == 1 or j == i:
#             print(j, end=" ")
#         else:
#             print(" ", end=" ")
#     print(" ")
# 4
#         1
#       2 3 2
#     3 4 5 4 3
#   4 5 6 7 6 5 4
# 5 6 7 8 9 8 7 6 5
# n = 5
# var = 1
# for i in range(1, n + 1):
#     for k in range(n, i, -1):
#         print(" ", end=" ")
#     for j in range(1, i + 1):
#         print(i + j - 1, end=" ")
#     for m in range(i - 1, 0, -1):
#         print(i + m - 1, end=" ")

#     print(" ")
# 5
#         1
#       1   2
#     1       3
#   1           4
# 1 2 3 4 5 2 3 4 5
# n = 5
# var = 1
# for i in range(1, n + 1):
#     for k in range(n, i, -1):
#         print(" ", end=" ")

#     for j in range(1, i + 1):
#         if i == 1 or i == n or j == 1:
#             print(j, end=" ")
#         else:
#             print(" ", end=" ")
#     for m in range(2, i + 1):
#         if i == 1 or i == n or m == 1 or m == i:
#             print(m, end=" ")
#         else:
#             print(" ", end=" ")

#     print(" ")

# 6

# n = 5
# for i in range(n, 0, -1):
#     var = n
#     for j in range(1, i + 1):
#         if i == 1 or i == n or j == 1 or j == i:
#             print(i - j + 1, end=" ")
#         else:
#             print(" ", end=" ")

#     print(" ")
