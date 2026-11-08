# ==========================================
# Exercise 1: Even and Odd Numbers
# ==========================================

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in list1:
    if num % 2 == 0:
        print('{} is an even number'.format(num))
    else:
        print('{} is an odd number'.format(num))


# ==========================================
# Exercise 2: While Loop with Else
# ==========================================

x = 0

while x < 10:
    print(f'{x} is less than 10')
    x += 1
else:
    print(f'{x} is not less than 10')
