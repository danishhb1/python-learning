list12 = []
list13 = []

for x in range(0, 5):
    list12.append(x ** 2)
    list13.append(x ** 2)

    numbers1 = list12 + list12[-2::-1]
    numbers2 = list13 + list13[-2::-1]

    text = str(numbers1) + str(numbers2)
    print(text.center(60))

while len(list12) > 1:
    list12.pop()
    list13.pop()

    numbers1 = list12 + list12[-2::-1]
    numbers2 = list13 + list13[-2::-1]

    text = str(numbers1) + str(numbers2)
    print(text.center(60))
