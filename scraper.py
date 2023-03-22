from bs4 import BeautifulSoup
import requests

def buscar_productos(buscar):


    nombre_txt = buscar + '.txt'


    web = requests.get(f'https://listado.mercadolibre.com.ar/{buscar}#D[A:{buscar}]')

    soup = BeautifulSoup(web.content, 'html.parser')

    pagina_principal = soup.find_all('div', class_='ui-search-result__content-wrapper')

    numero_de_paginas = soup.find('li', class_='andes-pagination__page-count')
    paginas = int(numero_de_paginas.text[3:])-1


    cont = 1


    for i in pagina_principal:

        auto = i.find('h2').text

        simbolo= i.find('span', class_='price-tag-symbol').text

        precio= i.find('span', class_='price-tag-fraction').text

        archivo = open(f'{nombre_txt}', 'a', encoding='utf-8')

        try:

            archivo.write(f'Producto n°{cont}: ' + auto.strip() + ' ')

            archivo.write('Precio: ' + simbolo + precio + '\n')

        except Exception as e:

            print(f"Error al escribir en el archivo: {e}")

        archivo.close()

        cont+=1

    

        if cont == 48:

            for i in range(paginas):

                web2 = requests.get(f'https://autos.mercadolibre.com.ar/autos_Desde_{i*48}_NoIndex_True')

                soup = BeautifulSoup(web2.content, 'html.parser')

                siguiente_pagina = soup.find_all('div', class_='ui-search-result__content-wrapper')


                for i in siguiente_pagina:

                    auto = i.find('h2').text

                    simbolo= i.find('span', class_='price-tag-symbol').text

                    precio= i.find('span', class_='price-tag-fraction').text

                    archivo = open(f'{nombre_txt}', 'a', encoding='utf-8')

                    try:

                        archivo.write(f'Producto n°{cont}: ' + auto.strip() + ' ')

                        archivo.write('Precio: ' + simbolo + precio + '\n')



                    except Exception as e:

                        print(f"Error al escribir en el archivo: {e}")

                    archivo.close()

                    cont+=1


