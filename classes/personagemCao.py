from classes.relogio import Relogio

class Personagem:                 
    def __init__(self, nome):
        self.__nome = nome
        self.__humor = 50
        self.__fome = 50
        self.__frio = 50
        self.__energia = 50
        self.__lugar = 'terreno baldio'

    def __str__(self):          #altera os atributos confome necessidade, sendo valores positivos ou negativos#
        return f'''

        Perfil {self.__nome}:
        ==============================
        |{("Humor - " + str(self.__humor) + "%").center(28)}|   
        |{("Fome - " + str(self.__fome) + "%").center(28)}|   
        |{("Frio - " + str(self.__frio) + "%").center(28)}|  
        |{("Energia - " + str(self.__energia) + "%").center(28)}|  
        ==============================   
        '''

    def muda_humor(self,humor_novo):
        self.__humor += humor_novo
    
    def muda_fome(self,fome_nova):
        self.__fome += fome_nova

    def muda_frio(self,frio_novo):
        self.__frio =+ frio_novo

    def muda_energia(self,nova_energia):
       self.__energia += nova_energia

    def muda_lugar(self,novo_lugar):
       self.__lugar = novo_lugar 

    @property
    def nome(self):
        return self.__nome

    @property
    def lugar(self):
        return self.__lugar

    def atualizacao_frio(self,relogio,frio = -5):
        if relogio.noite_fria():
            self.muda_frio (frio)
        else:
            self.muda_frio(frio * -1)