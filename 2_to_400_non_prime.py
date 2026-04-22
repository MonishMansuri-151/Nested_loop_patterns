# 2 se leker 400 ke beech me jitne bhi non prime number he vo print karne he
# for n in range(2, 401):
#     count = 0
#     for j in range(1, n):
#         if n % j == 0:
#             count += 1
#     if count > 2:
#         print(n)

for n in range(2, 401):
    count = 0

    for i in range(1, n):
        if n % i == 0:
            count += 1
    if count > 2:
        print(n)
