
from datetime import datetime

def greet(name):
    hour = datetime.now().hour
    message = 'Hello, ' + name + '-san!'

    if hour <= 11:
        message = 'Good morning'
    elif hour <= 17:
        message = 'Hello'
    else:
        message = 'Good evening'
    print(message)


greet('Inoue')
