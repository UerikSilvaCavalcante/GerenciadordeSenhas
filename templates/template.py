import sys, os
sys.path.append(os.path.abspath(os.curdir))

from model.password import Password
from view.password_view import FermetHasher


action = int(input('Digite 1 para salvar uma senha ou 2 para ler uma senha: '))



match action:
    case 1:
        if len(Password.get()) == 0:
            # print('Nenhuma senha salva')
            key, path = FermetHasher.creat_key(archive=True)
            print(f'Chave gerada: {key.decode('utf-8')}')
            if path:
                print(f'Arquivo gerado: {path}')
        else:
            key = input('Digite a chave: ')
        domain = input('Digite o domínio: ')
        password = input('Digite a senha: ')
        fernent_user = FermetHasher(key)
        p1 = Password(domain, fernent_user.encrypt(password).decode('utf-8'))
        p1.save()
    case 2:
        domain = input('Digite o domínio: ')
        key = input('Digite a chave: ')
        fernent_user = FermetHasher(key)
        data = Password.get()
        for i in data:
            if i['domain'] == domain:
                password = {fernent_user.decrypt(i['password'])}
                break
        if password:
            print(f'Senha: {password}')
        else:
            print('Senha não encontrada no dominio')
    case _:
        print('Opção inválida')