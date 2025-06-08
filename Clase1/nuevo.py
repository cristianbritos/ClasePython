
# pip install tabulate
from tabulate import tabulate

    
Clients=['Cristian','Juan','Pedro','Maria']

def list_clients():
    global Clients
    if Clients:
        print('Our Clients are :')
        show=[]
        for idx,name in enumerate(Clients):
            show.append([idx+1,name])
        print(tabulate(show,headers=['N°','Name'],tablefmt='fancy_grid'))
    else:
        print(' I don´t have Clients in this ent')



if __name__ == '__main__':
    list_clients()
