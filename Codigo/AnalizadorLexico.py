import ply.lex as lex

# Lista de tokens
tokens = [
    'NOMBRE',
    'DIRECCION',
    'NUMERO',
    'ARCH',
    'OCUPACION',
    'APARENT',
    'CPARENT',
    'COMA',
]

# Palabras Reservadas
reservadas = {
    'inicia':   'INICIA',
    'crea':     'CREA',
    'abre':     'ABRE',
    'ingresa':  'INGRESA',
    'lista':    'LISTA',
    'muestra': 'MUESTRA',
    'cierra': 'CIERRA',
    'termina': 'TERMINA'}

# Añadiendo las palabras reservadas a los tokens
tokens = tokens + list(reservadas.values())

# Expresión Regular para los Símbolos
t_APARENT  = r'\('
t_CPARENT  = r'\)'
t_COMA  = r'\,'


# Expresión Regular para INICIA
def t_INICIA(t):
     r'inicia'
     t.type = reservadas.get(t.value, 'INICIA')
     return t

# Expresión Regular para CREAR
def t_CREA(t):
     r'crea'
     t.type = reservadas.get(t.value, 'CREA')
     return t

# Expresión Regular para ABRE
def t_ABRE(t):
     r'abre'
     t.type = reservadas.get(t.value, 'ABRE')
     return t    

# Expresión Regular para INGRESA
def t_INGRESA(t):
     r'ingresa'
     t.type = reservadas.get(t.value, 'INGRESA')
     return t  

# Expresión Regular para LISTA
def t_LISTA(t):
     r'lista'
     t.type = reservadas.get(t.value, 'LISTA')
     return t
# Expresión Regular para MUESTRA
def t_MUESTRA(t):
     r'muestra'
     t.type = reservadas.get(t.value, 'MUESTRA')
     return t  
# Expresión Regular para CIERRA
def t_CIERRA(t):
     r'cierra'
     t.type = reservadas.get(t.value, 'CIERRA')
     return t 

# Expresión Regular para TERMINA
def t_TERMINA(t):
     r'termina'
     t.type = reservadas.get(t.value, 'TERMINA')
     return t  

# Expresión Regular para los Nombre
def t_NOMBRE(t):
    r'[A-ZÑ][a-zñ]+[ ][A-ZÑ][a-zñ]+'
    t.value = t.value
    return t

# Expresión Regular para las Direcciones
def t_DIRECCION(t):
    r'[A-ZÑ][a-zñ]+[ ][0-9]+'
    t.value = t.value
    return t

# Expresión Regular para los Codigos y Edades
def t_NUMERO(t):
    r'[0-9]+'
    t.value = t.value
    return t

# Expresión Regular para los Archivos
def t_ARCH(t):
    r'[a-zñ]+ \. txt'
    t.value = t.value
    return t

# Expresión Regular para las Ocupaciones
def t_OCUPACION(t):
    r'([a-zñ]+[ ]*)+'
    t.value = t.value
    return t

# Reglas para los saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Caracteres que se ignoran (espacios y tabulaciones)
t_ignore  = ' \t'

# Error
def t_error(t):
    print("Caracter no identificado '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
