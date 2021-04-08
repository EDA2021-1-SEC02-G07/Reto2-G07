import time
import tracemalloc
import config as cf
import model
import csv


def iniciarC():
    catalogo = model.NCatalogo()
    return catalogo

# Funciones para la carga de datos
def loadData(catalogo):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    # TODO: modificaciones para medir el tiempo y memoria
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    

    loadV(catalogo)
    loadCat(catalogo)


    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return delta_time, delta_memory

def iniciarC():
    catalogo = model.NCatalogo()
    return catalogo

# Funciones para la carga de datos

def loadV(catalogo):
    videosfile = cf.data_dir + 'videos-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for videosfile in input_file:
        model.addV(catalogo, videosfile)

def loadCat(catalogo):
    catfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(catfile, encoding='utf-8'), delimiter = '\t')
    for cat in input_file:
        model.addCat(catalogo, cat)

# Funciones de ordenamiento


# Funciones de consulta sobre el catálogo
def getTendPais(catalogo, pais, cate):
    return model.TendPais(catalogo, pais, cate)

def getDiasPais(catalogo, pais):
    return model.DiasPais(catalogo, pais)

def getDiasCat(catalogo, categoria):
    return model.DiasCat(catalogo, categoria)

def getLikesTag(catalogo, tag):
    return model.LikesTag(catalogo, tag)

#DEBUG
def getdebug(catalog):
    return model.debug(catalog)

def getTime():

#devuelve el instante tiempo de procesamiento en milisegundos

    return float(time.perf_counter()*1000)

def getMemory():

#toma una muestra de la memoria alocada en instante de tiempo

    return tracemalloc.take_snapshot()

def getMemory():

#toma una muestra de la memoria alocada en instante de tiempo

    return tracemalloc.take_snapshot()

def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory



