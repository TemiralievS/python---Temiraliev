from collections import Counter

ip_list = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as logs_file:
    content = logs_file.read()
    content_list = content.split('\n')  # каждая строка становится элементом списка
    for elem in content_list:
        user_ip = elem.split(' - -')[0]  # из каждого элемeнта получаем ip-адрес
        ip_list.append(user_ip)  # все ip-адреса добавляются в список ip_list
    # используется Counter из collections, т.к. получился слишком большой список для поиска повторяющихся ip-адресов:
    ip_count = Counter(ip_list)
    ip_dict = dict(ip_count)  # перевод Counter в тип: словарь
    # нахождение самого большого значения словаря, оно же количество повторениий ip:
    max_count = max(ip_dict.values())
    # получение словаря с ip-адресом в качестве ключа и наибольшим количеством повторений в качестве значения:
    spammer = {k: v for k, v in ip_dict.items() if v == max_count}
    print(f'Спамер: {spammer}')
