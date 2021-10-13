#calculate
'''def plus(first, second):
    return first+second
def multiply(first,second):
    return first*second

def div(first,second):
    if second == 0:
        return "Неккоректный ввод"
    return first/second


a = int(input('1'))
b = int(input('2'))
result = plus(a,b)
result2 = multiply(result, 5)

print(result)
print(result2)'''




def right_answer():#Подсчет кол-ва пятерок
    a = input('exit')#Запрашиваем фразу
    count_hello = 0#Счетчик количества
    while a != 'exit':#Выполняем программу до стоп слова
        if a == 'hello':#если введено нужное нам значнеие
            count_hello += 1#увеличиваем счетчик
        a = input('exit')#заново запрашиваем ввод
    return count_hello#результатом работы нашей ф-ии является количество "приветов"

def best_friend():
    count = right_answer()#Смотрим сколько раз с нами поздоровались и делаем выводы
    if count > 10:
        return 'best friend'
    if count > 5 and count < 10:
        return 'friend'



a = input()

if a == 'hello':
    print('....')
elif a == 'bye':
    print('...')
elif a != '':
    print('...')