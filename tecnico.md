#**MANUAL TECNICO** :elephant:

##Descricion del proyecto

se realizo una herramienta que es capaz de analizar una entrada de datos con una sintaxis sencilla la cual se analizaba con ayuda de un analizador lexico y un analizador sintactico luego era capaz de transformar esas funciones a un lenguaje de base de datos no relacionales como lo es mongoDB

### Lenguaje utilizado
 |pythom|
 |------|
 |![python](mdsource\descarga.png)|

##Analizador lexico y sintactico

* **analizador lexico:** primera fase de un compilador que se encarga de analizar el codigo fuente de un programa y dividirlo en unidades lexicas o tokens. Se en carga de analizar una cadena de caracteres y agruparlos en tokens que representan los elementos lexicos del lenguaje.
  
  |lista de tokens|lexemas|
  |---------------|--------|
  |simbolos |, {} () : |
  |digitos|0-9|
  |string|[a-zA-Z]*|
  |ID|[a-z_A-Z_][a-z_A-Z_0-9]*|
  |comentarios|/* */ ---|

  |palabras reservadas|
  |-------------------|
  |Nueva|
  |Creardb|
  |EliminarDB|
  |BuscarUnico|
  |BuscarTodo|
  |CrearColeccion|
  |Eliminarcoleccion|
  |InsertarUnico|
  |ActualizarUnico|


  ### Automata utilizado
   
![automata](mdsource\automata_L.jff.png)

* **Analizador Sintactico:** tambien es conocido como parser es un componente fundamental de un compilador o intérprete que se encarga de analizar la estructura sintáctica de un programa de acuerdo a una gramática formal que describe las reglas sintácticas del lenguaje en cuestión.

 ### Sintaxis de las funciones

     instruccion : crearDB ;
                | eliminarDB ; 
                | crearColeccion ;
                | eliminarColeccion ;
                | insertarUnico ;
                | actualizarUnico ;
                | eliminarUnico ;
                | buscarTodo ;
                | buscarUnico ;


    crearDB : CrearDB ID = nueva CrearDB ( )

    eliminarDB : EliminarDB ID = nueva EliminarDB ( )

    crearColeccion : CrearColeccion ID = nueva CrearColeccion ( STRING )

    eliminarColeccion : EliminarColeccion ID = nueva EliminarColeccion ( STRING )

    insertarUnico : InsertarUnico ID = nueva InsertarUnico ( STRING , STRING )

    actualizarUnico : ActualizarUnico ID = nueva ActualizarUnico ( STRING , STRING )

    eliminarUnico : EliminarUnico ID = nueva EliminarUnico ( STRING )

    buscarTodo : BuscarTodo ID = nueva BuscarTodo ( STRING )

    buscarUnico : BuscarUnico ID = nueva BuscarUnico ( STRING )