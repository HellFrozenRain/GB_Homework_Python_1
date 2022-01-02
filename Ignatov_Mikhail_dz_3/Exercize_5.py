"""Реализовать функцию get_jokes(), возвращающую n шуток,
сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]"""

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n: int):
    """возвращает n шуток
        :param n:int надо ввести цифру"""
    result = []
    for i in range(n):
        result.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    return result


print(get_jokes(3))
