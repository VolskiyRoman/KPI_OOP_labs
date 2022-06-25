s = 0
n = 5
m = 3
c = 1
a = 1
b = 1
for i in range(a, n):
    for j in range(b, m):
        if i-1 == 0 or j == 0:
            break
        else:
            s += (i/j)/(i-c)
if s == 0:
    print("Помилка, ділення на нуль!")
else:
    print("Сума:", s)
