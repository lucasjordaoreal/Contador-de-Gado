Detecção de Gado com YOLO

Esta é uma aplicação web desenvolvida em Python que utiliza Flask e o modelo de detecção de objetos YOLO (You Only Look Once) para identificar e contar gados em imagens enviadas pelos usuários.
Funcionalidades

    Upload de imagens para detecção de gados.
    Análise em tempo real usando o modelo YOLO.
    Exibição da imagem original e da imagem processada com as detecções.
    Contagem total de gados identificados.

Tecnologias Utilizadas

    Flask: Framework web para Python.
    YOLO (Ultralytics): Modelo de detecção de objetos.
    Werkzeug: Biblioteca para manipulação segura de arquivos.

Estrutura do Projeto
/Contador-de-Gado
│
├── app.py                   # Arquivo principal do Flask
├── requirements.txt         # Dependências do projeto
├── /static                  # Diretório para arquivos estáticos
│   ├── /uploads             # Diretório para imagens enviadas
│   └── /style               # Diretório para arquivos CSS
│       └── design.css       # Seu arquivo CSS
│
├── /templates               # Diretório para arquivos de template
│   └── index.html           # Seu arquivo de template HTML
│
└── /runs                    # Diretório para resultados do modelo YOLO
    ├── /detect              # Diretório para detecções
    │   ├── /train2          # Diretório do treinamento
    │   │   └── /weights     # Pesos do modelo
    │   └── /predictX        # Resultados das predições

Pré-requisitos

Antes de iniciar o projeto, você precisará ter o Python e o pip instalados em sua máquina.

Como Inicializar o Projeto

    Clone o Repositório

    Se você tiver o repositório em um serviço de controle de versão, clone-o usando o seguinte comando:

    bash

git clone <URL_DO_REPOSITORIO>
cd <NOME_DA_PASTA>

Crie um Ambiente Virtual

É uma boa prática usar um ambiente virtual para gerenciar as dependências do projeto. Você pode criar um usando:

bash

python -m venv venv

Ative o Ambiente Virtual

    No Windows:

    bash

venv\Scripts\activate

No macOS/Linux:

bash

    source venv/bin/activate

Instale as Dependências

Use o arquivo requirements.txt para instalar as dependências necessárias:

bash

pip install -r requirements.txt

Inicie o Servidor Flask

Execute o seguinte comando para iniciar a aplicação:

bash

python app.py

Acesse a Aplicação

Abra seu navegador e acesse http://127.0.0.1:5000 para usar a aplicação.
