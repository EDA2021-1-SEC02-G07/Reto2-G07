import config as cf
import model
import csv

def iniciarC():
    catalogo = model.NCatalogo()
    return catalogo

# Funciones para la carga de datos
def loadData(catalogo):
    loadV(catalogo)
    loadCat(catalogo)

def loadV(catalogo):
    videosfile = cf.data_dir + 'videos-large.csv'
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