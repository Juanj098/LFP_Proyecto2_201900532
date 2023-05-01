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
from sintactico.Sintactico import sintactico
from sintactico.Sintactico import toks
from sintactico.Sintactico import E_Sintacticos
from sintactico.Sintactico import Acept
from lexico.Lexico import list_T
from lexico.Lexico import list_E

list_commands = []


	# -CrearBD
	# -EliminarBD
	# -CrearColeccion
	# -EliminarColeccion
	# -InsertarUnico
	# -ActualizarUnico
	# -EliminarUnico
	# -BuscarTodo
	# -BuscarUnico

def analisis(cadena):
    sintactico(cadena)
    toks()

def result():
    if list_E:
        return 'Errores lexicos'
    elif E_Sintacticos:
        return 'Errores sintacticos'
    else:
        contador = 0
        while contador < len(Acept):
            obj = Acept.pop(0)
            x = isinstance(obj,Coment)
            if x == True:
                return obj.getIns()
            elif obj.getIns() == 'CrearBD':
            #   use proyecto
                return f'use {obj.getID()}'
            elif obj.getIns() == 'EliminarUnico':
            #   db.NameColeccion.deleteOne({"nombre":"obra literaria"})
                return f'db.{obj.getNameCollection()}.deleteOne({{{obj.getString()}}})'
            elif obj.getIns() == 'ActualizarUnico':
            #   db.NameColeccion.updateOne(
            #   {"nombre":"obra literaria"},
            #   {$set:{"autor":"Mario Vargas"}})
                return f'db.{obj.getNameCollection()}.updateOne({{{obj.getStringu()}}},\n{{\n{obj.getSet()}:{{{obj.getStringo()}}}\n}})'
            elif obj.getIns() == 'EliminarColeccion':
            #   db.NameColeccion.drop()
                return f'db.{obj.getNameCollection()}.drop()'
            elif obj.getIns() == 'BuscarUnico':
            #   db.NameColeccion.findOne({"nombre":"Obra Literaria"})        
                return f'db.{obj.getNameCollection()}.findOne()'
            elif obj.getIns() == 'BuscarTodo':
            #   db.NameColeccion.find()
                return f'db.{obj.getNameCollection()}.find()'
            elif obj.getIns() == 'InsertarUnico':
            #   db.NameColeccion.insertOne({
            #    "nombre":"Obra Literaria",
            #    "autor":"Jorge Luis"
            #   })
                return f'db.{obj.getNameCollection()}.insertOne({{{obj.getString()}}})'
            elif obj.getIns() == 'CrearColeccion':
            #   db.createCollection("NameColeccion")
                return f'db.createCollection("{{ {obj.getNameCollection()}}}")'
            elif obj.getIns() == 'EliminarBD':
            #   db.dropDatabase()
                return 'db.dropDatabase()'
    return None

def command():
    while True:
        tokens = result()
        if tokens:
            list_commands.append(tokens)
        else:
            break
    
    for com in list_commands:
        print(com)