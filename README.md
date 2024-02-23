# Gestor de produtos

## Objetivo

O objetivo desse repositório é a construção de um gerenciador de produtos para e-comerces.
O primiero passo será construir as páginas basicas so sistema e criar as rotas entre elas.

## Tecnologias

- Flask

## Páginas

- Homepage
- Seleção de módulos
- Cadastro de produtos
- Estoque
- Perfil do usuário

<img width="400" alt="rotas" src="https://github.com/Francisco-Libanio/Gerentciador-de-produtos/assets/75691960/fe353251-1516-4d30-9e35-b6d2b47f950f">

## Configuração do TailwindCss
Fique atendo estrutura de pastas após clonar o projeto se você está tendo problemas de renderizar o css ou construir o arquivo
outpu do tailwind revise sua estrutura de pastas.

(Documentação)[https://tailwindcss.com/docs/installation]
Primeiro realize os comandos 

~~~ npm install -D tailwindcss
npx tailwindcss init ~~~

Detentro do arquivo tailwind.config.js
o coteúdo deve ser o seguinte 

~~~ /** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./ERP/templates/*.html"],
  theme: {
    extend: {},
  },
  plugins: [],
} ~~~

Para construção do arquivo de saída do css você deve rodar o seguinte comando 

~~~ npx tailwindcss -i ./ERP/static/src/style.css -o ./ERP/static/css/output.css --watch
 ~~~
  
E para importar o arquivo outputcss dentro do arquivo HTML você deve usar a seguinte tag  HTML 

~~~ <link rel="stylesheet" href="{{url_for('static',filename='/css/output.css')}}"> ~~~