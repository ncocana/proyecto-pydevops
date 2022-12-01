from contextlib import redirect_stdout
from queries_db.get_all_data_from_bikes import get_all_data_from_bikes

def print_html():

    body = ''
    for document in get_all_data_from_bikes()['documents']:

        x=document['type']


        body += f'<p>Tipo: {x}.<p>'


    inicio = '<!DOCTYPE html><html lang="es" dir="ltr"><head><title>Flexbox</title><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link media="screen" rel="stylesheet" type="text/css" href="flexbox-css.css"><link rel="icon" type="image/png" sizes="80x80" href="imagenes/logo.ico"><base target="_self"></head><body><h1>this seems to work</h1>'
    final = '</body></html>'
    file = inicio + body + final

    with open('prueba.html', 'w') as f:
        with redirect_stdout(f):
            print(file)
    print(body)

print_html()