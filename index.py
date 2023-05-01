from lexico.Lexico import Analizador_L
from lexico.Lexico import instrucciones_
from sintactico.Sintactico import sintactico
from sintactico.Sintactico import toks
from analisis import analisis
from analisis import command
from analisis import result


Json = '''
    /*
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
Json2 ='''
    CrearBD cali = nueva CrearBD();
    CrearColeccion colecu = nueva CrearColeccion("Coleccionuno");
    CrearColeccion colecd = nueva CrearColeccion("Colecciondos");
    CrearColeccion colect = nueva CrearColeccion("Colecciontres");
    InsertarUnico uno = nueva InsertarUnico("Coleccion1",
	    {
		    "id": 1,
		    "nombre": "Calificacion",
		    "anio": 2023,
		    "curso": "Lenguajes Formales y de Programacion"
	    }
    );
    InsertarUnico dos = nueva InsertarUnico("Coleccion",
	    {
		    "id": 1,
		    "nombre" : "Calificacion 2",
		    "anio": 2023,
		    "curso": "Introduccion a la Programacion 2"
	    }
    );
    EliminarColeccion c = nueva EliminarColeccion("Colecciondos");

    ActualizarUnico ac = nueva ActualizarUnico("Coleccionuno",
	        {
		        "id" : 1
	        },
	        {
		        $set: {"curso": "Oficialmente estoy en Compi 1"}
        	}
    );
    EliminarUnico el = nueva EliminarUnico("Coleccionuno",
	        {
		        "id" : 2
	        }
    );
    BuscarTodo todo = nueva BuscarTodo("Coleccion1");
'''
# Analizador_L(Json2)
# instruccion = instrucciones_()
# print(instruccion)  

# sintactico(Json2)
# t=toks()
# print(t)

analisis(Json)
r=command()
print(r)