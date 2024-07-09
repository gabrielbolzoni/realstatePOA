# realstatePOA


Coleta e visualização de dados do mercado imobiliário de Porto Alegre

Descrição do projeto
O seguinte projeto tem como objetivo integrar o uso da programação(python e SQL) com assuntos relacionado a engenharia civil.O propósito desse trabalho surgiu com a necessidade de 
validar o estágio obrigatório da faculdade na empresa onde eu trabalho.Com isso, foram utilizados os conhecimentos de programação  para analisar um tema referente ao curso de engenharia civil.
Os arquivos aqui colocados englobam todas as fases da pipeline de dados, desde a extração até a visualização em um dashboard.A coleta é feita através do webscraping em sites de anúncios de imóveis e a visualização utiliza a biblioteca streamlit para gerar um dashboard na infraestrutura local.O repositório conta com um arquivo contendo a raspagem de dados feita durante a criação do projeto. Este arquivo tem informações sobre mais de 7000 imóveis de Porto Alegre e sua coleta foi realizada entre os dias 01/07/2024 e 14/07/2024, podendo estar desatualizados.Pode ser feita a visualização destes dados já coletados ou uma nova raspagem para a coleta de novos.

sumario
Apenas visualização do dashboard
Se o desejo for apenas acessar o dashboard contendo os dados já coletados, sem realizar o processo de uma nova captura dos dados, o arquivo vivaRealResults pode ser utilizado.
Para isso, é necessário transferir ele da pasta 'imoveis_coletado' para a pasta 'output/scrap_results' e executar o processo a partir do arquivo data_tranformation.Assim, é necessário executar os aquivos arquivos data_tranformation, db_connection e create_dash em sequência para visualizar o dashboard


Execução completa da pipeline
Para execução completa do processo, basta abrir o prompt de comando do windows e escrever o seguinte comando no diretório:
run_pipeline.py "url"
*Ver notas sobre a url*
Execução por partes
Os arquivos de coleta,transformação dos dados, criação do banco de dados e crição do dashboard podem ser executados separadamente seguindos as explicações a seguir:
1-Coleta dos dados
O processo começa com a extração dos dados e a execução do arquivo vivaRealScraping.py.Esse arquivo é executado recebendo a url do site VivaReal e o número de páginas 
que devem ser raspadas.Vale ressaltar que cada página possui aproximadamente 36 anúncios,então se o desejo for raspar um número x de anúncios deve-se fazer o cálculo para descobrir quantas páginas são necessárias, arredondando sempra para cima:
n pag = n anuncios/36
A execução do arquivo resulta na criação do arquivo json contendo as informações dos anúncios. O arquivo fica localizado na pasta output/scrap_results
2-Transformação dos dados
Com o arquivo json gerado, o arquivo data_transformation.py manipula os dados e gera na mesma pasta outro aquivo json(vivaRealCleanResults.py) com os dados tratados.
3-Alimentação do banco de dados
Com o banco de dados local criado(ver notas) a execução do arquivo db_connection.py vai popular o banco de dados com os dados coletados e tratados do webscraping, criando uma tabela de dimensão e tabelas fato.
4-Criação do dashboard
Com o banco de dados criado e populado, o arquivo create_dash.py vai criar dispor o dashboard.Os filtros aplicados no dashboard pelo usuário servirão como parâmetro nas funções que criam os gráficos,métricas e tabelas. 
Notas:
*Antes de executar o processo é necessário criar um banco de dados local utilizando SQLite.O arquivo deve ser criado na pasta database e deve possuir o nome poa.db*
Passo a passo para a criação do banco de dados: https://sqldocs.org/sqlite/sqlite-create-database/
*A url passada como parâmetro no prompt de comando deve ser a url do site viva real na aba de 'Alugar' e com a cidade de porto alegre já selecionada como filtro*

Sites utilizados para a coleta de dados: https://www.vivareal.com.br/
