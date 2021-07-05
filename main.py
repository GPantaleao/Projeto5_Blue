
from classes.personagemCao import Personagem
from classes.relogio import Relogio
from fases.introducao import Introducao
from fases.fases import fase1

if __name__ == '__main__':
    intro = Introducao()
    intro.executar()
    relogio = Relogio()
    personagem = Personagem('Gaara')
    fase1(relogio, personagem)

