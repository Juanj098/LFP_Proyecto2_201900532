from lexico.Lexico import Analizador_L
from lexico.Lexico import instrucciones_
Json = '''/*
        es un
        comentario de
        varias lineas
    */
    --- es un comentario de una linea
    CrearBD proyecto = nueva CrearBD();
    EliminarBD elimina = nueva EliminarBD();
    CrearColeccion colec = nueva CrearColeccion("NameColeccion");
    EliminarColeccion EliminarColecc = nueva EliminarColeccion("NameColeccion");
    InsertarUnico insertadoc = nueva InsertarUnico("NameColeccion",
            {
                "nombre":"Obra Literaria",
                "autor":"Jorge Luis"    
            }
    );
    ActualizarUnico actualizadoc = nueva ActualizarUnico("NameColeccion",
            {
                "nombre":"obra literaria"
            },
            {
                $set:{"autor":"Mario Vargas"}
            }
    );
    EliminarUnico eliminadoc = nueva EliminarUnico("NameColeccion",
            {
                "nombre":"obra literaria"  
            }
        );
    BuscarUnico todo = nueva BuscarUnico("NameColeccion");
    BuscarTodo todo = nueva BuscarTodo("NameColeccion");
'''
Analizador_L(Json)
instruccion = instrucciones_()
print(instruccion)  

