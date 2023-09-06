from user import *
from standart_user import *
from adm_user import *

class All_users():
    def __init__(self):
        self.__users = {
                'Don': Standart_user('Don', '1234556', '123'),
                'Lara': Adm_user('Lara', '9876543', '321')
            }
    def get_users(self):
        return self.__users