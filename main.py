#Task1 - Напишіть функцію, яка обчислює добуток елементів списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

def mult(list):
   prod = 1
   for i in list:
      prod = prod*i
   return prod
list = [2,4,5,3]
print('Initial list:',list)
print("Result: ")
print(mult(list))

#Task 2 - Напишіть функцію для знаходження мінімуму у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

def min(list):
    minimum= list[0]
    for i in list:
        if i<minimum:
            minimum=i
    return minimum

list = [19, 8, 54, 81]
print("Initial list: ",list)
print("Minimum number: ")
print(min(list))

#Task 3 -Напишіть функцію, яка визначає кількість простих чисел у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

def prime_numbers(n):
    list = [16, 43, 54, 83]
    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
        # else:
        #     list.append(i)
    return list

prime_list = prime_numbers(100)
print(prime_list)

#Task 4 -Напишіть функцію, яка видаляє зі списку ціле задане число.
# З функції потрібно повернути кількість видаленних елементів.

#v1.
list = [36, 78, 52, 11, 3, 90, 13, 6, 72]
list.remove(3)
print(list)

#v2.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list:
    if num % 3 == 0:
        list.remove(num)
print(list)

#Task 5 - Напишіть функцію, яка отримує два списки як параметр і повертає список,
# що містить елементи обох списків.

#v1.
list1 = [7, 6, 10, 17]
list2 = [33, 15, 2, 4, 12]

result = list1 + list2
print("Final list: "
      + str(list1+list2))

#v2.
def merge_lists(list3, list4):
    return list3 + list4

list3 = 3, 8, 9, 14
list4 = 2, 10, 5, 67
result = list3 + list4
print("Final list: ")
print(result)


#Task 6 - Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих.
# Значення для ступеня передається як параметр, список також передається як параметр.
# Функція повертає новий список, який містить отримані результати.
#для зведення у ступінь — **.

values = [2, 3, 5]

# Raise each number to the power 3
exponents = [pow(value, 3) for value in values]

# Output both lists
print("Original list:\n", values)
print("Raised to the power 3:\n", exponents)

def turn_to_power(values, power=3):
    return [value**power for value in values]
values = [1,2,3]
exponents = [pow(value, 3) for value in values]
print("Initial list: ")
print(values)
print("Exponent list: ")
print(exponents)

