from user import *

class Adm_user(User):
    def __init__(self, username, cpf, password):
        super().__init__(username, cpf, password);
    
    def show_users(self, users):
        for u in users:
            print(f'nome: {users[u].get_username()}')
            print(f'senha: {users[u].get_password()}')
            print(f'cpf: {users[u].get_cpf()}')
        print('')

    def edit_password(self, users):
        if(input('mostrar usuarios? y/n') == 'y'):
            self.show_users(users)

        select_user = input('escolha um usuário: ')
        users[select_user].set_password(input(f'digite uma senha para {users[select_user].get_username()}: '))

    def edit_username(self, users):
        if(input('mostrar usuarios? y/n') == 'y'):
            self.show_users(users)
        select_user = input('escolha um usuário: ')
        new_name = input(f'digite um usuario para {users[select_user].get_username()}: ')
        users[select_user].set_username(new_name)
        users[new_name] = users[select_user]
        del(users[select_user])

    def edit_cpf(self, users):
        if(input('mostrar usuarios? y/n') == 'y'):
            self.show_users(users)

        select_user = input('escolha um usuário: ')
        users[select_user].set_password(input(f'digite um cpf para {users[select_user].get_username()}: '))

    def delet_user(self, users):
        if(input('mostrar usuarios? y/n') == 'y'):
            self.show_users(users)
        select_user = input('escolha um usuário: ')
        print(f"Usuário {users.pop(select_user)} removido com sucesso!")
        return 0
    
    def delete_ad(self, id, ads_dict, logged_username):
        if ads_dict.get(id, None):
            ads_dict.pop(id)
            print(f"Anúncio de id: {id} removido com sucesso!\n")
        else:
            print(f"O id: {id} não existe!\n")