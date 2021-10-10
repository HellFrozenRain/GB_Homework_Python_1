import random
#
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    result = []
    for i in range(n):
        result.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    return result

print(get_jokes(3))