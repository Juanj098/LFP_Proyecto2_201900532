from lexico.Lexico import Analizador_L
from lexico.Lexico import instrucciones_
from sintactico.obs_S import Coment
from sintactico.obs_S import Error_S
from sintactico.obs_S import CrearBD
from sintactico.obs_S import EliminarBD
from lexico.Lexico import list_T
from lexico.Lexico import list_E

'''
comentario (bloque) -> /* comentario */
comentario (linea) -> --- comentario
crearDB: CrearDB ID = nueva crearDB();
EliminarDB: EliminarDB id = nueva EliiminarDB();
CrearColeccion : CrearColeccion ID = nueva CrearColeccion ( STRING );
EliminarColeccion : EliminarColeccion ID = nueva EliminarColeccion ( STRING );
InsertarUnico : InsertarUnico ID = nueva InsertarUnico ( STRING , STRING );
ActualizarUnico : ActualizarUnico ID = nueva ActualizarUnico ( STRING , {"STRING"} );
EliminarUnico : EliminarUnico ID = nueva EliminarUnico ( STRING );
BuscarTodo : BuscarTodo ID = nueva BuscarTodo ( STRING );
BuscarUnico : BuscarUnico ID = nueva BuscarUnico ( STRING );
'''
Acept = []
E_Sintacticos = []

def sintactico(cadena):
    Analizador_L(cadena)
    instrucciones_()

def analizador_S():
    if list_E:
        print(f'lista ocupada {len(list_E)}')
    else:
        contador = 0
        while contador < len(list_T)-1:
            token = list_T.pop(0)
            #comentario -> /* bloque */
            if token.getTipo()=='coment' and token.getLex()=='/*':
                token_cuerpo = list_T.pop(0)
                if len(list_T)>0 and list_T[0].getLex() == '*/' :
                    token_close = list_T.pop(0)
                    return Coment(token,token_cuerpo,token_close)
                else:
                    return Error_S('Sintactico','Falta simbolo de cierre (*/)')
            #CrearBD -> crearDB: CrearDB ID = nueva crearDB();
            elif token.getTipo() =='instruccion' and token.getLex() == 'CrearBD':
                id = list_T.pop(0)
                if id.getTipo() == 'ID':
                    igual = list_T.pop(0)
                    if igual.getTipo() == 'reservada' and igual.getLex() == '=':
                        nueva = list_T.pop(0)
                        if nueva.getTipo() == 'reservada' and nueva.getLex() == 'nueva':
                            res = list_T.pop(0)
                            if res.getTipo() == 'instruccion' and res.getLex() == 'CrearBD':
                                op = list_T.pop(0)
                                if op.getTipo() == 'reservada' and op.getLex() == '(': 
                                    cl = list_T.pop(0)
                                    if cl.getTipo()=='reservada' and cl.getLex() == ')':
                                        eof = list_T.pop(0)
                                        if eof.getTipo() == 'EOF':
                                            return CrearBD(token,id,igual,nueva,res,op,cl,eof) 
                                        else:
                                            return Error_S('Sintactico','Expected ";" ')
                                    else:
                                        return Error_S('Sintactico','expected: ")" ')
                                else:
                                    return Error_S('Sintactico','expected: "(" ')
                        else:
                            return Error_S('Sintactico','Falta palabra reservada, Expected: nueva')
                    else:
                        return Error_S('Sintactico','Falta signo =')
            elif token.getTipo() == 'instruccion' and token.getLex() == 'EliminarBD':
                return EliminarBD(token,None,None,None,None,None,None,None)
    return None

def toks():
    while True:
        tokens = analizador_S()
        if tokens:
            t = isinstance(tokens,Error_S)
            if t == False:
                Acept.append(tokens)
            else:
                E_Sintacticos.append(tokens)
        else:
            break

    for a in Acept:
        print(a.getCommand())
    
    for e in E_Sintacticos:
        print(e.getArg())
