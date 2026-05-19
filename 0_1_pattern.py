# print 0 1 triangel
for i in range(5, 0, -1):
    val = 1
    for j in range(1, i + 1):
        print(val, end=" ")
        val = 1 - val
    print()
