print("Helo World!")
x = input()
print(x)
x = input("Какой нибудь текст")
print(x)

x = int(input())
y = int(input())
print(x+y)
print(type(x))
print(y)

'''Преобразуйте переменную x, так, чтобы вывод на экран происходил без ошибки.
• Для решения задач, используйте PyCharm или любой другой аналог.
Подсказка: есть два варианта решения, изменить первую строку или изменить вторую'''

x = 25
print(x+25)

#Второй вариант:
x = '25'
print(int(x)+25)

#Третий вариант:
x = int('25')
print(x+25)


'''Напишите программу, где на ввод с клавиатуры подаются два числа X и Y, после чего, на экране должна
отобразиться сумма этих чисел.'''

x = int(input())
y = int(input())
print(x+y)

'''Напишите программу, которая будет преобразовывать общее время ночного сна человека в минуты.
• Программа принимает с клавиатуры на вход значения X и Y.
• На экран нужно вывести общее время сна в минутах.
В этой и дальнейших задачах, проверяйте работу программы на всех значениях из примеров ввода.'''

x = int(input())
y = int(input())
print(x*60 + y)

'''Напишите программу, где на ввод с клавиатуры подаются буквы и цифры X и Y,
после чего, на экране должны отобразиться данные ввода с пробелом.'''

x = input()
y = input()
print(x, y)

#Второй вариант:
x = input()
y = input()
print(x + " " + y) # между кавычками есть пробел

'''Напишите программу, где на ввод с клавиатуры подаются любые значения X и Y,
после чего, на экране должна отобразиться сумма длины(количестов символов) этих значений.'''

x = input()
y = input()
print(len(x)+len(y))

'''Напишите программу, которая объединяет первую и вторую строку и умножает их на N раз.
Программа принимает с клавиатуры на вход три значения: первой строки, второй строки и числовое
значение третьей строки N. Перед вводом значения, должно отображаться сообщение-подсказка(содержание на ваше усмотрение)
что должно быть введено в эту сроку. Перед выводом ответа, также добавьте подсказку.
Пример ввода: (с клавиатуры, значения должны вводиться на этой же строке, справа от текста подсказки) Ваш текст подсказки: Яблоко
Ваш текст подсказки: Груша
Ваш текст подсказки: 2
Пример вывода:
Ваш текст подсказки: ЯблокоГрушаЯблокоГруша
• Обратите внимание что текст-подсказка и значения находятся на одной строке
• Для корректного вывода, правильно расставляйте скобки "()". Правила действий, такие же как в математике.'''

x = input("Введите первую строку: ")
y = input("Введите вторую строку: ")
n = int(input("Введите количество повторов: "))
print("Ваш вывод:" + (x + y) * n)

'''Не меняя значений a,b,c,d, добавьте скобки в выражение в части print, чтобы итоговый результат выводил False.'''

a,b,c,d = False, True, False, True
print(a and b and not (c or d))

#Второй вариант
a,b,c,d = False, True ,False, True
print(a and b and((not c) or d))

'''Напишите программу, где на ввод с клавиатуры подаются любые числовые значения, а на выводе отображается
True или False в зависимости от того, больше первое число второго или нет.'''

x = int(input())
y = int(input())
print(x > y)

'''Напишите программу, где на ввод с клавиатуры, поочердёно подаются целые числа X и Y.
Если их сумма больше числа 10, тогда должно возникнуть сообщение "Сумма больше", если сумма этих
чисел меньше, тогда должно возникнуть сообщение "Сумма меньше", при равенстве, возникнет сообщение "Сумма равна".
Дополнительно: попробуйте решить задачу, используя else'''

x = int(input())
y = int(input())
z = 10
if x + y > z:
    print("Сумма больше")
elif x + y < z:
    print("Сумма меньше")
else:
    print("Сумма равна")

'''Напишите программу, где нужно ввести целое число. Если оно положительное, тогда на экран выводится цифра 1.
Если число отрицательное, выводится -1. Если введенное число – это 0, то на экран выводится 0.
Дополнительно: используйте не больше одного if.'''

x = int(input())
if x > 0:
    print("1")
elif x < 0:
    print("-1")
else:
    print("0")

'''Напишите программу, где на ввод с клавиатуры, поочердёно подаются целые числа X и Y. На экран
необходимо вывести минимальное значение из двух чисел. Если значения чисел совпадают, нужно вывести сообщение: "Числа совпадают".'''

x = int(input())
y = int(input())
if x > y:
    print(y)
elif x < y:
    print(x)
else:
    print("Числа совпадают")

'''Напишите программу, которая спрашивает у пользователя 3 вопроса: его имя, профессию и возраст.
А далее, подставляет значения и выводит три строки с ответами.
• При выводе данных, не забывайте про пробелы.'''

name = input("Введите Ваше имя: ")
profession = input("Введите Вашу профессию: ")
age = int(input("Введите Ваш возраст: "))
print(("Имя: "+name)+"\n"+("Профессия: "+job)+"\n"+("Возраст: "+age)+"\n")

'''Программа принимает 4 целых числа. Посчитайте сумму первых двух чисел и отдельно сумму других двух. 
Разделите первую сумму на вторую. Выведите результат на экран.'''

a, b, c, d = int(input()), int(input()), int(input()), int(input())
x = a+b
y = c+d
print(x/y)

# Второй вариант
sum1 = a+b
sum2 = c+d
sum3 = sum1/sum2
print(sum3)

'''Программа принимает 3 целых числа. Нужно определить какое из них является максимальным и вывести его на экран. 
У всех трёх чисел должны быть разные значения.'''

a, b, c = int(input()), int(input()), int(input())
if b<a>c:
    print(a)
elif a<b>c:
    print(b)
else:
    print(c)
    
#Второй вариант
a, b, c = int(input()), int(input()), int(input())
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)
        
#Третий вариант
a, b, c = int(input()), int(input()), int(input())
m = a

if m < b:
    m = b
    if m < c:
        m = c
        print(m)

'''Программа принимает 3 целых числа. Нужно определить какое из них является средним
(больше одного, но меньше другого) и вывести его на экран. У всех трёх чисел должны быть разные значения.'''

a, b, c = int(input()), int(input()), int(input())

if b>a>c or c>a>b:
    print(a)
elif a>b>c or c>b>a:
    print(b)
else:
    print(c)

'''Напишите программу, которая принимает целое число и выводит текст, как в примере. 
Обратите внимание на наличие пробелов и точек, в ответе они также должны быть.'''

x = int(input())
print('Следующее число для числа ' + str(x) + ' это ' + str(x + 1) + '.')
print('Предыдущее число для числа ' + str(x) + ' это ' + str(x - 1) + '.')

'''Напишите программу которая будет определять, достаточно ли у пользователя денег для покупки товаров.
На вход принимается целое число(количество денег пользователя) с сообщением подсказкой: "Сколько у Вас денег?".
Далее, нужно определить хватит ли денег на покупку всех товаров.
Если пользователю нужна сдача, тогда на экран нужно вывести общую стоимость товаров и далее отдельно 
строкой – сумму его сдачи. Если сдача ненужна, тогда нужно вывести сообщение: "Спасибо, что без сдачи!".
В других ситуациях, сообщение о нехватке суммы.
По условию, нужно купить: хлеб (стоит 30 рублей), молоко (стоит 50 рублей) и сыр (стоит 100 руб)'''

print("Сколько у Вас денег?")
x = int(input())
a = 30
b = 50
c = 100
y = a + b + c

if x > y:
    print("Ваша сдача: ", x - y)
elif x < y:
    print("Недостаточно денег")
else:
    print("Спасибо, что без сдачи!")
    
#Второй вариант
cash = int(input('Сколько у вас денег? '))

bread = 30
milk = 50
cheese = 100
total_price = bread + milk + cheese

if total_price < cash:
    print('Стоимость товаров ' + str(total_price) + ' руб.')
change = cash - total_price
    print('Ваша сдача ' + str(change) + ' руб.')
elif total_price == cash:
    print('Спасибо, что без сдачи!')
else:
    print('Недостаточно денег')

'''Из передачи "Спорт" Маша узнала, что рекомендуется бегать X метров в неделю, но также, сказали,
что бегать слишком много тоже вредно и не стоит бегать более Y метров. Сейчас Маша бегает Z метров в неделю.
Если Маша соблюдает рекомендации передачи "Спорт", выведите сообщение "Это нормально". Если Маша бегает менее X метров,
выведите "Слишком мало бегаете", если же более Y метров, то выведите "Много бегать вредно".
• Вводимое число X всегда меньше либо равно Y
• На вход программе в три строки подаются переменные в следующем порядке: X, Y, Z
• Будьте внимательны при выборе операторов: < и ≤ ; > и ≥'''

x = int(input())
y = int(input())
z = int(input())

if z >= x < y:
    print("Это нормально")
elif z <= x:
    print("Слишком мало бегаете")
else:
    print("Много бегать вредно")
    
#Второй вариант
X = int(input())
Y = int(input())
Z = int(input())

if Y >= Z >= X:
    print("Это нормально")
elif Z > Y:
    print("Много бегать вредно")
elif Z < X:
    print("Слишком мало бегаете")




