reserv = {
    "CrearBD"           :"CrearBD",
    "EliminarBD"        :"EliminarBD",
    "CrearColeccion"    :"CrearColeccion",
    "EliminarColeccion" :"EliminarColeccion",
    "InsertarUnico"     :"InsertarUnico",
    "ActualizarUnico"   :"ActualizarUnico",
    "EliminarUnico"     :"ActualizarUnico",
    "BuscarTodo"        :"BuscarTodo",
    "BuscarUnico"       :"BuscarUnico",
    "nueva"             :"nueva",
    "OpenComentario"    :"/*",
    "CloseComentario"   :"*/",
    "ComentarioLine"    :"---",
    "llaveA"            :"{",
    "llaveC"            :"}",
    "DosP"              :":",
    "coma"              :",",
    "igual"             :"="
}

reservadas = list(reserv.values())

for lexema in reservadas:
    print(lexema)