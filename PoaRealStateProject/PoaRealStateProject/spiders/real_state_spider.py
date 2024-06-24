import scrapy
from scrapy.http import Response
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import json
from datetime import datetime
import pandas as pd


class RealStateSpider(scrapy.Spider):
    name = "real_state_spider"
    start_urls = ['https://www.vivareal.com.br/aluguel/rio-grande-do-sul/porto-alegre/#onde=,Rio%20Grande%20do%20Sul,Porto%20Alegre,,,,,city,BR%3ERio%20Grande%20do%20Sul%3ENULL%3EPorto%20Alegre,-30.036818,-51.208989,&itl_id=1000183&itl_name=vivareal_-_botao-cta_buscar_to_vivareal_resultado-pesquisa']  # Replace with the target URL
    imoveis_info_list = []
    page_count = 1
    max_page = 2
    def __init__(self, *args, **kwargs):
        super(RealStateSpider, self).__init__(*args, **kwargs)
        
    def parse(self, response):
        imoveis = response.xpath('//div[@class="js-card-selector"]')
        information_log(len(imoveis),self.page_count,self.max_page,response.url)
        for imovel in imoveis:
            dados_imovel = {
                'preco_mes': imovel.xpath('.//div[@class="property-card__price js-property-card-prices js-property-card__price-small"]/p/text()').get(),
                'tipo_imovel' : imovel.xpath('.//h2[@class="property-card__header"]/span[1]/text()').get(),
                'endereco' : imovel.xpath('.//h2[@class="property-card__header"]/span[2]/span[1]/text()').get(),
                'area'  : imovel.xpath('.//ul[@class="property-card__details"]/li[1]/span[1]/text()').get(),
                'quartos' : imovel.xpath('.//ul[@class="property-card__details"]/li[2]/span[1]/text()').get(),
                'vagas' : imovel.xpath('.//ul[@class="property-card__details"]/li[4]/span[1]/text()').get()

            }
            self.imoveis_info_list.append(dados_imovel)
        
            with open('output\scrap_results\\vivaRealResults2.json','w',encoding='utf-8') as f:
                json.dump(self.imoveis_info_list, f,ensure_ascii=False,indent=4)
        
        if self.page_count <= self.max_page:
            try:
                next_url = get_next_page(response.url)
                self.page_count+=1
                yield scrapy.Request(url=next_url, callback=self.parse)
            except: 
                problem_log(self.max_page,self.page_count)


def information_log(num_anuncios,page_count,max_page,url):
        info_paginas = {
            'Página atual': f'{page_count}/{max_page}',
            'Anuncios disponíveis': num_anuncios,
            'Source': url,
            'Data':str(datetime.now()) 
                    }
        with open('output\logs\\vivaRealLogs.json', 'a',encoding='utf-8') as f:
                json.dump(info_paginas, f,ensure_ascii=False,indent=1)
                f.write(',')

def problem_log(page_count,max_page):
    info_paginas = {
            'Página atual': page_count,
            'Páginas totais': max_page,
            'Data':str(datetime.now()) 
                    }
    with open('output\logs\\vivaRealFailLogs.json', 'a',encoding='utf-8') as f:
                json.dump(info_paginas,f,ensure_ascii=False,indent=1)
                f.write(',')
     


def get_next_page(current_url):

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument(f"user-agent={user_agent}")

    navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

    navegador.get(current_url)
    time.sleep(3)

    initial_page_pos = navegador.execute_script("return window.pageYOffset;")
    navegador.execute_script(f"window.scrollBy(0, 500);")
    time.sleep(0.5)
    final_page_pos = navegador.execute_script("return window.pageYOffset;")

    while initial_page_pos != final_page_pos:
        initial_page_pos = navegador.execute_script("return window.pageYOffset;")
        navegador.execute_script(f"window.scrollBy(0, 500);")
        time.sleep(0.5)
        final_page_pos = navegador.execute_script("return window.pageYOffset;")
    
    try:
        button = navegador.find_element(By.XPATH, '//button[@title="Próxima página"]')
        print('Achou botao')
        button.click()
        time.sleep(4)
        next_url = navegador.current_url
        print(next_url)
    except:
        print('Não achou botao')

    navegador.quit()
    return next_url