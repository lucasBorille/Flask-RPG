from abc import ABC, abstractmethod

class Raca(ABC):
    def __init__(self, nome: str, movimento: int, infravisao: str, alinhamento: str):
        self.nome = nome
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento = alinhamento

    @abstractmethod
    def get_habilidades(self) -> dict:
        """Retorna a lista de habilidades raciais."""
        pass

    def __str__(self):
        return self.nome