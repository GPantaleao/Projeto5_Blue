from classes.relogio import Relogio

class Personagem:                 
    def __init__(self, nome):
        self.nome = nome
        self.humor = 50
        self.fome = 50
        self.frio = 50
        self.energia = 50

    def __str__(self):          #altera os atributos confome necessidade, sendo valores positivos ou negativos#
        return f'''
        Humor - {self.humor}   
        Fome - {self.fome}    
        Frio - {self.frio} 
        Energia - {self.energia}    
        '''

    def muda_humor(self,humor_novo):
        self.humor += humor_novo
    
    def muda_fome(self,fome_nova):
        self.fome += fome_nova

    def muda_frio(self,frio_novo):
        self.frio =+ frio_novo

    def muda_energia(self,nova_energia):
       self.energia += nova_energia

    def atualizacao_frio(self,relogio,frio = -5):
        if relogio.noite_fria():
            self.muda_frio (frio)
        else:
            self.muda_frio(frio * -1)