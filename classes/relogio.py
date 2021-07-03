class Relogio:
    def __init__(self):
        self.horas = 8
        self.minutos = 0
        self.dia = 1
    
    def __str__(self):    #devolve as horas formatadas#
        return f"{self.horas:02d}:{self.minutos:02d}"
    
    def avanca_tempo(self, minutos):    
        self.minutos += minutos
        while(self.minutos >= 60):   #tira dos minutos rodados o valor 60, e adicionar +1 na hora, para fazer o relogio funcionar# 
            self.minutos -= 60
            self.horas += 1

    def avanca_dia(self): #avança um dia, e começa o novo dia no mesmo horario do dia anterior#
        self.dia +=1
        self.horas = 8
        self.minutos = 0

    def noite_fria(self):
        return self.horas >= 19 or self.horas < 8

