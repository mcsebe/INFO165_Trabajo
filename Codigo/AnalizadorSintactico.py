import ply.yacc as yacc

from AnalizadorLexico import tokens

def p_inicia(p):
    'A : INICIA'
    result.append("Bienvenido!\n")

def p_termina(p):
    'A : TERMINA'
    result.append("Adios\n")

def p_crea(p):
    'A : CREA APARENT ARCH CPARENT'
    global f
    f = open( './Datos/' + p[3], "w+")

def p_abre(p):
    'A : ABRE APARENT ARCH CPARENT'
    try:
        global f
        f = open('./Datos/' + p[3], "r+")
    except:
        result.append("El archivo no existe!\n")

def p_ingresa(p):
    'A : INGRESA APARENT NUMERO COMA NOMBRE COMA NUMERO COMA OCUPACION COMA DIRECCION CPARENT'
    global f
    try:
         f.write("{:<3} {:<18} {:<4} {:<18} {:<18}\n".format(p[3], p[5], p[7], p[9], p[11]))
    except:
        result.append("No se ha abierto ningún archivo!\n")

def p_lista(p):
    'A : LISTA'
    try:
        global f
        f.seek(0)
        result.append("{:<3} {:<18} {:<4} {:<18} {:<18}\n".format("ID", "Nombre", "Edad", "Ocupación", "Dirección"))
        result.append("{:<3} {:<18} {:<4} {:<18} {:<18}\n".format("--", "------", "----", "---------", "---------"))
        result.append(f.read()[0:-1] + "\n")
    except:
        result.append("No se ha abierto ningún archivo!\n")

def p_muestra(p):
    'A : MUESTRA APARENT NUMERO CPARENT'
    try:
        f.seek(0)
        result.append("{:<3} {:<18} {:<4} {:<18} {:<18}\n".format("ID", "Nombre", "Edad", "Ocupación", "Dirección"))
        result.append("{:<3} {:<18} {:<4} {:<18} {:<18}\n".format("--", "------", "----", "---------", "---------"))
        for i in f.read()[0:-1].split("\n"):
            if(p[3] == i.split(" ")[0]):
                result.append(i + "\n")
    except:
        result.append("No se ha abierto ningún archivo!\n")

def p_cierra(p):
    'A : CIERRA'
    global f
    f.close()

def p_error(p):
    result.append("Error de sintaxis!\n")

parser = yacc.yacc()

def Analizar(palabra):
    global result
    result = []
    parser.parse(palabra)
    return result
