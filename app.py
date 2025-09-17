# app.py
from flask import Flask, render_template, request

# Importando nosso MODELO
from model.personagem import Personagem
from model.gerador_atributos import GeradorAtributos
from model.racas.humano import Humano
from model.racas.anao import Anao
from model.racas.elfo import Elfo
from model.racas.halfling import Halfling
from model.classes.guerreiro import Guerreiro
from model.classes.ladrao import Ladrao
from model.classes.mago import Mago

app = Flask(__name__)

RACAS = {"Humano": Humano, "Anao": Anao, "Elfo": Elfo, "Halfling": Halfling}
CLASSES = {"Guerreiro": Guerreiro, "Ladrao": Ladrao, "Mago": Mago}

@app.route('/', methods=['GET'])
def index():
    # A rota principal agora só exibe o formulário inicial
    return render_template('index.html')

@app.route('/criar', methods=['POST'])
def criar_personagem():
    # Esta rota recebe os dados do formulário inicial
    nome = request.form['nome']
    raca_str = request.form['raca']
    classe_str = request.form['classe']
    metodo_atributos = request.form['metodo_atributos']

    if metodo_atributos == 'classico':
        # Se for clássico, cria o personagem diretamente
        raca_obj = RACAS[raca_str]()
        classe_obj = CLASSES[classe_str]()
        atributos = GeradorAtributos.gerar_classico()

        personagem_final = Personagem(
            nome=nome,
            raca=raca_obj,
            classe=classe_obj,
            atributos=atributos
        )
        return render_template('ficha.html', personagem=personagem_final, ficha_texto=str(personagem_final))
    else:
        # Se for interativo, rola os valores e redireciona para a página de distribuição
        rolagens = []
        if metodo_atributos == 'aventureiro':
            rolagens = GeradorAtributos.gerar_aventureiro()
        elif metodo_atributos == 'heroico':
            rolagens = GeradorAtributos.gerar_heroico()
        
        return render_template('distribuir_atributos.html',
                               nome=nome,
                               raca=raca_str,
                               classe=classe_str,
                               valores=rolagens)

@app.route('/finalizar', methods=['POST'])
def finalizar_personagem():
    # Esta rota recebe os dados da página de distribuição
    nome = request.form['nome']
    raca_obj = RACAS[request.form['raca']]()
    classe_obj = CLASSES[request.form['classe']]()
    
    # Monta o dicionário de atributos com base nas escolhas do usuário
    atributos = {
        "Força": int(request.form['Força']),
        "Destreza": int(request.form['Destreza']),
        "Constituição": int(request.form['Constituição']),
        "Inteligência": int(request.form['Inteligência']),
        "Sabedoria": int(request.form['Sabedoria']),
        "Carisma": int(request.form['Carisma'])
    }
    
    personagem_final = Personagem(
        nome=nome,
        raca=raca_obj,
        classe=classe_obj,
        atributos=atributos
    )
    
    return render_template('ficha.html', personagem=personagem_final, ficha_texto=str(personagem_final))

if __name__ == '__main__':
    app.run(debug=True)