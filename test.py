#Получить с клавиатуры 6 чисел.
#Вывести на экран их в возрастающем порядке.
A_rr = []
print("Введите 6 целых чисел:")
for i in range (0, 6):
    b = int(input())
    A_rr.append(b)
    A_rr.sort()
    
