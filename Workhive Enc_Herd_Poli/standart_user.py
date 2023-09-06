from user import *

class Standart_user(User):
    def __init__(self, username, cpf, password):
        super().__init__(username, cpf, password);
    
    def edit_password(self, user):
        new_password = input('Digite uma nova senha: ')
        self.set_password(new_password)
        return
    
    def edit_username(self, users):
        new_username = input('Digite um novo nome de usuário: ')
        users[new_username] = users.pop(self.get_username())
        users[new_username].set_username(new_username)
        print(users)
        return
    
    def edit_cpf(self, user):
        new_cpf = input('digite um novo cpf')
        self.set_cpf(new_cpf)
        return
    
    def delet_user(self, users):
        password_test = input('confirme a sua senha: ')
        if self.get_password() == password_test:
            users.pop(self.get_username())
            return 1
        else:
            print('senha errada!')
            return 0