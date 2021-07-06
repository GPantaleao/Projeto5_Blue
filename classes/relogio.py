class Relogio:
    def __init__(self):
        self.__horas = 8
        self.__minutos = 0
        self.__dia = 1
    
    def __str__(self):    #devolve as horas formatadas#
        return f"{self.__horas:02d}:{self.__minutos:02d}"
    
    def avanca_tempo(self, minutos):    
        self.__minutos += minutos
        while(self.__minutos >= 60):   #tira dos minutos rodados o valor 60, e adicionar +1 na hora, para fazer o relogio funcionar# 
            self.__minutos -= 60
            self.__horas += 1

    def avanca_dia(self): #avança um dia, e começa o novo dia no mesmo horario do dia anterior#
        self.__dia +=1
        self.__horas = 8
        self.__minutos = 0

    def noite_fria(self):
        return self.__horas >= 19 or self.__horas < 8

    @property
    def dia(self):
        return self.__dia
    
    @property
    def horas(self):
        return self.__horas

    @property
    def minutos(self):
        return self.__minutos
