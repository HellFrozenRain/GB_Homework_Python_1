import random
# вообще не разобрался с аргументами =(
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n: int):
    """домашку доделать не успел, + наставник на помощь не пришёл,
    скинул как есть.
        :param n:int надо ввести цифру"""
    result = []
    for i in range(n):
        result.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    return result

print(get_jokes(3))