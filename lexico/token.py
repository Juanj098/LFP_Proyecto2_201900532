class Token:
    def __init__(self,tipo,token) -> None:
        self.tipo = tipo
        self.token = token

    def getToken(self):
        return f'tipo ->{self.tipo}, token ->{self.token}'

    def getLex(self):
        return self.token

    def getTipo(self):
        return self.tipo
    
    def mod(self,x):
        self.token = x


class comentario:
    def __init__(self,token,argumento) -> None:
        self.token = token
        self.args = argumento

    def getComent(self):
        return self.args
    
