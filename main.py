from classes.personagemCao import Personagem
from classes.relogio import Relogio
from classes.carrocinha import Carrocinha
from fases.introducao import Introducao
from fases.fases import fase1
from time import sleep
# importando a biblioteca para limpar tela
import subprocess as cls


if __name__ == '__main__': #Main usado para chamar todas as Classes
    intro = Introducao()
    intro.executar()
    relogio = Relogio()
    carrocinha = Carrocinha()
    nome = input('Digite o nome do seu cãozinho: ').title()
    cls.call('cls', shell=True)  # Chamando a função de limpar tela
    sleep(1)
    personagem = Personagem(nome)
    fase1(relogio, personagem)