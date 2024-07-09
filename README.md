
# Coleta e visualização de dados do mercado imobiliário de Porto Alegre
- Projeto por: Gabriel Bolzoni Salles de Abreu
## Motivação do projeto
O seguinte projeto tem como objetivo integrar o uso da programação(python e SQL) com assuntos relacionado a engenharia civil.O propósito desse trabalho surgiu com a necessidade de 
validar o estágio obrigatório da faculdade na empresa de dados onde eu trabalho.Com isso, foram utilizados conhecimentos de programação  para analisar um tema referente ao curso de engenharia civil,o mercado imobiliário da cidade de Porto Alegre.
Assim, a partir dos dados de localização,preço do aluguel,número de quartos e vagas de cada imóvel coletado, consegue-se realizar análises e ver como o mercado imobiliário se comporta na cidade e quais fatores mais o afetam.
## Descrição da pipeline de dados
Os arquivos aqui colocados englobam todas as fases da pipeline de dados, desde a extração até a sua visualização em um dashboard.A coleta é feita através do webscraping em sites de anúncios de imóveis e a visualização utiliza a biblioteca streamlit para gerar um dashboard na infraestrutura local.O repositório conta com um arquivo contendo a raspagem de dados feita durante a criação do projeto. Este arquivo tem informações sobre mais de 7000 imóveis de Porto Alegre e sua coleta foi realizada entre os dias 01/07/2024 e 14/07/2024, podendo estar desatualizados.Pode-se escolher visualizar e analisar o mercado imobiliário de Porto Alegre a partir destes dados já coletados ou realizar uma nova raspagem para uma nova coleta.

## Apenas visualização do dashboard
Se o desejo for apenas acessar o dashboard contendo os dados já coletados, sem realizar o processo de uma nova captura dos dados, o arquivo 'vivaRealResults.json' pode ser utilizado.
Para isso, é necessário transferir ele da pasta 'imoveis_coletado' para a pasta 'output/scrap_results' e executar o processo a partir do arquivo data_tranformation.Assim, é necessário executar os arquivos data_tranformation, db_connection e create_dash em sequência para visualizar o dashboard.

## Execução completa da pipeline
Para rodar a pipeline é necessário que o banco de dados local já esteja criado **(Ver notas sobre o banco de dados).**

Para execução completa do processo, basta abrir o prompt de comando do windows e escrever o seguinte comando no diretório do projeto:
``` python 
run_pipeline.py "url"
```
**(Ver notas sobre a url)**
## Execução por partes
Os arquivos de coleta,transformação dos dados, criação do banco de dados e crição do dashboard podem ser executados separadamente seguindos as explicações a seguir:
### 1-Coleta dos dados
O processo começa com a extração dos dados e a execução do arquivo vivaRealScraping.py.Esse arquivo é executado recebendo a url do site VivaReal e o número de páginas 
que devem ser raspadas.Vale ressaltar que cada página possui aproximadamente 36 anúncios,então se o desejo for raspar um número x de anúncios, deve-se fazer o cálculo para descobrir quantas páginas são necessárias, arredondando sempra para cima:
número de paginas = número de anuncios/36.É normal que apareçam alguns anúncios repetidos no site,então recomenda-se definir cerca de 10% a mais de páginas para que ao excluir os anúncios duplicado o valor desejado de imóveis ainda seja atendido.

A execução do arquivo resulta na criação do arquivo .json contendo as informações dos anúncios. O arquivo fica localizado na pasta 'output/scrap_results'
### 2-Transformação dos dados
Com o arquivo json gerado previamente, o arquivo data_transformation.py manipula os dados e gera na mesma pasta outro aquivo json(vivaRealCleanResults.py) com os dados tratados.
### 3-Alimentação do banco de dados
Com o banco de dados local criado **(ver notas)** a execução do arquivo db_connection.py vai popular o banco de dados com os dados coletados e tratados do webscraping, criando uma tabela de dimensão e tabelas fato.
### 4-Criação do dashboard
Com o banco de dados criado e populado, o arquivo create_dash.py vai criar e abrir o dashboard.Os filtros aplicados pelo usuário servirão como parâmetro nas funções que criam os gráficos,métricas e tabelas e atualizarão automaticamente o dashboard. 
## Notas:
- **Antes de executar o processo é necessário criar um banco de dados local utilizando SQLite.O arquivo deve ser criado na pasta database e deve possuir o nome poa.db**
  -- Passo a passo para a criação do banco de dados: https://sqldocs.org/sqlite/sqlite-create-database/ 
- **A url passada como parâmetro no prompt de comando deve ser a url do site viva real na aba de 'Alugar' e com a cidade de porto alegre já selecionada como filtro**

![Captura de tela 2024-07-09 115930](https://github.com/gabrielbolzoni/realstatePOA/assets/171706295/869bb306-f7a9-42e0-9fac-d9f579189204)

Sites utilizados para a coleta de dados: https://www.vivareal.com.br/
