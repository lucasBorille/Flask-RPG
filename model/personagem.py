from .racas.raca_base import Raca
from .classes.classe_base import Classe

class Personagem:
    def __init__(self, nome: str, raca: Raca, classe: Classe, atributos: dict):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.atributos = atributos
        self.pontos_de_vida = classe.pontos_de_vida_inicial

    def __str__(self):
        """Retorna a ficha completa do personagem formatada."""
        
        habilidades_raca = ""
        for nome, desc in self.raca.get_habilidades().items():
            habilidades_raca += f"  - {nome}: {desc}\n"
            
        habilidades_classe = ""
        for nome, desc in self.classe.get_habilidades_de_classe().items():
            habilidades_classe += f"  - {nome}: {desc}\n"

        ficha = (
            f"\n{'='*40}\n"
            f"FICHA DE PERSONAGEM\n"
            f"{'='*40}\n"
            f"Nome: {self.nome}\n"
            f"Raça: {self.raca.nome}\n"
            f"Classe: {self.classe.nome}\n"
            f"Alinhamento Padrão da Raça: {self.raca.alinhamento}\n" # Adicionado
            f"\n--- Atributos ---\n"
            f"Força: {self.atributos['Força']}\n"
            f"Destreza: {self.atributos['Destreza']}\n"
            f"Constituição: {self.atributos['Constituição']}\n"
            f"Inteligência: {self.atributos['Inteligência']}\n"
            f"Sabedoria: {self.atributos['Sabedoria']}\n"
            f"Carisma: {self.atributos['Carisma']}\n"
            f"\n--- Status de Combate ---\n"
            f"Pontos de Vida (PV): {self.pontos_de_vida}\n"
            f"Base de Ataque (BA): {self.classe.base_ataque}\n"
            f"Movimento: {self.raca.movimento}m\n"
            f"Infravisão: {self.raca.infravisao}\n" # Adicionado
            f"\n--- Habilidades de Raça ---\n"
            f"{habilidades_raca}"
            f"\n--- Habilidades de Classe (Nível 1) ---\n"
            f"{habilidades_classe}"
            f"{'='*40}\n"
        )
        return ficha