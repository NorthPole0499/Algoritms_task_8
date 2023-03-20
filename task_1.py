n = int(input("Введите сдачу, которую нужно выдать: "))
s1 = int(input("Введите номинал первой монеты: "))
m1 = int(input("Введите количество первых монет: "))
s2 = int(input("Введите номинал второй монеты: "))
m2 = int(input("Введите количество вторых монет: "))
s3 = int(input("Введите номинал третьей монеты: "))
m3 = int(input("Введите количество третьих монет: "))
s4 = int(input("Введите номинал четвёртой монеты: "))
m4 = int(input("Введите количество четвёртых монет: "))

data = [(s1, m1), (s2, m2), (s3, m3), (s4, m4)]
data.sort(key=lambda x: x[0], reverse=True)
ans = []

for i in range(4):
    counter = 0
    while True:
        if data[i][0] <= n and data[i][1] > 0:
            counter += 1
            n -= data[i][0]
            data[i] = (data[i][0], data[i][1] - 1)
        else:
            break
    ans.append((data[i][0], counter))

print()
for j in ans:
    print(f"Номинал монеты: {j[0]} Количество: {j[1]}")
