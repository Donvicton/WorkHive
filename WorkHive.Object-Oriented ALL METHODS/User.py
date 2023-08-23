from Ad import Ad

class User():
    def __init__(self, username, cpf, password):
        self.username = username
        self.cpf = cpf
        self.password = password
        self.favoritos = []
        self.notificacoes = []
        
    def create_ad(self, ads_dict, category, description, price):
        ad = Ad(self.username, category, description, price)
        ad_id = len(ads_dict) + 1
        ads_dict.update({ad_id: ad})
        print(f"Anúncio de id: {ad_id}criado com sucesso!\n")

    def delete_ad(self, id, ads_dict, logged_username):
        if ads_dict.get(id, None):
            if ads_dict[id].username == logged_username:
                ads_dict.pop(id)
                print(f"Anúncio de id: {id} removido com sucesso!\n")
            else:
                print("Usuário não tem acesso para remover o anúncio!\n")
        else:
            print(f"O id: {id} não exite!\n")


if __name__ == "__main__":
    user1 = User('Gabi', '06348242447', '123')
    print(user1.username)    


    user2 = User('Arthur', '0634824xxx7', '123')
    print(user2.username)  
