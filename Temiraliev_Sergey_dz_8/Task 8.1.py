import re

RE_MAIL = re.compile(r'^[A-Z0-9._%+-]+@[A-Z0-9-]+.[A-Z]{2,4}$', re.IGNORECASE)


def email_is_valid(email_adress):
    if RE_MAIL.match(email_adress) == None:
        raise ValueError(f'Wrong email: {email_adress}')
    return RE_MAIL.match(email_adress)


def email_parse(email_adress):
    result = re.split('@', email_adress)
    email_dict = {'username': result[0], 'domain': result[1]}
    print(email_dict)


if __name__ == '__main__':
    while True:
        mail = input('Введите email адрес: ')
        if email_is_valid(mail):
            break
    email_parse(mail)
