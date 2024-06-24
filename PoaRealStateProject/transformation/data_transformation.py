import json
import pandas as pd


bairros_porto_alegre = [
    "Aberta dos Morros", "Agronomia", "Anchieta", "Arquipélago", "Auxiliadora", "Azenha", "Bela Vista", 
    "Belém Novo", "Belém Velho", "Boa Vista", "Boa Vista do Sul", "Bom Jesus", "Bom Fim", "Camaquã", 
    "Campo Novo", "Cascata", "Cavalhada", "Centro", "Chácara das Pedras", "Chapéu do Sol", "Cidade Baixa", 
    "Coronel Aparício Borges", "Costa e Silva", "Cristal", "Cristo Redentor", "Espírito Santo", "Extrema", 
    "Farrapos", "Farroupilha", "Floresta", "Glória", "Guarujá", "Higienópolis", "Hípica", "Humaitá", 
    "Independência", "Ipanema", "Jardim Botânico", "Jardim Carvalho","Jardim Europa", "Jardim Dona Leopoldina", "Jardim Floresta", 
    "Jardim Isabel", "Jardim Itu-Sabará", "Jardim Itu", "Jardim Sabará", "Jardim Lindóia", "Jardim do Salso", 
    "Jardim São Pedro", "Lageado", "Lami", "Lomba do Pinheiro", "Marcílio Dias", "Mário Quintana", "Medianeira", 
    "Menino Deus", "Moinhos de Vento", "Mont' Serrat", "Morro Santana", "Navegantes", "Nonoai", "Parque Santa Fé", 
    "Partenon", "Passo da Areia", "Passo das Pedras", "Pedra Redonda", "Petrópolis", "Pitinga", "Ponta Grossa", 
    "Praia de Belas", "Restinga", "Rio Branco", "Rubem Berta", "Santa Cecília", "Santa Maria Goretti", 
    "Santa Rosa de Lima", "Santa Tereza", "Santana", "Santo Antônio", "São Caetano", "São Geraldo", "São João", 
    "Vila São José", "São Sebastião", "Sarandi", "Serraria", "Sétimo Céu", "Teresópolis", "Três Figueiras", 
    "Tristeza", "Vila Assunção", "Vila Conceição", "Vila Ipiranga", "Vila Jardim", "Vila João Pessoa", "Vila Nova"
]
def extract_bairro(endereco,bairros=bairros_porto_alegre):
    for bairro in bairros:
        if bairro in endereco: 
            endereco=bairro
    return endereco

def data_transformation(json_content):
    imoveis_list_cleaned=[]
    for imovel in json_content:
        preco = imovel['preco_mes'].strip()
        preco = preco[3:].replace('.','')
        tipo_imovel = (imovel['tipo_imovel'].strip()).split()
        tipo_imovel = tipo_imovel[0]
        bairro = extract_bairro(imovel['endereco'])
        area = imovel['area'].strip()
        if imovel['quartos'].strip() == "--":
            quartos = "0"
        else:
            quartos = imovel['quartos'].strip()
        if imovel['vagas'].strip()  == "--":
            vagas = "0"
        else:
            vagas = imovel['vagas']
        cleaned_imovel= {
            'tipo_imovel' : tipo_imovel,
            'preco_mes': preco,
            'bairro' : bairro,
            'area'  : area,
            'quartos' : quartos,
            'vagas' : vagas
        }
        imoveis_list_cleaned.append(cleaned_imovel)

    with open('PoaRealStateProject\output\scrap_results\\vivaRealCleanResults.json','w',encoding='utf-8') as f:
        json.dump(imoveis_list_cleaned, f,ensure_ascii=False,indent=4)

    
with open('PoaRealStateProject\output\scrap_results\\vivaRealResults2.json', 'r', encoding='utf-8') as f:
    json_content = json.load(f)
    data_transformation(json_content)
    f.close()


def clean_df(path,imoveis_analisados):
    all_imoveis_info_df = pd.read_json(path)
    final_info_df = all_imoveis_info_df[all_imoveis_info_df['tipo_imovel'].isin(imoveis_analisados)]
    final_info_df.loc[final_info_df['tipo_imovel']=='Sala/Conjunto','tipo_imovel']= 'Sala'
    final_info_df.loc[final_info_df['tipo_imovel']=='Kitnet/Conjugado','tipo_imovel']= 'Kitnet'
    final_info_df['preco_mes'] = final_info_df['preco_mes'].astype(float)
    final_info_df['area'] = final_info_df['area'].astype(float)
    final_info_df['quartos'] = final_info_df['quartos'].astype(float)
    final_info_df['vagas'] = final_info_df['vagas'].astype(float)
    return final_info_df 

imoveis_analisados = ['Sala/Conjunto','Apartamento','Kitnet/Conjugado','Casa','Loft']
final_info_df = clean_df('PoaRealStateProject\output\scrap_results\\vivaRealCleanResults.json',imoveis_analisados)











