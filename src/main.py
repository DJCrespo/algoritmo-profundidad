from simpleai.search import SearchProblem, astar

# Búsqueda por profundidad
###
# Tenemos 2 estados, el objetivo y el incial, donde la 'e' es la aspiradora
# ###

objetivo = '''0-e-0'''

# inicial = '''1-e-1'''

# Conversiones de la lista a cadena y viceversa

def string2list(lista):
    return lista.split('-')

def list2string(lista):
    return '-'.join(lista)

# comprueba si el estado actual es el objetivo

def isObjective(state):
    return state == objetivo

# acciones de la aspiradora

def clean(state, positionAspirator):
    for i in state:
        if state.index(i) == positionAspirator:
            if i == '1':
                state[positionAspirator] = '0'
                return state
            else:
                return state

def detectedSpaces(state):
    for i in state:
        if i == 'e':
            index = state.index(i)
            derecha = True if (index + 1) < 3 else False
            izquierda = True if (index - 1) > -1 else False
            return izquierda, derecha, index
        
def moveLeft(state, list):
    if state[0] == False and state[1] == True:
        return list
    if state[0] == True and state[1] == True:
        newPosition = state[3] - 1
        newState = clean(list, newPosition)
        return newState
        
def moveRight(state, list):
    if state[0] == True and state[1] == False:
        return list
    if state[0] == True and state[1] == True:
        newPosition = state[3] + 1
        newState = clean(list, newPosition)
        return newState
        
# Problema de búsqueda
print('Hola, soy la aspiradora; ¿me ayudas a limpiar la casa? Por favor, ingresa el estado inicial de la casa: formato -> 1-e-1')
estadoInicial = input()
check = isObjective(estadoInicial)
if check == True:
    print('La casa ya está limpia, hasta luego')
else:
    while check == False:
        list = string2list(estadoInicial)
        positions = detectedSpaces(list)
        newState = moveLeft(positions, list)
        print(newState)
        comprobation = isObjective(list)
        if comprobation == True:
            check = True
        else:
            newState = moveRight(positions, list)
            print(newState)
            comprobation = isObjective(list)
            if comprobation == True:
                check = True