PASSWORD = '12345'

def password_required(func):
    def wrapper():
        password = input('Cual es la contraseña?')
        if password == PASSWORD:
            return func()
        else:
            print('Contraseña incorrecta')
    return wrapper


def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()
    return wrapper


@password_required
def needs_password():
    print('La constraseña es correcta!!!')

@upper
def say_my_name(name):
    return 'Hola {}'.format(name)

if __name__ == '__main__':
    needs_password()
    print(say_my_name('Cristian'))

