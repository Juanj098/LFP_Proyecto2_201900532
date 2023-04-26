from lexico.Lexico import Analizador_L
from lexico.reservadas import list_reservadas

Json = '''
    /*
        es un
        comentario de
        varias lineas
    */
    --- es un comentario de una linea
    CrearBD proyecto = nueva crearBD();
    EliminarBD elimina = nueva Eliminar();
    CrearColeccion colec = nueva CrearColeccion("NameColeccion");
    EliminarColeccion EliminarColecc = nueva EliminarColeccion("NameColeccion");
    InsertarUnico insertadoc = nueva InsertarUnico("NameColeccion",
            {
                "nombre":"Obre Literaria",
                "autor":"Jorge Luis"    
            }
    );
    ActualizarUnico actualizadoc = nueva EliminarUnico("NameColeccion",
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
    BuscarTodo todo = nueva BuscarTodo("NameColeccion");
    BuscarUnico todo = nueva BuscarUnico("NameColeccion");
'''
analisis = Analizador_L(Json)
print(analisis)
