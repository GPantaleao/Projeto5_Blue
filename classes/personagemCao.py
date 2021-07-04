from classes.relogio import Relogio

class Personagem:                 
    def __init__(self, nome):
        self.nome = nome
        self.humor = 50
        self.fome = 50
        self.frio = 50
        self.energia = 50
        self.lugar = 'terreno baldio'

    def __str__(self):          #altera os atributos confome necessidade, sendo valores positivos ou negativos#
        return f'''

        Perfil {self.nome}:
        ==============================
        |{("Humor - " + str(self.humor) + "%").center(28)}|   
        |{("Fome - " + str(self.fome) + "%").center(28)}|   
        |{("Frio - " + str(self.frio) + "%").center(28)}|  
        |{("Energia - " + str(self.energia) + "%").center(28)}|  
        ==============================   
        '''

    def muda_humor(self,humor_novo):
        self.humor += humor_novo
    
    def muda_fome(self,fome_nova):
        self.fome += fome_nova

    def muda_frio(self,frio_novo):
        self.frio =+ frio_novo

    def muda_energia(self,nova_energia):
       self.energia += nova_energia

    def muda_lugar(self,novo_lugar):
       self.lugar = novo_lugar 

    def atualizacao_frio(self,relogio,frio = -5):
        if relogio.noite_fria():
            self.muda_frio (frio)
        else:
            self.muda_frio(frio * -1)