class Coment:
    def __init__(self, Abre,cuerpo,cierra) -> None:
        self.open = Abre
        self.cuerpo = cuerpo
        self.close = cierra

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
    
    def getCommand(self):
        return f'{self.ins.getLex()}'
        #{self.id.getLex()} {self.res.getLex()} {self.nueva.getLex()} {self.delete.getLex()}{self.op.getLex()}{self.clo.getLex()}{self.ptcom.getLex()}'

class Error_S:
    def __init__(self,tipo,argumento) -> None:
        self.tipo = tipo
        self.args = argumento
    
    def getArg(self):
        return self.args