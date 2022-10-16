"""
Задание 1.
Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python
На каждый скрипт нужно два решения - исходное и оптимизированное.
Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler
Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler
Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.
ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.
"""

# Основы. 3 урок. Задание 5.

from memory_profiler import memory_usage, profile
from collections import namedtuple
import random


def decor_memory(func):
    def wrapper(*args):
        m1 = memory_usage()
        func(*args)
        m2 = memory_usage()
        print(f'memory - {m2[0] - m1[0]}')
    return wrapper



# До оптимизации


@decor_memory
def get_jokes(nums):
    jokes_dict = {
    'nouns' : ["автомобиль", "лес", "огонь", "город", "дом"],
    'adverbs' : ["сегодня", "вчера", "завтра", "позавчера", "ночью"],
    'adjectives' : ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]}

    funny_jokes = []
    for n in range(nums):
        random_nouns = random.choice(jokes_dict['nouns'])
        random_adverbs = random.choice(jokes_dict['adverbs'])
        random_adjectives = random.choice(jokes_dict['adjectives'])
        joke = ' '.join([random_nouns, random_adverbs, random_adjectives])
        funny_jokes.append(joke)

    print(funny_jokes)


num = 2
get_jokes(num)



# После оптимизации


@decor_memory
def get_jokes(nums):
    nouns = namedtuple('nouns', ('a', 'b', 'c', 'd', 'e'))
    ns = nouns(a="автомобиль", b="лес", c="огонь", d="город", e="дом")

    adverbs = namedtuple('adverbs', ('a', 'b', 'c', 'd', 'e'))
    advs = adverbs(a="сегодня", b="вчера", c="завтра", d="позавчера", e="ночью")

    adjectives = namedtuple('adjectives', ('a', 'b', 'c', 'd', 'e'))
    adjs = adjectives(a="веселый", b="яркий", c="зеленый", d="утопичный", e="мягкий")
    funny_jokes = []
    for n in range(nums):
        random_nouns = ns[random.randint(0, 4)]
        random_adverbs = advs[random.randint(0, 4)]
        random_adjectives = adjs[random.randint(0, 4)]
        joke = ' '.join([random_nouns, random_adverbs, random_adjectives])
        funny_jokes.append(joke)

    print(funny_jokes)


num = 2
get_jokes(num)


"""
Занимаемая память - 0.015625 при использовании dict
Занимаемая память - 0.0078125 при использовании namedtuple

Согласно замерам при переходе от обычного спискового включения к array
объем занимаемой памяти уменьшился в 2 разa
"""

