<h1 align="center">
    <p> web scraping e-commerce </p>
</h1>
<p align="center">
  automação; webscraping site e-commerce
</p>

## About
  Percorre todas as páginas do [site](https://telefonesimportados.netlify.app/) e extrai os nomes e preços de todos os produtos cadastrados. O programa armazena todos os nomes e preços dos produtos em um arquivo
  <b> .xlsx </b>. Ao final do processo a planilha é enviada por e-mail, que é solicitado no início da aplicação.
  ### server.json
  O arquivo <b>server.json</b> contém as informações do servidor smtp gmail. As informações de login *(email, senha)* do e-mail remetente devem ser adicionadas ao arquivo.

## Tools
- [Python](https://www.python.org/)
- [Selenium](https://www.selenium.dev/pt-br/documentation/)

## How to run program
```
python main.py
```
