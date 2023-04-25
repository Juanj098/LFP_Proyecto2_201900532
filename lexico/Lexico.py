global n_linea
global n_col
global instrucciones
global list_lexemas

n_linea =1
n_col=1

errores = []
instrucciones = []
list_T = []

def instruccion(cadena):
    global n_col
    global n_linea
    global list_lexemas

    lexema=""
    puntero=0
    