# Objetivo do programa
O progarama consiste em um pequeno projeto "fullstack" de login e cadastro utilizando tecnologias de frontend e de backend.

## Como rodar o códico
  Para executar o servidor do backend através do `uvicorn.run()`, basta rodar o arquivo controller.py com o comando: `python controller.py` no terminal
  
  Para executar o servidor do frontend, basta rodar o arquivo `server.py` com o comando: `waitress-serve --listen=127.0.0.1:5001 server:app` acessa o cadastro, `waitress-serve --listen=127.0.0.1:5002 server:app_login` acessa o login. 
  
  OBS: os arquivos: `index.html`, `login.html` são executaveis em portas diferentes, no caso do código, foi habilitado as portas: 5001, 5002 pelo CORS do backend.

## Tecnologias utilizadas

    - Python
    - FastAPI
    - SqlAlchemy
    - MySql
    - JavaScript
    - AJAX
    - HMTL
    - CSS

## Folder banckend
- File controller.py:
  Este código é um servidor HTTP que utiliza o framework FastAPI para receber requisições HTTP POST. Através dessas requisições, o servidor é capaz de cadastrar novos usuários no banco de dados e realizar login.
  
  O servidor possui dois endpoints:

  - POST /cadastre:
  
    Este endpoint recebe três parâmetros: name, email e password. Esses parâmetros são utilizados para cadastrar um novo usuário no banco de dados.

    O valor do campo status indica o resultado do cadastro:

    0: Cadastro realizado com sucesso

    1: Senha inválida (a senha deve ter no mínimo 6 caracteres)

    2: Usuário já existe no banco de dados

    3: Erro interno do servidor
  
  - POST /login:
  
    Este endpoint recebe dois parâmetros: name e password. Esses parâmetros são utilizados para realizar o login do usuário.

    O valor do campo status indica o resultado do login:

    4: Usuário não encontrado no banco de dados
    
    5: Login realizado com sucesso
    
    Se o login foi realizado com sucesso, o campo user irá conter os seguintes dados do usuário:

    `name`: Nome do usuário
    `email`: Endereço de e-mail do usuário
    
  - Observações:
    
    O servidor utiliza uma conexão com banco de dados, que é criada através da função `connect_with_schema()`. O servidor se conecta a um banco de dados que deve ser especificado em uma constante `CONN` definida no arquivo `model.py`. É necessário que o banco de dados esteja criado e as tabelas definidas. As definições das tabelas estão no arquivo `model.py`.

    O servidor utiliza uma classe DTO (UserDto) para retornar os dados do usuário ao realizar login. Esta classe pode ser encontrada no arquivo `dtos.py`.

## Folder frontend
- File server.py:

    O código define duas funções que servem como aplicativos web simples que retornam o conteúdo de arquivos HTML para cadastro e login. As funções abrem os arquivos, lêem seus conteúdos e retornam como resposta HTTP ao cliente. Cada função recebe dois parâmetros, um ambiente e uma função de resposta de início. Além disso, cada função define um cabeçalho de resposta HTTP que indica que o conteúdo retornado é do tipo HTML.

    Este é um código HTML que cria uma página de cadastro para um sistema web. Ele usa a biblioteca Bootstrap e jQuery para estilização e funcionalidades de interação do usuário.

- File cadastre.html:

    O código HTML tem uma seção head com a configuração da página, incluindo uma folha de estilo CSS e uma referência a um arquivo JavaScript.

    A seção body contém os elementos visuais da página, incluindo campos de entrada para o nome, e-mail e senha do usuário, bem como um botão para enviar o formulário.

    O código JavaScript incluído na página é responsável por fazer uma chamada AJAX para enviar os dados do formulário ao servidor. Ele também inclui uma função que é chamada quando a resposta é recebida, a qual atualiza a página com uma mensagem de sucesso ou erro, dependendo da resposta do servidor.

- File login.html:

    O código é uma página HTML com um formulário de login. Ele usa o framework Bootstrap para estilizar a página. O formulário tem dois campos: "Nome" e "Senha". Quando o usuário clica no botão "Entrar", uma função JavaScript é executada que faz uma chamada AJAX para uma URL específica com os dados do usuário e senha. Dependendo da resposta da chamada AJAX, uma mensagem de sucesso ou erro é exibida na página.