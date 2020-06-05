import os

from bs4 import BeautifulSoup as bs
from selenium import webdriver


def dolar():
    dolar_float = ''
    while dolar_float == '':
        try:
            # options = webdriver.FirefoxOptions()
            options = webdriver.ChromeOptions()
            options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
            options.add_argument('--headless')
            options.add_argument('--disable-dev-ahm-usage')
            options.add_argument('--no-sandbox')
            driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)
            # driver = webdriver.Firefox(options=options)
            # driver = webdriver.Chrome(options=options)
            driver.get('https://economia.uol.com.br/cotacoes/')
            html = driver.page_source
            google_page = bs(html, 'html.parser')
            moedas = google_page.find_all(class_='value bra')
            dolar_str = str(moedas[0].text)
            dolar_str = dolar_str.replace('R$ ', '').replace(',', '.')
            dolar_float = float(dolar_str)
            print(dolar_float)
        except IndexError:
            print('Tentando novamente!')
            driver.close()
            continue
    driver.close()
    # print(f'U$$ 1,00 vale R$ {dolar_float:.3f}')
    return dolar_float

# Teste Local
# Teste local
# def dolar():
#     dolar_float = ''
#     while dolar_float == '':
#         try:
#             options = webdriver.ChromeOptions()
#             options.add_argument('--headless')
#             driver = webdriver.Chrome(options=options)
#             driver.get('https://economia.uol.com.br/cotacoes/')
#             html = driver.page_source
#             google_page = bs(html, 'html.parser')
#             moedas = google_page.find_all(class_='value bra')
#             dolar_str = str(moedas[0].text)
#             dolar_str = dolar_str.replace('R$ ', '').replace(',', '.')
#             dolar_float = float(dolar_str)
#             print(dolar_float)
#         except IndexError:
#             print('Tentando novamente!')
#             driver.close()
#             continue
#     driver.close()
#     # print(f'U$$ 1,00 vale R$ {dolar_float:.3f}')
#     return dolar_float


def buscaValor(coluna, url):
    # options = webdriver.FirefoxOptions()
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument('--headless')
    options.add_argument('--disable-dev-ahm-usage')
    options.add_argument('--no-sandbox')
    nav_gc_m = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)
    # nav_gc_m = webdriver.Firefox(options=options)
    # nav_gc_m = webdriver.Chrome(options=options)
    nav_gc_m.get(url)
    html = nav_gc_m.page_source
    lme_page = bs(html, 'html.parser')
    metal_valor = lme_page.find_all('td')[coluna]
    metal_str = str(metal_valor.text)
    metal_float = float(metal_str)
    dolar_float = dolar()
    metal_float_dolar = metal_float * dolar_float
    metal_float_dolar_str = f'{metal_float_dolar:.2f}'
    metal_float_dolar = float(metal_float_dolar_str)
    nav_gc_m.close()
    print('Valor metal: ', metal_float_dolar)
    return metal_float_dolar

# Teste Local
# Teste local
# def buscaValor(coluna, url):
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')
#     nav_gc_m = webdriver.Chrome(options=options)
#     nav_gc_m.get(url)
#     html = nav_gc_m.page_source
#     lme_page = bs(html, 'html.parser')
#     metal_valor = lme_page.find_all('td')[coluna]
#     metal_str = str(metal_valor.text)
#     metal_float = float(metal_str)
#     dolar_float = dolar()
#     metal_float_dolar = metal_float * dolar_float
#     metal_float_dolar_str = f'{metal_float_dolar:.2f}'
#     metal_float_dolar = float(metal_float_dolar_str)
#     nav_gc_m.close()
#     print('Valor metal: ', metal_float_dolar)
#     return metal_float_dolar


def valorAluminio():
    valor = buscaValor(coluna=2, url='https://www.lme.com/Metals/Non-ferrous/Aluminium#tabIndex=0')
    return valor


def valorCobre():
    valor = buscaValor(coluna=2, url='https://www.lme.com/Metals/Non-ferrous/Copper#tabIndex=0')
    return valor


def valorChumbo():
    valor = buscaValor(coluna=2, url='https://www.lme.com/Metals/Non-ferrous/Lead#tabIndex=0')
    return valor


def valorNiquel():
    valor = buscaValor(coluna=2, url='https://www.lme.com/Metals/Non-ferrous/Nickel#tabIndex=0')
    return valor


def valorEstanho():
    valor = buscaValor(coluna=2, url='https://www.lme.com/Metals/Non-ferrous/Tin#tabIndex=0')
    return valor


def valorZinco():
    valor = buscaValor(coluna=2, url='https://www.lme.com/Metals/Non-ferrous/Zinc#tabIndex=0')
    return valor


def valorVergalhoesAco():
    valor = buscaValor(coluna=1, url='https://www.lme.com/Metals/Ferrous/Steel-Rebar#tabIndex=0')
    return valor


def valorSucataAco():
    valor = buscaValor(coluna=1, url='https://www.lme.com/Metals/Ferrous/Steel-Scrap#tabIndex=0')
    return valor
