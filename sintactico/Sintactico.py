from lexico.Lexico import Analizador_L
from lexico.Lexico import instrucciones_
from lexico.token import Token
from sintactico.obs_S import Coment
from sintactico.obs_S import Error_S
from sintactico.obs_S import CrearBD
from sintactico.obs_S import EliminarBD
from sintactico.obs_S import CrearColeccion
from sintactico.obs_S import EliminarColeccion
from sintactico.obs_S import EliminarUnico
from sintactico.obs_S import InsertarUnico
from sintactico.obs_S import ActualizarUnico
from sintactico.obs_S import BuscarUnico
from sintactico.obs_S import BuscarTodo
from lexico.Lexico import list_T
from lexico.Lexico import list_E

'''
-comentario (bloque) -> /* comentario */
-comentario (linea) -> --- comentario
-crearDB: CrearDB ID = nueva crearDB();
-EliminarDB: EliminarDB id = nueva EliiminarDB();
-CrearColeccion : CrearColeccion ID = nueva CrearColeccion ( STRING );
-EliminarColeccion : EliminarColeccion ID = nueva EliminarColeccion ( STRING );
-InsertarUnico : InsertarUnico ID = nueva InsertarUnico ( STRING , STRING );
-ActualizarUnico : ActualizarUnico ID = nueva ActualizarUnico ( STRING , {"STRING"} );
-EliminarUnico : EliminarUnico ID = nueva EliminarUnico ( STRING );
-BuscarTodo : BuscarTodo ID = nueva BuscarTodo ( STRING );
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
            #EliminarBD -> EliminarDB: EliminarDB id = nueva EliiminarDB(); 
            elif token.getTipo() == 'instruccion' and token.getLex() == 'EliminarBD':
                id = list_T.pop(0)
                if id.getTipo() == 'ID':
                    igual = list_T.pop(0)
                    if igual.getTipo() == 'reservada' and igual.getLex() == '=':
                        nueva = list_T.pop(0)
                        if nueva.getTipo() == 'reservada' and nueva.getLex() == 'nueva':
                            res = list_T.pop(0)
                            if res.getTipo() == 'instruccion' and res.getLex() == 'EliminarBD':
                                op = list_T.pop(0)
                                if op.getTipo() == 'reservada' and op.getLex() == '(': 
                                    cl = list_T.pop(0)
                                    if cl.getTipo()=='reservada' and cl.getLex() == ')':
                                        eof = list_T.pop(0)
                                        if eof.getTipo() == 'EOF':                
                                            return EliminarBD(token,id,igual,nueva,res,op,cl,eof)
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
            #CrearColeccion -> CrearColeccion : CrearColeccion ID = nueva CrearColeccion ( STRING );
            elif token.getTipo() == 'instruccion' and token.getLex() == 'CrearColeccion':
                id = list_T.pop(0)
                if id.getTipo() == 'ID':
                    ig = list_T.pop(0)
                    if ig.getTipo() == 'reservada' and ig.getLex() == '=':
                        res = list_T.pop(0)
                        if res.getTipo()=='reservada' and res.getLex() == 'nueva':
                            ins = list_T.pop(0)
                            if ins.getTipo() == 'instruccion' and ins.getLex() == 'CrearColeccion':
                                op = list_T.pop(0)
                                if op.getTipo() == 'reservada' and op.getLex() == '(':
                                    str = list_T.pop(0)
                                    if str.getTipo() == 'string':
                                        cl = list_T.pop(0)
                                        if cl.getTipo() == 'reservada' and cl.getLex() == ')':
                                            eof = list_T.pop(0)
                                            if eof.getTipo() == 'EOF':
                                                return CrearColeccion(token,id,ig,res,ins,op,str,cl,eof)
                                            else:
                                                return Error_S('Sintactico','Expected ";" ')
                                        else:
                                            return Error_S('Sintactico','expected: ")" ')
                                else:
                                    return Error_S('Sintactico','expected: "(" ')
                        else:
                            return Error_S('Sintactico','Falta palabra reservada, Expected: nueva')
            #EliminarColeccion -> EliminarColeccion : EliminarColeccion ID = nueva EliminarColeccion ( STRING );
            elif token.getTipo() == 'instruccion' and token.getLex() == 'EliminarColeccion':
                id = list_T.pop(0)
                if id.getTipo() == 'ID':
                    ig = list_T.pop(0)
                    if ig.getTipo() == 'reservada' and ig.getLex() == '=':
                        res = list_T.pop(0)
                        if res.getTipo()=='reservada' and res.getLex() == 'nueva':
                            ins = list_T.pop(0)
                            if ins.getTipo() == 'instruccion' and ins.getLex() == 'EliminarColeccion':
                                op = list_T.pop(0)
                                if op.getTipo() == 'reservada' and op.getLex() == '(':
                                    str = list_T.pop(0)
                                    if str.getTipo() == 'string':
                                        cl = list_T.pop(0)
                                        if cl.getTipo() == 'reservada' and cl.getLex() == ')':
                                            eof = list_T.pop(0)
                                            if eof.getTipo() == 'EOF':
                                                return EliminarColeccion(token,id,ig,res,ins,op,str,cl,eof)
                                            else:
                                                return Error_S('Sintactico','Expected ";" ')
                                        else:
                                            return Error_S('Sintactico','expected: ")" ')
                                else:
                                    return Error_S('Sintactico','expected: "(" ')
                        else:
                            return Error_S('Sintactico','Falta palabra reservada, Expected: nueva')    
            #InsertarUnico ->   InsertarUnico : InsertarUnico ID = nueva InsertarUnico ( STRING , STRING );
            elif token.getTipo() == 'instruccion' and token.getLex() == 'InsertarUnico':
                id = list_T.pop(0)
                if id.getTipo() == 'ID':
                    ig = list_T.pop(0)
                    if ig.getTipo() =='reservada' and ig.getLex() =='=':
                        new = list_T.pop(0)
                        if new.getTipo() =='reservada' and new.getLex() =='nueva':
                            ins = list_T.pop(0)
                            if ins.getTipo()=='instruccion' and ins.getLex() == 'InsertarUnico':
                                op = list_T.pop(0)
                                if op.getTipo() == 'reservada' and op.getLex() == '(':
                                    str = list_T.pop(0)    
                                    if str.getTipo() == 'string':   
                                        com = list_T.pop(0)              
                                        if com.getTipo() == 'reservada' and com.getLex() == ',': 
                                            n = list_T.pop(0)
                                            if n.getLex()=='\\n':
                                                opc = list_T.pop(0)
                                                if opc.getTipo() == 'reservada' and opc.getLex() =='{':
                                                    string=''
                                                    s = list_T.pop(0)
                                                    while len(list_T) > 0 and (list_T[0] != '}' or list_T[0] == ')'):
                                                        if s.getLex()=='\\n':
                                                            s.mod('\n')
                                                            string+=s.getLex()
                                                        string +=s.getLex()
                                                        string+=' '
                                                        s=list_T.pop(0)
                                                        if s.getLex() == '}' or  s.getLex() == ')':
                                                            break
                                                    n2 = list_T.pop(0)
                                                    if n2.getLex()=='\\n':
                                                        n2.mod('\n')
                                                        if n2.getLex()=='\n':
                                                            to = Token('reservada','}')
                                                            list_T.insert(0,to)
                                                            clc = list_T.pop(0)
                                                            if clc.getTipo() == 'reservada' and clc.getLex() == '}':
                                                                clp = list_T.pop(0)
                                                                if clp.getTipo() == 'reservada' and clp.getLex() == ')':
                                                                    eof = list_T.pop(0)
                                                                    if eof.getTipo() == 'EOF':
                                                                        return InsertarUnico(token,id,ig,new,ins,op,str,com,n,opc,string,n2,clc,clp,eof) 
                                                                    else:
                                                                        return Error_S('Sintactico','Expected ";" ')
                                                                else:
                                                                    return Error_S('Sintactico','Expected ")" ')
                                                            else:
                                                                return Error_S('Sintactico','Expected "}" ')
                                                else:
                                                    return Error_S('Sintactico','Expected "{" ')
                                        else:
                                            return Error_S('Sintactico','Expected "," ')   
                                else:
                                    return Error_S('Sintactico','Expected "(" ')
                        else:
                            return Error_S('Sintactico','Falta palabra reservada, Expected: nueva') 
            #ActualizarUnico -> ActualizarUnico : ActualizarUnico ID = nueva ActualizarUnico ( STRING , {"STRING"} );
            elif token.getTipo() == 'instruccion' and token.getLex() == 'ActualizarUnico':
                id = list_T.pop(0)
                if id.getTipo() == 'ID':
                    ig = list_T.pop(0)
                    if ig.getTipo() =='reservada' and ig.getLex() =='=':
                        new = list_T.pop(0)
                        if new.getTipo() =='reservada' and new.getLex() =='nueva':
                            ins = list_T.pop(0)
                            if ins.getTipo()=='instruccion' and ins.getLex() =='ActualizarUnico':
                                op = list_T.pop(0)
                                if op.getTipo() == 'reservada' and op.getLex() == '(':
                                    str = list_T.pop(0)    
                                    if str.getTipo() == 'string':   
                                        com = list_T.pop(0)              
                                        if com.getTipo() == 'reservada' and com.getLex() == ',': 
                                            n = list_T.pop(0)
                                            if n.getLex()=='\\n':
                                                opc = list_T.pop(0)
                                                if opc.getTipo() == 'reservada' and opc.getLex() =='{':
                                                    string=''
                                                    s = list_T.pop(0)
                                                    while len(list_T) > 0 and (list_T[0] != '}' or list_T[0] == ')'):
                                                        if s.getLex()=='\\n':
                                                            s.mod('\n')
                                                            string+=s.getLex()
                                                        string +=s.getLex()
                                                        string+=' '
                                                        s=list_T.pop(0)
                                                        if s.getLex() == '}':
                                                            break
                                                    to = Token('reservada','}')
                                                    list_T.insert(0,to)
                                                    clc = list_T.pop(0)
                                                    if clc.getTipo() == 'reservada' and clc.getLex() == '}':
                                                        com=list_T.pop(0)
                                                        if com.getTipo() == 'reservada' and com.getLex() == ',':
                                                            n2 = list_T.pop(0)
                                                            if n2.getLex()=='\\n':
                                                                n2.mod('\n')
                                                                if n2.getLex()=='\n':
                                                                    cor = list_T.pop(0)
                                                                    if cor.getTipo() == 'reservada' and cor.getLex() == '{':
                                                                        n3 = list_T.pop(0)
                                                                        if n3.getLex()=='\\n':
                                                                            n3.mod('\n')
                                                                            if n3.getLex()=='\n':
                                                                                set=list_T.pop(0)
                                                                                if set.getTipo() == 'reservada' and set.getLex() == '$set':
                                                                                    tp = list_T.pop(0)
                                                                                    if tp.getTipo() == 'reservada' and tp.getLex() == ':':
                                                                                        coo = list_T.pop(0)
                                                                                        if coo.getTipo() == 'reservada' and coo.getLex() == '{':
                                                                                            strings=''
                                                                                            ss = list_T.pop(0)
                                                                                            while len(list_T) > 0 and (list_T[0] != '}' or list_T[0] == ')'):
                                                                                                if ss.getLex()=='\\n':
                                                                                                    ss.mod('\n')
                                                                                                    strings+=ss.getLex()
                                                                                                strings+=ss.getLex()
                                                                                                strings+=' '
                                                                                                ss=list_T.pop(0)
                                                                                                if ss.getLex() == '}':
                                                                                                    break
                                                                                            too = Token('reservada','}')
                                                                                            list_T.insert(0,too)
                                                                                            cloc = list_T.pop(0)
                                                                                            n4 = list_T.pop(0)
                                                                                            if n4.getLex()=='\\n':
                                                                                                n4.mod('\n')
                                                                                                if n4.getLex()=='\n':
                                                                                                    cc = list_T.pop(0)
                                                                                                    if cc.getTipo() == 'reservada' and cc.getLex() == '}':
                                                                                                        n5 = list_T.pop(0)
                                                                                                        if n5.getLex()=='\\n':
                                                                                                            n5.mod('\n')
                                                                                                            if n5.getLex()=='\n':
                                                                                                                clp = list_T.pop(0)
                                                                                                                if clp.getTipo() == 'reservada' and clp.getLex() == ')':
                                                                                                                    eof = list_T.pop(0)
                                                                                                                    if eof.getTipo() == 'EOF':
                                                                                                                        return ActualizarUnico(token,id,ig,new,ins,op,str,com,n,opc,string,clc,com,n2,cor,n3,set,tp,coo,strings,cloc,n4,cc,n5,clp,eof) 
                                                                                                                    else:
                                                                                                                        return Error_S('Sintactico','Expected ";" ')
                                                                                                                else:
                                                                                                                    return Error_S('Sintactico','Expected ")" ')
                                                                                                    else:
                                                                                                        return Error_S('Sintactico','Expected "}" ')
                                                                                        else:
                                                                                            return Error_S('Sintactico','Expected "{" ')
                                        else:
                                            return Error_S('Sintactico','Expected "," ')   
                                else:
                                    return Error_S('Sintactico','Expected "(" ')
                        else:
                            return Error_S('Sintactico','Falta palabra reservada, Expected: nueva')
            #EliminarUnico -> EliminarUnico : EliminarUnico ID = nueva EliminarUnico ( STRING );
            elif token.getTipo() == 'instruccion' and token.getLex() == 'EliminarUnico':
                id = list_T.pop(0)
                if id.getTipo() == 'ID':
                    ig = list_T.pop(0)
                    if ig.getTipo() =='reservada' and ig.getLex() =='=':
                        new = list_T.pop(0)
                        if new.getTipo() =='reservada' and new.getLex() =='nueva':
                            ins = list_T.pop(0)
                            if ins.getTipo()=='instruccion' and ins.getLex() == 'EliminarUnico':
                                op = list_T.pop(0)
                                if op.getTipo() == 'reservada' and op.getLex() == '(':
                                    str = list_T.pop(0)    
                                    if str.getTipo() == 'string':   
                                        com = list_T.pop(0)              
                                        if com.getTipo() == 'reservada' and com.getLex() == ',': 
                                            n = list_T.pop(0)
                                            if n.getLex()=='\\n':
                                                opc = list_T.pop(0)
                                                if opc.getTipo() == 'reservada' and opc.getLex() =='{':
                                                    string=''
                                                    s = list_T.pop(0)
                                                    while len(list_T) > 0 and (list_T[0] != '}' or list_T[0] == ')'):
                                                        if s.getLex()=='\\n':
                                                            s.mod('\n')
                                                            string+=s.getLex()
                                                        string +=s.getLex()
                                                        string+=' '
                                                        s=list_T.pop(0)
                                                        if s.getLex() == '}' or  s.getLex() == ')':
                                                            break
                                                    n2 = list_T.pop(0)
                                                    if n2.getLex()=='\\n':
                                                        n2.mod('\n')
                                                        if n2.getLex()=='\n':
                                                            to = Token('reservada','}')
                                                            list_T.insert(0,to)
                                                            clc = list_T.pop(0)
                                                            if clc.getTipo() == 'reservada' and clc.getLex() == '}':
                                                                clp = list_T.pop(0)
                                                                if clp.getTipo() == 'reservada' and clp.getLex() == ')':
                                                                    eof = list_T.pop(0)
                                                                    if eof.getTipo() == 'EOF':
                                                                        return EliminarUnico(token,id,ig,new,ins,op,str,com,n,opc,string,n2,clc,clp,eof) 
                                                                    else:
                                                                        return Error_S('Sintactico','Expected ";" ')
                                                                else:
                                                                    return Error_S('Sintactico','Expected ")" ')
                                                            else:
                                                                return Error_S('Sintactico','Expected "}" ')
                                                else:
                                                    return Error_S('Sintactico','Expected "{" ')
                                        else:
                                            return Error_S('Sintactico','Expected "," ')   
                                else:
                                    return Error_S('Sintactico','Expected "(" ')
                        else:
                            return Error_S('Sintactico','Falta palabra reservada, Expected: nueva')  
            #BuscarTodo ->   BuscarTodo : BuscarTodo ID = nueva BuscarTodo ( STRING );
            elif token.getTipo() == 'instruccion' and token.getLex() == 'BuscarTodo':
                id = list_T.pop(0)
                if id.getTipo() == 'ID':
                    ig = list_T.pop(0)
                    if ig.getTipo() == 'reservada' and ig.getLex() == '=':
                        res = list_T.pop(0)
                        if res.getTipo()=='reservada' and res.getLex() == 'nueva':
                            ins = list_T.pop(0)
                            if ins.getTipo() == 'instruccion' and ins.getLex() == 'BuscarTodo':
                                op = list_T.pop(0)
                                if op.getTipo() == 'reservada' and op.getLex() == '(':
                                    str = list_T.pop(0)
                                    if str.getTipo() == 'string':
                                        cl = list_T.pop(0)
                                        if cl.getTipo() == 'reservada' and cl.getLex() == ')':
                                            eof = list_T.pop(0)
                                            if eof.getTipo() == 'EOF':
                                                return BuscarTodo(token,id,ig,res,ins,op,str,cl,eof)
                                            else:
                                                return Error_S('Sintactico','Expected ";" ')
                                        else:
                                            return Error_S('Sintactico','expected: ")" ')
                                else:
                                    return Error_S('Sintactico','expected: "(" ')
                        else:
                            return Error_S('Sintactico','Falta palabra reservada, Expected: nueva')
            #BuscarUnico -> BuscarUnico : BuscarUnico ID = nueva BuscarUnico ( STRING );
            elif token.getTipo() == 'instruccion' and token.getLex() == 'BuscarUnico':
                id = list_T.pop(0)
                if id.getTipo() == 'ID':
                    ig = list_T.pop(0)
                    if ig.getTipo() == 'reservada' and ig.getLex() == '=':
                        res = list_T.pop(0)
                        if res.getTipo()=='reservada' and res.getLex() == 'nueva':
                            ins = list_T.pop(0)
                            if ins.getTipo() == 'instruccion' and ins.getLex() == 'BuscarUnico':
                                op = list_T.pop(0)
                                if op.getTipo() == 'reservada' and op.getLex() == '(':
                                    str = list_T.pop(0)
                                    if str.getTipo() == 'string':
                                        cl = list_T.pop(0)
                                        if cl.getTipo() == 'reservada' and cl.getLex() == ')':
                                            eof = list_T.pop(0)
                                            if eof.getTipo() == 'EOF':
                                                return BuscarUnico(token,id,ig,res,ins,op,str,cl,eof)
                                            else:
                                                return Error_S('Sintactico','Expected ";" ')
                                        else:
                                            return Error_S('Sintactico','expected: ")" ')
                                else:
                                    return Error_S('Sintactico','expected: "(" ')
                        else:
                            return Error_S('Sintactico','Falta palabra reservada, Expected: nueva')
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

    # for a in Acept:
    #     print(a.getCommand())
    
    # for e in E_Sintacticos:
    #     print(e.getArg())
