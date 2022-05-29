import math

def my_log(value, **kwargs):
    """Ищет целую степень числа от двойки"""
    #база
    base = 2
    #если аргументов нет (если это первая функция в рекурсии)
    if not kwargs:
        #степень, в которую будем возводить
        power = 1
    #если аргументы есть - берем оттуда степень для возведения
    else:
        power =kwargs['power']

    #если 2 в проверяемой степени <= цифре, у которой ищем степень
    if base**power <= value:
        #запуская следующую иттерацию, повышая степень на единицу
        power = my_log(value, power=power +1)
    else:
        #значит предыдущая степень была целой степенью
        power = power-1
    #возвращаем целую искому степень
    return power

value = 1023

x = my_log(value)
y = math.log(value, 2)


print(x)
print(y)