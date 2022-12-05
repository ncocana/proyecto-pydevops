from contextlib import redirect_stdout
from get_bikes_by_availability import get_bikes_by_availability

def print_html():
    x=get_bikes_by_availability(True)['documents'][0]['type']
    y=get_bikes_by_availability(False)['documents'][0]['type']
    line1 = '<!DOCTYPE html>'
    line2 = '<html lang="es" dir="ltr">'
    line_header = '<head><title>Flexbox</title><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link media="screen" rel="stylesheet" type="text/css" href="flexbox-css.css"><link rel="icon" type="image/png" sizes="80x80" href="imagenes/logo.ico"><base target="_self"></head>'
    line_body = '<body><h1>this seems to work</h1></body>'
    line_body2 = f'<body><p>La más barata es: {x}. Y la más cara es: {y}.<p></body>'
    line_final = '</html>'
    file = line1 + line2 + line_header + line_body + line_body2 + line_final

    with open('prueba.html', 'w') as f:
        with redirect_stdout(f):
            print(file)
    print(line_body2)

print_html()