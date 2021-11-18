''' 1. Реализовать вывод информации о промежутке времени
в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
        Примеры:

duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек
'''
duration = int(input('Введите продолжительность времени'))
days = duration // 86400 # дни - целочисленное деление на 24*3600
hours = (duration % 86400) // 3600 # часы - целочисленное деление на 3600
minutes = (duration % 3600) // 60 # минуты - целочисленное деление на 60
seconds = duration % 60 # секунды - остаток от деления на 60

if duration < 60:
    print(f'{seconds} сек.')
elif duration >= 60 and duration  < 3600:
    print(f'{minutes} мин. {seconds} сек.')
elif duration >= 3600 and duration < 86400:
    print(f'{hours} час. {minutes} мин. {seconds} сек.')
elif duration >= 86400:
    print(f'{days} дн. {hours} час. {minutes} мин. {seconds} сек.')
else:
    print('end')