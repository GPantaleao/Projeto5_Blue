from classes.personagemCao import Personagem
from classes.relogio import Relogio
from fases.introducao import Introducao
from fases.fase1 import fase1

if __name__ == '__main__':
    intro = Introducao()
    intro.executar()
    relogio = Relogio()
    personagem = Personagem('')
    fase1(relogio, personagem)

