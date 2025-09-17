# Old Dragon - Criador de Personagens Web (Flask MVC)

Este projeto é uma aplicação web desenvolvida em Python com o framework Flask para a criação completa de personagens de 1º nível para o RPG de mesa "Old Dragon", seguindo as regras do "Livro I – Regras Básicas".

A aplicação foi desenvolvida como parte da avaliação da disciplina de Tópicos Especiais em Software e demonstra a aplicação de conceitos de Programação Orientada a Objetos (OOP) em uma arquitetura Model-View-Controller (MVC).

## Funcionalidades Implementadas

A aplicação web guia o usuário através de um processo interativo e de múltiplas etapas para criar um personagem, incluindo:

1.  **Definição de Atributos:** Implementação dos três métodos de geração de atributos, com uma interface web para distribuição nos modos interativos:
    * **Estilo Clássico:** 3d6 em ordem sequencial, gerado com um clique.
    * **Estilo Aventureiro:** 3d6, com os valores rolados apresentados em uma nova página para distribuição livre pelo usuário.
    * **Estilo Heróico:** 4d6 (descartando o menor), com os valores rolados apresentados para distribuição livre.

2.  **Seleção de Raça:** Implementação de todas as quatro raças básicas do livro, cada uma com suas características e habilidades únicas listadas na ficha final:
    * Humano
    * Anão
    * Elfo
    * Halfling

3.  **Seleção de Classe:** Implementação de três classes de personagem distintas, com suas regras de 1º nível:
    * Guerreiro
    * Ladrão
    * Mago

4.  **Ficha Final:** Ao final do processo, o programa exibe uma ficha de personagem completa e bem formatada com todas as informações geradas.

## Arquitetura e Estrutura do Projeto

O código foi organizado seguindo a arquitetura **Model-View-Controller (MVC)** para garantir a separação de responsabilidades, facilitando a manutenção e escalabilidade do projeto.

```text
/
├── app.py              # Controller: Orquestra a aplicação com Flask.
│
├── model/                # Model: Contém a lógica de negócio e regras do jogo.
│   ├── personagem.py
│   ├── gerador_atributos.py
│   ├── utils.py
│   ├── racas/
│   └── classes/
│
└── templates/            # View: Contém os arquivos HTML para a interface.
    ├── index.html        # Formulário inicial de criação.
    ├── distribuir_atributos.html # Página para distribuição interativa de atributos.
    └── ficha.html        # Página para exibir a ficha final.
```

## Decisões de Design (Pontos para a Defesa de Código)
- **Model-View-Controller (MVC):**

    - Model: A pasta `model` contém todo o back-end e a lógica do RPG. As classes são independentes da interface, focando apenas nas regras.

    - View: A pasta `templates` contém os arquivos HTML. Eles são responsáveis apenas pela apresentação dos dados e não contêm lógica de negócio.

    - Controller: O arquivo `app.py` usa o Flask para conectar o Model e a View. Ele recebe as requisições do usuário, aciona a lógica no Model e renderiza a View apropriada com os dados resultantes.

- **Fluxo Interativo na Web:** Para replicar a distribuição de atributos do modo console, foi criado um fluxo de múltiplas páginas. O Controller gerencia o estado da criação do personagem entre as requisições, passando os dados necessários (nome, raça, etc.) através de campos de formulário ocultos (`<input type="hidden">`).

- **Validação Front-end e Back-end:**

No front-end (`distribuir_atributos.html`), foi utilizado JavaScript para impedir que o usuário selecione o mesmo valor para múltiplos atributos, melhorando a usabilidade.

No back-end (`app.py`), uma validação na rota `/finalizar` garante que os atributos enviados pelo usuário correspondem exatamente aos que foram rolados pelo servidor. Isso cria uma aplicação mais segura e robusta, que não confia cegamente nos dados enviados pelo cliente.

## Como Executar
1. **Pré-requisitos**: Certifique-se de ter o Python 3 instalado.
2. **Clone o Repositório:**

``` Bash
git clone <URL_DO_SEU_REPOSITORIO>
cd <NOME_DA_PASTA_DO_PROJETO>
```
3. **Crie e Ative um Ambiente Virtual:**

```Bash
# Criar
python -m venv venv
# Ativar (Windows)
.\venv\Scripts\activate
# Ativar (macOS/Linux)
# source venv/bin/activate
```
4. **Instale as Dependências**:

```Bash
pip install Flask
```
5. **Execute a Aplicação:**

```Bash
python app.py
```
6. **Acesse no Navegador:** Abra seu navegador e acesse o endereço `http://127.0.0.1:5000`.

## Critérios de Avaliação Atendidos
- **Funcionalidades**: Todas as funcionalidades de criação (3 métodos de atributos, 4 raças, 3 classes) foram implementadas em uma interface web funcional.

- **Reutilização de Código**: As classes do back-end foram reutilizadas e movidas para uma pasta model, conforme solicitado.

- **Arquitetura MVC**: O projeto foi estruturado seguindo o padrão MVC, com uma clara separação entre a lógica de negócio (Model), a interface do usuário (View) e a orquestração (Controller).

- **Uso de Flask**: O framework Flask foi utilizado para construir o Controller e gerenciar as rotas e templates da aplicação.

