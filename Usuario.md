# **Manual de Usuario** :octopus:

##Descripcion de Proyecto

El proyecto consiste en crear una herramienta capaz de traducir un conjunto de instrucciones escritas en un formato simple a instrucciones de una base de datos no relacionales como lo es MongoDB.

###**Funciones de entrada**
    1. CrearDB
    2. EliminarDB
    3. CrearColeccion
    4. EliminarColeccion
    5. InsertarUnico
    6. ActualizarUnico
    7. BuscarTodo
    8. BuscarUnico
   
###**Entrada de Datos**

El programa recibe datos con un formato simple como se mostrara:

```Python
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
```

###**Interfaz de usuario**

La interfaz es simple y agradable al usuario, donde posee 2 areas de visualizacion, 1 donde se puede editar la entrada y otro donde se visualizan el codigo obtenido o los errore lexicos o sintacticos.

####**FUNCION DE BOTONES**
|   BOTON |    FUNCION       |
|---------|------------------|
|ABRIR    |Abre archivos con extension  *.lfp|
|GUARDAR  |Guarda los cambios efectuados en el archivo|
|ANALIZAR |Analiza la entrada y verifica si hay algun error o devuelve las instrucciones en sintaxis de MongoDB|
|ERRORES  | muestra los errores que posee el texto|
|SALIR    |Finaliza el programa|

![imagen de interfaz](mdsource\interfaz.png)

![imagen interzas abrir archivos](mdsource\30232645.png)

![imagen de interfaz 2](mdsource\interfaz2.png)