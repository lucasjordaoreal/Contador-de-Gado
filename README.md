![drone](https://github.com/user-attachments/assets/a8d8c88c-5523-499c-a5cf-59f0dab9df9a)

🐄 Detecção de Gado com YOLO
Este é um projeto de aplicação web que utiliza o modelo YOLO (You Only Look Once) para detectar e contar gados em imagens. O aplicativo permite que os usuários façam upload de imagens, que são então processadas pelo modelo para identificar o número de gados presentes na imagem.

🚀 Funcionalidades

Upload de Imagens: Envie imagens para o sistema identificar gados.

Detecção em Tempo Real: Utiliza YOLO para processar a imagem e contar gados.

Exibição dos Resultados: Mostra a imagem original, a imagem processada e a contagem total de gados.

Armazenamento de Imagens: As imagens originais e processadas são armazenadas no servidor.


🛠️ Tecnologias Utilizadas

Flask: Framework web para Python.

YOLO (Ultralytics): Modelo de detecção de objetos pré-treinado.

Werkzeug: Para manipulação segura de arquivos.


📁 Estrutura do Projeto

/ContadorDeGado

├── app.py                  
├── requirements.txt         
├── /static                  
│   ├── /uploads            
│   └── /style              
│       └── design.css      
│
├── /templates               
│   └── index.html           
│
└── /runs                   
    ├── /detect              
    └── /train2             

🔧 Como Inicializar o Projeto

Pré-requisitos

Você precisará ter Python instalado. Recomendo também o uso de um ambiente virtual para gerenciar as dependências do projeto.

Passo a Passo

1. Clone o repositório

git clone https://github.com/lucasjordaoreal/Contador-de-Gado.git
cd Contador de Gado


2. Crie e ative um ambiente virtual

No Windows:

python -m venv venv
venv\Scripts\activate

No macOS/Linux:

python3 -m venv venv
source venv/bin/activate



3. Instale as dependências

pip install -r requirements.txt


4. Inicie o servidor

python app.py


5. Acesse a aplicação

Abra seu navegador e vá para http://127.0.0.1:5000.



📦 Dependências

As principais bibliotecas usadas neste projeto incluem:

Flask

YOLO (Ultralytics)

Werkzeug


Para instalar todas as dependências, use o comando:

pip install -r requirements.txt

🖼️ Demonstração

Imagem Original: 

Imagem Processada com Detecção: 

> Exemplo de uma imagem com gados detectados.





