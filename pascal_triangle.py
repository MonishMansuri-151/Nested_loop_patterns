# pascal triangle
#       1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1
n = 4
prev = [1]
for i in range(1, n + 1):
    for k in range(n, i, -1):
        print(" ", end="")
    # prev
    for num in prev:
        print(num, end=" ")
    print()
    new = [1]
    for j in range(len(prev) - 1):
        new.append(prev[j] + prev[j + 1])
    new.append(1)

    prev = new
