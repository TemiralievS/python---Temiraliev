"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""

import heapq  # Модуль heapq обеспечивает реализацию алгоритма очереди кучи
from collections import Counter, namedtuple



    #структура дерева
class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

    #«листья дерева», у них нет потомков, но есть значение символа
class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"

    # функция кодирования символов в коды Хаффмана
def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)

        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))

        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


    # функция декодирования исходной строки по кодам Хаффмана
def huffman_decode(encoded, code):
    sx = []
    enc_ch = ""
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                sx.append(dec_ch)
                enc_ch = ""
                break
    return "".join(sx)

# Главная функция программы, она считывает текст пользователя,
# кодирует его, выводит частоту встречаемости каждого символа и его код Хаффмана.
# Потом выводит весь текст в виде кода Хаффмана и декодирует его обратно в читаемый текст
def main():
    s = input('Введите строку для кодирования: ')
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)

    for ch in sorted(code):
        print(f'{ch}: {code[ch]}')

    print(f'Закодированная строка: {encoded}')
    print(f'Раскодированная строка: {huffman_decode(encoded, code)}')


main()

"""
Введите строку для кодирования: beep boop beer
 : 110
b: 00
e: 10
o: 111
p: 011
r: 010
Закодированная строка: 00101001111000111111011110001010010
Раскодированная строка: beep boop beer

Process finished with exit code 0

"""

