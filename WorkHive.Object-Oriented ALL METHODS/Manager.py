# Manager class
from User import User
from Ad import Ad
import smtplib
import ssl
from email.message import EmailMessage

class Manager():


    def send_email(self):
        email_sender = 'noreply.workhive@gmail.com'
        email_password = 'glapmivmumcddcce'

        email_receiver = input('Email do destinatário: ')
        subject = input('Qual o assunto do seu email? ')
        print('\nLembre de informar uma forma de contato pessoal para futuro contato com o prestador de serviço.\n')
        body = input('Digite sua mensagem: ')

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

    def mostrar_notificacoes(self):
        user = self.users.get(self.logged_username)

        if user:
            notificacoes = user.notificacoes

            if notificacoes:
                print("Você tem", len(notificacoes), "notificação(ões):")
                for notificacao in notificacoes:
                    print(notificacao)
                user.notificacoes = []  # Limpa as notificações após exibi-las
            else:
                print("Você não possui notificações.")
        else:
            print('Usuário não encontrado.')

    def visualizar_feedbacks(self):
        user = self.users[self.logged_username]

        print('Feedbacks dos seus anúncios:')
        found_feedback = False

        for id_anuncio, ad in self.ads_dict.items():
            if ad.username == user.username:
                feedbacks = ad.feedbacks
                if feedbacks:
                    print(f"Anúncio ID {id_anuncio}:")
                    print(f"Username: {ad.username}")
                    print(f"Categoria: {ad.category}")
                    print(f"Descrição: {ad.description}")
                    print(f"Preço: R${ad.price:.2f}")
                    print("Feedbacks:")
                    for feedback in feedbacks:
                        print(feedback)
                    print()
                    found_feedback = True

        if not found_feedback:
            print("Não há feedbacks para seus anúncios.")

    

    def adicionar_feedback_anuncio(self):
        identificador = int(input('Digite o ID do anúncio: '))
        feedback = input('Digite seu feedback: ')

        if identificador in self.ads_dict:
            ad = self.ads_dict[identificador]
            ad.add_feedback(feedback)

            print('Feedback adicionado com sucesso!')
        else:
            print('Anúncio não encontrado.')


    def listar_anuncios_por_categoria(self):
        categoria = input('Digite a categoria: ')

        print(f'\nAnúncios na categoria "{categoria}":')
        for id_anuncio, ad in self.ads_dict.items():
            if ad.category.lower() == categoria.lower():
                print(f"ID: {id_anuncio}")
                print(f"Username: {ad.username}")
                print(f"Categoria: {ad.category}")
                print(f"Descrição: {ad.description}")
                print(f"Preço: R${ad.price:.2f}\n")
        
        print(f'Fim dos anúncios na categoria "{categoria}".')

    def show_favoritos(self):
        user = self.users[self.logged_username]
        favoritos = user.favoritos

        if not favoritos:
            print('Aba de favoritos vazia.')
        else:
            print('Aba de favoritos:')
            for id_anuncio in favoritos:
                if id_anuncio in self.ads_dict:
                    ad = self.ads_dict[id_anuncio]
                    print(f"ID: {id_anuncio}")
                    print(f"Username: {ad.username}")
                    print(f"Categoria: {ad.category}")
                    print(f"Descrição: {ad.description}")
                    print(f"Preço: R${ad.price:.2f}\n")
                else:
                    print(f"Anúncio com ID {id_anuncio} não encontrado.\n")

    def favoritar(self):
        id_anuncio = int(input('Qual o ID do anúncio que deseja favoritar? '))
        if id_anuncio in self.ads_dict:
            self.users[self.logged_username].favoritos.append(id_anuncio)
            self.ads_dict[id_anuncio].favoritos += 1  # Incrementar o contador de favoritos
            print('Anúncio favoritado com sucesso!')
        else:
            print('Anúncio não encontrado.')
            
    def __init__(self):
        self.logged_username = None

        self.users = {
            'Gabi': User('Gabi', '1234556', '123'),
            'Lara': User('Lara', '9876543', '321')
        }
        

        self.ads_dict = {
            1: Ad('Gabi', 'tecnologia', 'crio sites', '76543'),
            2: Ad('Gabi', 'Marcenaria', 'mesas artesanais', '123'),
            3: Ad('Lara', 'Hidráulico', 'conserto canos', '45'),
            4: Ad('Lara', 'eletricista', 'crio tomadas', '150'),
        }

        self.category = ['tecnologia', 'consultoria juridica','consultoria engenharia' 'ensino']


     



    def start(self):
        while True:

            if self.logged_username == None:
                print('\n*** MENU ***')
                print('1 para criar usuario.')
                print('2 para fazer login.')
                print('999 para mostrar usuarios cadastrados.')


                option = int(input ('\nSelect option: '))

                if option == 1:
                    username = input('Digite seu nome de usuario: ')
                    cpf = input('Digite seu cpf (apenas números): ')
                    password = input('Crie sua senha (apenas números): ')

                    self.create_user(username, cpf, password)

                elif option == 2:
                    username = input('Digite seu nome de usuario: ')
                    password = input('Confirme sua senha: ')

                    self.login(username, password)

                elif option == 999:
                    for user in self.users.values():
                        print(f"username: {user.username} || cpf: {user.cpf} || password: {user.password}")

            else:
                    
                print('\n*** MENU ***')
                print('1 para editar usuario.')
                print('2 para remover usuario.')
                print('3 para deslogar.')
                print('4 para criar um anúncio')
                print('5 para deletar um anúncio')
                print('6 para mostrar anúncios existentes')
                print('7 para favoritar um anúncio')
                print('8 para listar os favoritos')
                print('9 mostrar anuncios por categoria')
                print('10 para adicionar feedbacks')
                print('11 para vizualizar feedbacks')
                print('12 para visualizar notificações')
                print('13 para enviar email para o prestador de serviço')
                print('999 para mostrar usuarios cadastrados.')
                

                option = int(input ('\nSelect option: '))

                if option == 1:
                    self.edit_user()
                
                elif option == 2:
                    self.delete_user()
                
                elif option == 3:
                    self.logout()

                elif option == 4:
                    user = self.users[self.logged_username]
                    category = input('Qual a categoria do serviço? ')
                    description = input('Descreva o serviço: ')
                    price = float(input('Qual o preço do serviço? R$'))

                    user.create_ad(self.ads_dict, category, description, price)

                    for u in self.users.values():
                        if u.username != user.username:
                            u.notificacoes.append(f'Novo anúncio disponível: {category}')

                elif option == 5:
                    id = int(input('Digite o ID do anúncio a ser deletado! '))
                    user = self.users[self.logged_username]

                    user.delete_ad(id, self.ads_dict, self.logged_username)

                    
                    

                elif option == 6:
                    for id, ad in self.ads_dict.items():
                        print(f"ID: {id}")
                        print(f"Username: {ad.username}")
                        print(f"Categoria: {ad.category}")
                        print(f"Description: {ad.description}")
                        print(f"Price: R${ad.price}\n")
                        
                elif option == 7:
                    self.favoritar()    

                elif option == 8:
                    self.show_favoritos()        
                
                elif option == 9:
                    self.listar_anuncios_por_categoria()       

                elif option == 10:
                    self.adicionar_feedback_anuncio()
                
                
                elif option == 11:
                    self.visualizar_feedbacks()
                
                elif option == 12:
                    self.mostrar_notificacoes()

                elif option == 13:
                    self.send_email()

                elif option == 999:
                    for user in self.users.values():
                        print(f"username: {user.username} || cpf: {user.cpf} || password: {user.password}")
                
                

                 


    def login(self, username, password):
        user = self.users.get(username,None)
        if user:
            if user.password == password:
                self.logged_username = username
            else:
                print('Senha incorreta! ')
        else:
            print('Usuario nao encontrado! ')
        

    def create_user(self, username, cpf, password):
        if username in self.users:
            print('Este usuario ja existe!')
        else:
            user = User(username, cpf, password)
            self.users.update({username: user})
            print('Usuario criado com sucesso!')
        

    def edit_user(self):
        print('\nO que deseja mudar?')
        print('1 para usuario')
        print('2 para senha\n')
        option = int(input("Digite sua opção: "))

        if option == 1:
            self.users[self.logged_username].username = input('Digite um novo nome de usuario: ')
        if option == 2:
            self.users[self.logged_username].password = input('Digite uma nova senha: ')


    def delete_user(self):
        self.users.pop(self.logged_username)
        print(f"Usuario {self.logged_username} removido com sucesso!")
        self.logged_username = None
        
        
    def logout(self):
        self.logged_username = None



if __name__ == "__main__":
    manager = Manager()
    manager.start()
