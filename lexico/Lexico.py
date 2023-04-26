from lexico.reservadas import list_reservadas

def Analizador_L(cadena):
    list_reservadas
    list_L = [] #lexemas
    puntero = 0
    n_fil = 0
    lexema = ''
    while puntero < len(cadena):
        char = cadena[puntero]
        if char.isalpha(): #or (cadena[puntero-1].isalpha() and char == ''):  #cadenas [a-z]
            lexema = F_lexema(cadena[puntero:])
            if lexema:
                puntero+=(len(lexema)-1)
                list_L.append(lexema)
        elif char.isdigit(): #[0-9]
            lexema = F_num(cadena[puntero:])
            if lexema:
                puntero+=(len(lexema)-1)
                list_L.append(lexema)
        elif char == '('or char ==')' or char == '=' or char == '\"' or char =='{' or char == '}' or char == ':': #simbolos
            list_L.append(char)
        elif char == '-' or char == '*' or char == '/': #comentarios --- /* */
            lexema = F_comentario(cadena[puntero:])
            if lexema:
                puntero+=(len(lexema)-1)
                list_L.append(lexema)
        elif char == '\n':
            cadena = cadena[1:]
            n_fil+=1
        else:
            pass
        puntero+=1
    return list_L
    
def F_lexema(cadena):
    lexema = ''
    puntero = ''
    for char in cadena:
        puntero += char
        if char.isalpha()==False:
            return lexema
        else:
            lexema+=char

def F_comentario(cadena):
    lexema = ''
    puntero = ''
    for char in cadena:
        puntero += char
        if char != '-' and char!='/' and char != '*' :
            return lexema
        else:
            lexema+=char

def F_num(num):
    lexema = ''
    puntero = ''
    for digi in num:
        puntero += digi
        if digi.isdigit() == False:
            return(lexema)
        else:
            lexema+=digi 