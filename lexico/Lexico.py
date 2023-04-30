from lexico.reservadas import list_reservadas
from lexico.reservadas import list_instrucciones
from lexico.token import Token

list_L = [] #lexemas
list_I = [] #instrucciones
list_T = [] #tokens
list_E = [] #errores lexicos

def Analizador_L(cadena):
    list_reservadas
    list_L.clear()
    puntero = 0
    n_fil = 0
    lexema = ''
    while puntero < len(cadena):
        char = cadena[puntero]
        if char.isalpha() or char == '$': #or (cadena[puntero-1].isalpha() and char == ''):  #cadenas [a-z]
            lexema = F_lexema(cadena[puntero:])
            if lexema:
                puntero+=(len(lexema)-1)
                list_L.append(lexema)
        elif char.isdigit(): #[0-9]
            lexema = F_num(cadena[puntero:])
            if lexema:
                puntero+=(len(lexema)-1)
                list_L.append(lexema)
        elif char == '('or char ==')' or char == '=' or char == '\"' or char =='{' or char == '}' or char == ':' or char == ';' or char ==',': #simbolos
            list_L.append(char)
        elif char == '-' or char == '*' or char == '/': #comentarios --- /* */
            lexema = F_comentario(cadena[puntero:])
            if lexema:
                puntero+=(len(lexema)-1)
                list_L.append(lexema)
        elif char == '\n' or char == '':
            list_L.append(char)
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
        if char.isalpha()==False and char != '$':
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

def instrucciones():
    id = ''
    ins = ''
    reservada = ''
    coment = ''

    if list_L != None:
        contador = 0
        while contador < len(list_L):
            tok = list_L.pop(0)
            if tok in list_reservadas: #revisa que lexema este en reservadas
                if tok in list_instrucciones: 
                    ins = tok
                    return Token('instruccion',ins)
                
                elif tok == '/*':
                    return Token('coment',tok)
                elif tok == '*/':
                    return Token('coment',tok)                                                
                
                elif tok == '---':
                    coment=''
                    coment+=tok
                    c=list_L.pop(0)
                    while c != '\n':
                        coment+=c
                        coment+=' '
                        c=list_L.pop(0)
                    return Token('one_line',coment)
                elif tok == ';':
                    return Token('EOF',tok)
                else:
                    reservada = tok
                    return Token('reservada',reservada)
            elif list_T[len(list_T)-1].getLex() == '/*': 
                cadena = ''
                c = list_L.pop(0)
                c+=' '
                while len(list_L) > 0 and list_L[0] != '*/':
                    if  c == '\n':
                        c+='\\n'
                        cadena+=c
                    cadena+=c
                    c=list_L.pop(0)
                    c+=' '
                return Token('coment',cadena)
            else:    
                if tok == '\"':
                    string=''
                    s=list_L.pop(0)
                    while s != '\"':
                        string+=s
                        s=list_L.pop(0)
                    return Token('string',string)
                elif tok =='\n':
                    tok = '\\n'
                    return Token('\\n',tok)
                else:
                    if list_L[0]=="=":
                        id=tok
                        return Token('ID',id)
                    else:
                        return Token('?',tok)
            contador+=1
    else:
        return 'lista vacia'
    return None
    
def instrucciones_():
    while True:
        cadena = instrucciones()
        if cadena:
            if cadena.getTipo() != '?':
                list_T.append(cadena)
            else:
                list_E.append(cadena)
        else:
            break 
    # for toks in list_T:
    #     print(toks.getToken())