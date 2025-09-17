# model/gerador_atributos.py

# A importação agora precisa ser relativa
from .utils import rolar_dados, rolar_4d6_drop_lowest
import random # Vamos precisar do random aqui agora

class GeradorAtributos:
    
    @staticmethod
    def gerar_classico():
        """Gera um dicionário de atributos no estilo Clássico."""
        print("Gerando atributos no Estilo Clássico...")
        atributos = {}
        ordem_atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
        for atributo in ordem_atributos:
            atributos[atributo] = sum(rolar_dados(3, 6))
        return atributos

    @staticmethod
    def gerar_aventureiro():
        """
        Rola 6 valores de 3d6 para o estilo Aventureiro.
        A distribuição é feita pelo Controller.
        """
        print("\nGerando valores para o Estilo Aventureiro...")
        return [sum(rolar_dados(3, 6)) for _ in range(6)]

    @staticmethod
    def gerar_heroico():
        """
        Rola 6 valores de 4d6 (drop lowest) para o estilo Heróico.
        A distribuição é feita pelo Controller.
        """
        print("\nGerando valores para o Estilo Heróico...")
        return [rolar_4d6_drop_lowest() for _ in range(6)]