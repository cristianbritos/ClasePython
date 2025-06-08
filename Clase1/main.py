import sys

clients = 'Fatima,Maria,'


def add_client(new_client):
    global clients
    if new_client not in clients:
        clients += new_client
        _add_comma()
    else:
        print('El cliente ya existe')


def update_client(new_client, update_client_name):
    global clients
    if new_client in clients:
        clients = clients.replace(new_client + ',', update_client_name+',')
    else:
        print('El cliente no existe')


def remove_client(client):
    global clients
    if client in clients:
        clients = clients.replace(client+',','')
    else:
        print('El cliente no existe')


def buscar_client(cliente):
    global clients
    if cliente in clients:
        print('El Cliente existe')
    else:
        print('El cliente no existe')

def list_clients():
    global clients
    print(clients)

def _add_comma():
    global clients
    clients += ', '

def _print_welcome():
    print('Bienvenido A Ventas')
    print("*" * 30)
    print("Que quieres hacer hoy?")
    print('[C]rear Clientes')
    print('[B]orrar Clientes')
    print('[A]ctualizar Clientes')
    print('[S]earch Clientes')

def _get_client_name():
    client_name = None
    while not client_name:
        client_name=input('Ingrese el nombre del cliente:')
        if client_name =='exit':
            client_name = None
            print('Adios')
            break
    if not client_name:
        sys.exit()
    return client_name


if __name__ == '__main__':
    _print_welcome()

    comando = input()
    comando = comando.upper()

    if comando == 'C':
        nombre = _get_client_name()
        add_client(nombre)
        list_clients()
    elif comando=='B':
        nombre = _get_client_name()
        remove_client(nombre)
        list_clients()
    elif comando == 'A':
        nombre = _get_client_name()
        update_client_name = input('Ingrese el nuevo nombre del cliente:')
        update_client(nombre, update_client_name)
        list_clients()
    elif comando == 'S':
        nombre  = _get_client_name()
        buscar_client(nombre)
        list_clients()
    else:
        print('Opcion no valida')
        

