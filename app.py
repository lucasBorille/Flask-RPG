# app.py
from flask import Flask, render_template, request
import json 

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

def salvar_personagem_json(personagem):
    """Salva o personagem em um arquivo JSON local."""
    with open('personagem_salvo.json', 'w', encoding='utf-8') as f:
        # Aqui usamos o método to_dict que criamos no passo 1
        json.dump(personagem.to_dict(), f, ensure_ascii=False, indent=4)
    print("Personagem salvo com sucesso em 'personagem_salvo.json'!")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/criar', methods=['POST'])
def criar_personagem():
    nome = request.form['nome']
    raca_str = request.form['raca']
    classe_str = request.form['classe']
    metodo_atributos = request.form['metodo_atributos']

    if metodo_atributos == 'classico':
        raca_obj = RACAS[raca_str]()
        classe_obj = CLASSES[classe_str]()
        atributos = GeradorAtributos.gerar_classico()

        personagem_final = Personagem(
            nome=nome,
            raca=raca_obj,
            classe=classe_obj,
            atributos=atributos
        )

        salvar_personagem_json(personagem_final) 

        return render_template('ficha.html', personagem=personagem_final, ficha_texto=str(personagem_final))
    else:
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
    nome = request.form['nome']
    raca_obj = RACAS[request.form['raca']]()
    classe_obj = CLASSES[request.form['classe']]()
    
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
    
    salvar_personagem_json(personagem_final)
    
    return render_template('ficha.html', personagem=personagem_final, ficha_texto=str(personagem_final))

if __name__ == '__main__':
    app.run(debug=True)