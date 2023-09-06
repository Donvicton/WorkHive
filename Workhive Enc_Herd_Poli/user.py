from Ad import Ad
        
class User():
    def __init__(self, username, cpf, password):
        self.__username = username
        self.__cpf = cpf
        self.__password = password
        self.__favoritos = []
        self.__notificacoes = []

    def __repr__(self):
        return f"'{self.__username}'"
    
    def create_ad(self, ads_dict, category, description, price):
        ad = Ad(self.__username, category, description, price)
        ad_id = len(ads_dict) + 1
        ads_dict.update({ad_id: ad})
        print(f"Anúncio de id: {ad_id} criado com sucesso!\n")

    def delete_ad(self, id, ads_dict, logged_username):
        if ads_dict.get(id, None):
            if ads_dict[id].get_username() == logged_username:
                ads_dict.pop(id)
                print(f"Anúncio de id: {id} removido com sucesso!\n")
            else:
                print("Usuário não tem acesso para remover o anúncio!\n")
        else:
            print(f"O id: {id} não existe!\n")

    # Métodos para acessar os atributos encapsulados
    def get_username(self):
        return str(self.__username)

    def set_username(self, new_username):
        self.__username = new_username

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, new_cpf):
        self.__cpf = new_cpf

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password

    def get_favoritos(self):
        return self.__favoritos

    def favoritar(self, ad_id):
        self.__favoritos.append(ad_id)

    def get_notificacoes(self):
        return self.__notificacoes

    def adicionar_notificacao(self, notificacao):
        self.__notificacoes.extend(notificacao)