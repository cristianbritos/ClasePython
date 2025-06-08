
import sys

clients = [
    {
        'name':'Cristian',
        'company':'JobGroup',
        'email': 'cristian@jobgroup.com',
        'position': 'Software Engineer'
    },
    {
        'name':'Cristian',
        'company':'JobGroup',
        'email': 'cristian@jobgroup.com',
        'position': 'Software Engineer'
    }
]


def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print('El cliente ya existe')


def update_client(client_name, update_name):
    global clients
    if client_name in clients:
        id_clients = clients.index(client_name)
        clients[id_clients]['name'] = update_name
    else:
        print('El cliente no existe')


def remove_client(client):
    global clients
    if client in clients:
        clients = clients.remove(client)
    else:
        print('El cliente no existe')


def buscar_client(client_name):
    global clients
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True

def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            position=client['position']
        ))

def _print_welcome():
    print('Bienvenido A Ventas')
    print("*" * 30)
    print("Que quieres hacer hoy?")
    print('[C]rear Clientes')
    print('[B]orrar Clientes')
    print('[A]ctualizar Clientes')
    print('[S]earch Clientes')


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('Ingrese para el Cliente, su {}: '.format(field_name))

    return field


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
        client = {
            'name': _get_client_field('nombre'),
            'company': _get_client_field('compañia'),
            'email': _get_client_field('correo'),
            'position': _get_client_field('cargo')
        }
        create_client(client)
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
        

