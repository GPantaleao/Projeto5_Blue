from time import sleep
import subprocess as cls # importando a biblioteca para limpar tela

from fases.fases import fase1

from classes.personagemCao import Personagem
from classes.relogio import Relogio
from fases.introducao import Introducao

if __name__ == '__main__': #Main usado para chamar todas as Classes
    intro = Introducao()
    intro.executar()
    relogio = Relogio()
    nome = input('Digite o nome do seu cãozinho: ').title()
    cls.call('cls', shell=True)  # Chamando a função de limpar tela
    sleep(1)
    personagem = Personagem(nome)
    fase1(relogio, personagem)