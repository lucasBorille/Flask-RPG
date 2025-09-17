from .raca_base import Raca

class Humano(Raca):
    def __init__(self):
        super().__init__(
            nome="Humano",
            movimento=9,
            infravisao="Não possui", 
            alinhamento="Qualquer um" 
        )

    def get_habilidades(self) -> dict:
        """
        Retorna as habilidades específicas do Humano.
        Fonte: Livro de Regras OD2, pág. 21.
        """
        return {
            "Aprendizado": "Recebe um bônus de 10% sobre toda experiência (XP) recebida.",
            "Adaptabilidade": "Recebe um bônus de +1 em uma única Jogada de Proteção à sua escolha."
        }