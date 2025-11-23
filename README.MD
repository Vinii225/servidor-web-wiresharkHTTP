# Atividade Avaliativa AV2

## Este repositório contém uma solução da atividade proposta pelo professor na disciplina de Redes de Computadores

**Professor:** Jose Raul de Brito Andrade

**Disciplina:** Redes de Computadores

**Data de realização:** durante os dias 10 e 24 de Novembro de 2025

### 1. Implementação do Servidor WEB em python

Para realizar a atividade, foi implementado um servidor Web simples em Python, responsável por disponibilizar apenas uma página específica.

A logica funciona da seguinte maneira : 

Existe um arquivo principal do servidor (por exemplo: webserver.py).

Dentro dele, o código cria um socket, inicia o servidor HTTP básico e aguarda conexões.

Quando o navegador acessa a página correta (por exemplo: index.html ou o arquivo solicitado no PDF), o servidor lê o arquivo local,

envia o conteúdo para o navegador,

responde com o cabeçalho HTTP/1.1 200 OK.
Porém, se tentar acessar qualquer outra pagina que não existe no diretorio , o servidor irá retonar : HTTP/1.1 404 Not Found 

### 2. Análises das requisições e respostas do HTTP utilizando Wireshark como ferramenta
A primeira requisição GET não usa If-Modified-Since (cache limpo).

Primeira requisição:
Não tem If-Modified-Since, porque o navegador não tinha cache.
O servidor retorna 200 OK e envia o arquivo.

Segunda requisição:
O navegador envia If-Modified-Since com a data do arquivo.
O servidor responde 304 Not Modified, não envia o conteúdo e manda o navegador usar o arquivo do cache.

### Estrutura do Repositório

```plaintext
- README.md               # Documentação do repositório
- Atividade - AV2.pdf     # Arquivo da atividade com as tarefas

--- Servidor-Web (Pasta)
- HelloWorld.html        # Arquivo HTML
- webserver.py           # Arquivo python HTTP servidor




