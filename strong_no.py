# wirte a program 100 to 600 all strong number usign nested loop
# n = 145 is strong number
n = 151
n2 = n
sum = 0
for i in range(len(str(n))):
    rem = n % 10
    n = n // 10
    fact = 1
    # print(rem)
    for j in range(1, rem + 1):
        fact = fact * j
    sum = sum + fact
print(sum)
if sum == n2:
    print("Strong number  :")
else:
    print("Week number !......")
