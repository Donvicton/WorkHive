from Ad import Ad

class User():
    def __init__(self, username, cpf, password):
        self.__username = username
        self.__cpf = cpf
        self.__password = password
        self.__favoritos = []
        self.__notificacoes = []

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
        return self.__username

    def get_cpf(self):
        return self.__cpf

    def get_password(self):
        return self.__password

    def get_favoritos(self):
        return self.__favoritos

    def favoritar(self, ad_id):
        self.__favoritos.append(ad_id)
    def get_notificacoes(self):
        return self.__notificacoes

    def adicionar_notificacao(self, notificacao):
        self.__notificacoes.extend(notificacao)