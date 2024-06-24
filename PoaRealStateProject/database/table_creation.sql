
CREATE TABLE IF NOT EXISTS dim_imoveis (
   id INTEGER PRIMARY KEY,
   imovel TEXT NOT NULL);
INSERT INTO dim_imoveis(imovel)
SELECT DISTINCT tipo_imovel FROM base_table;

CREATE TABLE IF NOT EXISTS dim_bairros (
   id INTEGER PRIMARY KEY,
   nome_bairro TEXT NOT NULL);
INSERT INTO dim_bairros(nome_bairro)
SELECT DISTINCT bairro FROM base_table;

UPDATE base_table 
SET bairro = dim_bairros.id
FROM dim_bairros 
WHERE bairro = dim_bairros.nome_bairro;

UPDATE base_table 
SET tipo_imovel  = dim_imoveis.id
FROM dim_imoveis 
WHERE tipo_imovel = dim_imoveis.imovel;