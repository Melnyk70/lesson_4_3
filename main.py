#ДЗ 4.3. Список із 3 елементів
import random #підключаємо бібліотеку
numbers=[] #порожній початковий список
numbers1=[] #порожній результуючий список
for i in range(random.randint(3, 11)): # розмір списку із випадковою кількістю елементів від 3 до 10
   print(len(numbers))
   numbers.append(random.randint(1, 1000)) #наповнюємо список рандомними значеннями від 1 до 999
print(numbers, "== ", end='') #вивід початкового списку
numbers1.insert(0, numbers[0]) #додаємо в результуючий список елемент початкового списку з індексом 0 - перший
numbers1.insert(1, numbers[2]) #додаємо в результуючий список елемент початкового списку з індексом 0 - третій
numbers1.insert(2, numbers[-2]) #додаємо в результуючий список елемент початкового списку з індексом 0 - другий з кінця
print(numbers1) #виводимо результуючий список
