class Coment:
    def __init__(self, Abre,cuerpo,cierra) -> None:
        self.open = Abre
        self.cuerpo = cuerpo
        self.close = cierra

    def getIns(self):
        return f'{self.open.getLex()} {self.cuerpo.getLex()}{self.close.getLex()}'

    def getCommand(self):
        return f'{self.open.getLex()} {self.cuerpo.getLex()}{self.close.getLex()}'
    
class CrearBD():
    def __init__(self,instruccion,id,reserv,nueva,crear,open,close,ptcom) -> None:
        self.ins = instruccion
        self.id = id
        self.res = reserv
        self.nueva = nueva
        self.crear = crear
        self.op = open
        self.clo = close
        self.ptcom = ptcom 
    
    def getIns(self):
        return self.ins.getLex()

    def getID(Self):
        return Self.id.getLex()

    def getCommand(self):
        return f'{self.ins.getLex()} {self.id.getLex()} {self.res.getLex()} {self.nueva.getLex()} {self.crear.getLex()}{self.op.getLex()}{self.clo.getLex()}{self.ptcom.getLex()}'

class EliminarBD():
    def __init__(self,instruccion,id,reserv,nueva,eliminar,open,close,ptcom) -> None:
        self.ins = instruccion
        self.id = id
        self.res = reserv
        self.nueva = nueva
        self.delete = eliminar
        self.op = open
        self.clo = close
        self.ptcom = ptcom 
    
    def getIns(self):
        return self.ins.getLex()

    def getCommand(self):
        return f'{self.ins.getLex()} {self.id.getLex()} {self.res.getLex()}  {self.nueva.getLex()} {self.delete.getLex()}{self.op.getLex()}{self.clo.getLex()}{self.ptcom.getLex()}'

class CrearColeccion:
    def __init__(self,instruccion,ID,igual,res,CrearColeccion,op,string,cl,eof) -> None:
        self.ins = instruccion
        self.id = ID
        self.igual = igual
        self.res = res
        self.cc = CrearColeccion
        self.op = op
        self.str = string
        self.cl = cl
        self.eof = eof
    
    def getID(self):
        return self.id.getLex()

    def getNameCollection(self):
        return self.str.getLex()
    
    def getIns(self):
        return self.ins.getLex()

    def getCommand(self):
        return f'{self.ins.getLex()} {self.id.getLex()} {self.igual.getLex()} {self.res.getLex()} {self.cc.getLex()} {self.op.getLex()} {self.str.getLex()} {self.cl.getLex()}{self.eof.getLex()}' 

class EliminarColeccion:
    def __init__(self,instruccion,ID,igual,res,CrearColeccion,op,string,cl,eof) -> None:
        self.ins = instruccion
        self.id = ID
        self.igual = igual
        self.res = res
        self.cc = CrearColeccion
        self.op = op
        self.str = string
        self.cl = cl
        self.eof = eof
    
    def getIns(self):
        return self.ins.getLex()
    
    def getNameCollection(Self):
        return Self.str.getLex()
    
    def getCommand(self):
        return f'{self.ins.getLex()} {self.id.getLex()} {self.igual.getLex()} {self.res.getLex()} {self.cc.getLex()} {self.op.getLex()} {self.str.getLex()}{self.cl.getLex()}{self.eof.getLex()}' 

class InsertarUnico:
    def __init__(self,ins,id,ig,new,inst,op,stro,com,n,opc,stru,n2,clc,clp,eof) -> None:
        self.ins = ins
        self.id = id
        self.ig = ig
        self.nue = new
        self.insert = inst
        self.op = op
        self.srto = stro
        self.com = com
        self.n = n
        self.opc = opc
        self.stru = stru
        self.n2 =n2
        self.clc = clc
        self.clp = clp
        self.eof = eof

    def getNameCollection(self):
        return self.srto.getLex()
    
    def getString(self):
        return self.stru

    def getIns(self):
        return self.ins.getLex()

    def mod(self,x):
        self.n = x

    def getCommand(self):
        return f'{self.ins.getLex()} {self.id.getLex()} {self.ig.getLex()} {self.nue.getLex()} {self.insert.getLex()} {self.op.getLex()} {self.srto.getLex()}{self.com.getLex()} {self.n.getLex()} {self.opc.getLex()}{self.stru}{self.n2.getLex()}{self.clc.getLex()}{self.clp.getLex()}{self.eof.getLex()}'

class ActualizarUnico:
    def __init__(self,ins,id,ig,new,inst,op,stro,com,n,opc,stru,clc,comx,n2,cor,n3,set,tp,coo,strings,cloc,n4,cc,n5,clp,eof) -> None:
        self.ins = ins
        self.id = id
        self.ig = ig
        self.nue = new
        self.insert = inst
        self.op = op
        self.srto = stro
        self.com = com
        self.n = n
        self.opc = opc
        self.stru = stru
        self.clc = clc
        self.comx = comx
        self.n2 = n2
        self.cor = cor
        self.n3 = n3
        self.set = set
        self.tp = tp
        self.coo = coo
        self.strings = strings
        self.cloc = cloc
        self.n4 = n4
        self.cc = cc
        self.n5 = n5
        self.clp = clp
        self.eof = eof

    def getNameCollection(self):
        return self.srto.getLex()

    def getStringu(self):
        return self.stru
    
    def getSet(self):
        return self.set.getLex()
    
    def getStringo(self):
        return self.strings

    def getIns(self):
        return self.ins.getLex()

    def getCommand(self):
        return f'{self.ins.getLex()} {self.id.getLex()} {self.ig.getLex()} {self.nue.getLex()} {self.insert.getLex()}{self.op.getLex()}{self.srto.getLex()}{self.com.getLex()}{self.n.getLex()}{self.opc.getLex()}{self.stru}{self.clc.getLex()}{self.comx.getLex()}{self.n2.getLex()}{self.cor.getLex()}{self.n3.getLex()}{self.set.getLex()}{self.tp.getLex()}{self.coo.getLex()}{self.strings}{self.cloc.getLex()}{self.n4.getLex()}{self.cc.getLex()}{self.n5.getLex()}{self.clp.getLex()}{self.eof.getLex()}'

class EliminarUnico:
    def __init__(self,ins,id,ig,new,inst,op,stro,com,n,opc,stru,n2,clc,clp,eof) -> None:
        self.ins = ins
        self.id = id
        self.ig = ig
        self.nue = new
        self.insert = inst
        self.op = op
        self.srto = stro
        self.com = com
        self.n = n
        self.opc = opc
        self.stru = stru
        self.n2 =n2
        self.clc = clc
        self.clp = clp
        self.eof = eof

    def getNameCollection(self):
        return self.srto.getLex()
    
    def getString(self):
        return self.stru
    
    def getIns(self):
        return self.ins.getLex()
 
    def mod(self,x):
        self.n = x

    def getCommand(self):
        return f'{self.ins.getLex()} {self.id.getLex()} {self.ig.getLex()} {self.nue.getLex()} {self.insert.getLex()} {self.op.getLex()} {self.srto.getLex()}{self.com.getLex()} {self.n.getLex()} {self.opc.getLex()}{self.stru}{self.n2.getLex()}{self.clc.getLex()}{self.clp.getLex()}{self.eof.getLex()}'
    
class BuscarUnico:
    def __init__(self,instruccion,ID,igual,res,CrearColeccion,op,string,cl,eof) -> None:
        self.ins = instruccion
        self.id = ID
        self.igual = igual
        self.res = res
        self.cc = CrearColeccion
        self.op = op
        self.str = string
        self.cl = cl
        self.eof = eof
    
    def getNameCollection(self):
        return self.str.getLex()
    
    def getIns(self):
        return self.ins.getLex()

    def getCommand(self):
        return f'{self.ins.getLex()} {self.id.getLex()} {self.igual.getLex()} {self.res.getLex()} {self.cc.getLex()} {self.op.getLex()} {self.str.getLex()} {self.cl.getLex()}{self.eof.getLex()}' 
class BuscarTodo:
    def __init__(self,instruccion,ID,igual,res,CrearColeccion,op,string,cl,eof) -> None:
        self.ins = instruccion
        self.id = ID
        self.igual = igual
        self.res = res
        self.cc = CrearColeccion
        self.op = op
        self.str = string
        self.cl = cl
        self.eof = eof
    
    def getIns(self):
        return self.ins.getLex()

    def getNameCollection(self):
        return self.str.getLex()

    def getCommand(self):
        return f'{self.ins.getLex()} {self.id.getLex()} {self.igual.getLex()} {self.res.getLex()} {self.cc.getLex()} {self.op.getLex()} {self.str.getLex()} {self.cl.getLex()}{self.eof.getLex()}' 
class Error_S:
    def __init__(self,tipo,argumento) -> None:
        self.tipo = tipo
        self.args = argumento
    
    def getArg(self):
        return self.args
    