from abc import ABC, abstractmethod

class Classe(ABC):
    def __init__(self, nome, pontos_de_vida_inicial, base_ataque):
        self.nome = nome
        self.pontos_de_vida_inicial = pontos_de_vida_inicial
        self.base_ataque = base_ataque

    @abstractmethod
    def get_habilidades_de_classe(self) -> dict:
        """Retorna as habilidades da classe."""
        pass

    def __str__(self):
        return self.nome