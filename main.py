#Фугкції та види функцій
#функція - це іменований шматок алгоритму, де ми пишемо якусь логіку
#далі її можно викликати по імені скільки завгодно разів у коді
################################################################
# def say_hello(): #назва функції має відповідати правилам іменування змінних
#     print("Hello")
#назва функції має бути дієсловом, відповідати на запит - що треба зробити.
#після назви функції ми ставимо (), у них вказуються параметри - тобто змінні,
#які ми будемо використовувати в рамках функції
#за допомогою цих змінних ми будемо передавати якісь данні
#по факту фунція - це механізм, в який вбудований алгоритм, який щось робить
#
# try:
#     # print("Hello")
#     number = 10
#     print(number)
#     print(say_hello)
#     say_hello()  # виклик функції (функція починає працювати тут у цьому місці)
#     say_hello()
# except Exception as error:
#     print(error)
#обробку виключень має сенс робити тільки там, де функція починає працювати,
#бо саме тут можливі помилки

####################################
# def say_hello():
#     print("Hello Friends!")
#коли ми створюємо функцію з однаковою назвою, то вона переопределяється
#тобто коли ми пишено новую реалізацію функції, то
#вона переопределяється і в нас не буде доступу до попередньої\ першох реалізації
#у нашому випадку name - це параметр функції
#фактично параметр - це змінна, яка існує тільки у рамках конкретної функції
# say_hello()
#
#
# def say_hello(name):
#     print(f"Hello {name}!")
#     name = "qqqq"
#     print(f"Hello {name}!")
#
#
# # say_hello("Test user")
# name1 = "Anton"
# say_hello(name1)
# print(name1)


# def say_hello_name(username):
#     print(f"Hello, {username}")
#
#
# say_hello_name("Vasya")
# name = "Petya"
# say_hello_name(name)
# #
#якщо функція має в кінці повренути нічого, то ми у нії пишемо в кінці None:
#якщо нам треба після відпрацювання функції отримати \ повернути якесь значення, то
#замість None треба написати int \ що нам треба отримати в кінці ціле число
#і тут треба ще буде в кінці функції додати return
#
# def user_info(name: str, age: int, hobby: str) -> None:
#     print(f"Welcome, {name}! Your age: {age} and hobby is {hobby}")
#
#
# try:
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     user_hobby = input("Enter your hobby: ")
#     user_info(name, age, user_hobby)
# except Exception as e:
#     print(e)


########
# після того як відпрацює ключове слово return - функція припиняє свою роботу (тільки функція, а не вся програма)
# return – поверне результат роботи функції. Після відпрацьовування return - решта дій функції не відпрацюють
# то функція завершить свою роботу. Якщо у функції є цикл - у циклi return працює як break,
# але на відміну від break – поверне результат, а не просто зупинить дії.
# Якщо у функції є цикли, і в одному з циклів спрацював return - функція припинить свою роботу.
# ключове слово return може зустрічатися в тілі функції скільки завгодно разів.
#return використовується тільки в функціях

# #приклад з калькулятором
# #add функція додавання:
# def add(n1, n2):
#     return n1 + n2
#
# #sub функція віднімання:
# def sub(n1, n2):
#     return n1 - n2
#
# #mult функція добутку\множиння:
# def mult(n1, n2):
#     return n1 * n2
#
# #mult функція розділення:
# def division(n1, n2):
#     return n1 / n2
#
#
# def calculate() -> None: #для розрахунків ми скористаємося функцією calculate
#     first_number = int(input("Enter first number: "))
#     second_number = int(input("Enter second number: "))
#     math_operation = input("Enter math operation + - * / ")
#
#     match math_operation:
#         case "+":
#             print(f"{first_number} {math_operation} {second_number} = {add(first_number, second_number)}")
#         case "-":
#             print(f"{first_number} {math_operation} {second_number} = {sub(first_number, second_number)}")
#         case "*":
#             print(f"{first_number} {math_operation} {second_number} = {mult(first_number, second_number)}")
#         case "/":
#             print(f"{first_number} {math_operation} {second_number} = {division(first_number, second_number)}")
#         case _:
#             raise Exception("Invalid math operation!")
#
#
# try:
#     # calculate() #для розрахунків ми скористаємося функцією calculate, або виведемо результат, буде те саме
#     result = add(2, 4)
#     print(result)
# except ZeroDivisionError:
#     print("Do not divide by zero please!")
# except Exception as error:
#     print(error)

###
#памаметри у функції можуть бути обов'язковими чи необов'язковими
#ми можемо задавати самостійно додаткові параметри окрім дефолтних параметрів конкретних функцій
#якщо ми хочемо самі додати параметр і зробити його обов'язковим, то краще його не писати
# у кінці, а кращен додати поміж іншими обов'язковими параметрами
#обов'язковий параметр - не має якогось присвоєнного значення у функції,
#а не обов'язковий параметр має якесь присвоєнне значення через знак = це значення.
# приклад нижче
# def user_info(name: str, additional_info: str, age: int = 18, hobby: str = "no hobby") -> None:
#
# def user_info(name: str, age: int = 18, hobby: str = "no hobby") -> None:
#     print(f"Welcome, {name}! Your age: {age} and hobby is {hobby}")
#
#
# user_info("Vasya", 33, "test")
# user_info("Vasya", 33)
# user_info("Vasya")
#
# user_info("walking", "Petya", 33) #тут наші параметри відпрацювали за позицією, а не за ім'ям
# user_info(hobby="walking", name="Petya", age=33) #тут ми фактично прописуємо яке значення відноситься до якого параметру
# #це називається іменовані параметри, їм можна передавати у будь-якій послідовності, бо параметри
# #відпрацюють не за позицією, а за ім'ям

#####
## Усі параметри,
# які розташовуються праворуч від символу *, отримують значення лише на ім'я:
#тобто, всі параметри після символу * мають бути передачні за ім'ям через знак = і далі конкретне ім'я цього параметру
#
# def print_person(name, *, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
# #у цьому прикладі ми маємо задати після * по імені параметри age та company через знак =
#
# print_person("Bob", age=41, company="Microsoft")
# #
# #
# #також ми можемо написати, щоб всі параметри у функції були обов'язово по імені
# def print_person(*, name, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person(name="Bob", age=41, company="Microsoft")
#
# # Якщо навпаки треба визначити параметри, яким можна передавати значення лише за позицією,
# # тобто позиційні параметри, можна використовувати символ /: всі параметри, які йдуть до символу / ,
# # є позиційними і можуть отримувати значення лише за позицією
#
# def print_person(name, /, age, company="Microsoft"):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Tom", company="JetBrains", age=24)  # Name: Tom  Age: 24  company: JetBrains
# print_person("Bob", 41)

#
# #приклад комбінованого використання символів / та * у одній функції
# def print_person(name, /, age=18, *, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Sam", company="Google")  # Name: Sam  Age: 18  company: Google
# print_person("Tom", 37, company="JetBrains")  # Name: Tom  Age: 37  company: JetBrains
# print_person("Bob", company="Microsoft", age=42)  # Name: Bob  Age: 42  company: Microsoft

####
#упаковка та розпаковка даних за допомогою *args та **kwargs:
#наприклад в нас э функція, де треба передати багато різних значень, і ми не знаємо, скільки таких значень
#за фактом під капотом у функції *args є кортеж
#напр.ми використовуэмо *args, якщо юзер воодить купу параметрів і ми з ними будемо працювати як з колекцією

# #нижче приклад упаковки значень у кортеж за допомогою *args
# def show_info(name, *args, add_info="no data"):
#     print(name)
#     print(args)
#     print(add_info)
#
#
# show_info("Vasya")
# show_info("test", 1, 4, 2, 6, "sssss", add_info="my info")
#тут ми бачимо ^^ обов'язковий параметр + упаковка різних значень у кортеж після *args + параметр по імені
#
#
# #нижче приклади розпаковки значень у функції за допомогою *kwargs
# def show_info(num1, num2, num3):
#     print(num1, num2, num3)
# #
# #
# nums = [2, 5, 1]
# show_info(nums[0], nums[1], nums[2]) #ось так розпаковувати не дуже зручно
# show_info(*nums) #а так розпаковувати набагато зручніше, хоча обидва варіанти розпаковки дадуть однаковий результат

###
# #приклад розпаковки значень у функції але вже зі словником
#
# def user_info(**kwargs):
#     print(kwargs)
#
#
# user_info(name="Vasya", age=33)
# #оператор ** перетворить вказані значення у словник, з парою ключ:значення
#
#
# def user_info(name, age):
#     print(name, age)
#
#
# user = {
#     "name": "Vasya",
#     "age": 33
# }
#
# user_info(**user)

#####
# #приклад для спільного застосування *args та **kwargs у одній функції
# #**kwargs завжди має бути вказаним останнім у функції
# def user_info(user_id, add_info="no info", *marks, **sport_types):
#     print(f"User Id: {user_id} and add_info: {add_info}")
#     for i in range(len(marks)):
#         print(f"Mark {i + 1}: {marks[i]}")
#
#     for sport_type, desc in sport_types.items():
#         print(f"{sport_type}: {desc}")
#
#
# user_info(123, "some info", 11, 12, 10, type1="sport 1", type2="sport 2")
# #
# print()

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

