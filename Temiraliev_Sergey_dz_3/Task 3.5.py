import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(nums):
    """
    Случайно берёт по одному слову из трёх источников и составляет фразу, которую помещает в список,
    как отдельный элемент.
    Количество фраз(nums) задаётся пользователем.
    """
    funny_jokes = []
    for n in range(nums):
        random_nouns = random.choice(nouns)
        random_adverbs = random.choice(adverbs)
        random_adjectives = random.choice(adjectives)
        joke = ' '.join([random_nouns, random_adverbs, random_adjectives])
        funny_jokes.append(joke)

    print(funny_jokes)


num = int(input('Введите количество шуток: '))
get_jokes(num)
