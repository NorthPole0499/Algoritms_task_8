from operator import itemgetter


n = int(input('Введите количество экспонатов: '))
data = []
for i in range(n):
    a, b = map(int, input("Введите вес экспоната и его цену: ").split())
    data.append((a, b, b / a))
data.sort(key=itemgetter(2, 0), reverse=True)
m = int(input("Сколько заходов может сделать вор: "))
k = int(input("Сколько кг может унести вор за раз: "))
ans = []

for i in range(m):
    index = 0
    current_weight = k
    del_index = []
    for index in range(len(data)):
        if data[index][0] <= current_weight:
            current_weight -= data[index][0]
            ans.append(data[index][1])
            del_index.append(index)

    new_data = []
    for w in range(len(data)):
        if w not in del_index:
            new_data.append(data[w])
    data = new_data

print("Максимальная сумма украденного:", sum(ans))
