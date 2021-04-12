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
    
    loadCat(catalogo)
    loadV(catalogo)


def iniciarC():
    catalogo = model.NCatalogo()
    return catalogo

# Funciones para la carga de datos
def loadCat(catalogo):
    catfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(catfile, encoding='utf-8'), delimiter = '\t')
    for cat in input_file:
        model.addCat(catalogo, cat)

def loadV(catalogo):
    st = time.time()
    videosfile = cf.data_dir + 'videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for videosfile in input_file:
        model.addVid(catalogo, videosfile)
    model.loadMaps(catalogo)
    fn = time.time()
    print(fn - st)
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




