user_list = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as logs_file:
    content = logs_file.read()
    content_list = content.split('\n')  # каждая строка становится элементом списка content_list
    # для каждого элемента списка content_list находим remote_address, request_type, requested_resource:
    for elem in content_list:
        remote_address = elem.split(' -')[0]
        request_type = elem.split('"')[1].split('/')[0]
        requested_resource = elem.split(' /')[1].split(' HTTP')[0]
        user_tuple = (remote_address, request_type, requested_resource)  # помещаем в кортеж
        user_list.append(user_tuple)  # полученные кортежи помещаем в список user_list
    print(user_list)  # вывод всего списка, либо выводить по элементу user_list[i]
