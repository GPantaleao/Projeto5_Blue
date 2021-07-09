from classes.personagemCao import Personagem
from classes.relogio import Relogio
from fases.introducao import Introducao
from fases.fases import fase1
from time import sleep
# importando a biblioteca para limpar tela
import subprocess as cls

if __name__ == '__main__':
    intro = Introducao()
    intro.executar()  # NÃO ESQUECER DE TIRAR DE COMENTARIO DEPOIS
    relogio = Relogio()
    nome = input('Digite o nome do seu cãozinho: ').title()
    cls.call('cls', shell=True)  # chamando a função de limpar tela
    sleep(1)
    personagem = Personagem(nome)
    fase1(relogio, personagem)