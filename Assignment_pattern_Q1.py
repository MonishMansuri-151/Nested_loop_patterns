# ****
#  ****
#   ****
#    ****
# print this pattern

for i in range(1, 5):
    for k in range(1, i):
        print("", end=" ")
    for j in range(1, 5):
        print("*", end="")
    print(" ")
