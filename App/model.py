import time 
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
import DISClib.DataStructures.listiterator as it
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import quicksort as quick
assert cf

# Construccion de modelos
def NCatalogo():
    catalogo = {'videos': None, 'videosID': None, 'categorias': None, 'catIds': None, 'paises': None}

    catalogo['videos'] = lt.newList('ARRAY_LIST', cmpfunction=cmpSTR)
    #Llave es el ID del video
    catalogo['videosID'] = mp.newMap(688411, maptype='PROBING', loadfactor=0.693, comparefunction = cmpSTR)
    #Llave es el nombre de la categoría
    catalogo['categorias'] = mp.newMap(37, maptype='PROBING', loadfactor=0.693, comparefunction= cmpSTR)
    #Llave es el ID de la categoría
    catalogo['catIDs'] = mp.newMap(37, maptype='PROBING', loadfactor=0.693, comparefunction=cmpINT)
    #Llave es el nombre del país
    catalogo['paises'] = mp.newMap(337, maptype='PROBING', loadfactor=0.693, comparefunction = cmpSTR)
    #Llave es la ID de la categoría
    catalogo['catVid'] = mp.newMap(37, maptype='PROBING', loadfactor=0.693, comparefunction=cmpINT)

    return catalogo


# ==============================
# Funciones para creación de datos
# ==============================
def nuevoCatVideo(name, id):
    #relación entre un tag y los videos con el tag
    #tiene un total de videos con ese tag
    #crea una lista con los videos
    cat = {'id': '', 'name': '', 'videos': None}
    cat['name'] = name
    cat['id'] = id
    cat['videos'] = lt.newList('SINGLE_LINKED', cmpfunction=cmpSTR)
    return cat

def nuevoPais(name):
    #crea una lista con los videos por pais
    pais = {'name':'', 'videos':None}
    pais['name'] = name
    pais['videos'] = lt.newList('SINGLE_LINKED', cmpSTR)
    return pais

# ==============================
# Funciones para agregar info al catalogo
# ==============================
def addVid(catalog, video):
    #agrega un video a la lista de videos
    #también guarda el video en un map, usa el id para eso
    #se agrega en los canales una referencia al video
    #crea una entrada en el map de paises
    
    lt.addLast(catalog['videos'], video)
    '''if video['video_id'] != '#NAME?':
        mp.put(catalog['videosID'], video['video_id'], video)
    addVideoPais(catalog, video)
    addVideoCat(catalog, video)'''
    
    

def loadMaps(catalog):
    orden = sortVideos(catalog['videos'], cmpViewsReverse, quick)
    iterator = it.newIterator(orden)
    while it.hasNext(iterator):
        x = it.next(iterator)
        if x['video_id'] != '#NAME?':
            mp.put(catalog['videosID'], x['video_id'], x)
            addVideoPais(catalog, x)
            addVideoCat(catalog, x)

def addVideoPais(catalog, video):
    #agrega un pais a la lista de paises
    paises = catalog['paises']
    pais = video['country'].lower().strip()
    if mp.contains(paises, pais):
        paisf = me.getValue(mp.get(paises, pais))
    else:
        paisf = nuevoPais(pais)
        mp.put(paises, pais, paisf)
    
    lt.addLast(paisf['videos'], video['video_id'])
 
def addCat(catalog, cat):
    #actualiza una categoria a la tabla de categorias de catlogo
    newC = nuevoCatVideo(cat['name'].lower().strip(), cat['id'])
    mp.put(catalog['categorias'], cat['name'].lower().strip(), cat['id'])
    mp.put(catalog['catIDs'], cat['id'], cat['name'].lower().strip())
    mp.put(catalog['catVid'], cat['id'], newC)

def addVideoCat(catalog, video):
    catIDs = catalog['catIDs']
    catVid = catalog['catVid']
    cat = video['category_id']
    name = me.getKey(mp.get(catIDs, cat))
    if mp.contains(catVid, cat):
        catf = me.getValue(mp.get(catVid, cat))
    else:
        catf = nuevoCatVideo(name ,cat)
        mp.put(catVid, cat, catf)

    lt.addLast(catf['videos'], video['video_id'])

# ==============================
# Funciones de consulta
# ==============================
def TendPais(catalogo, pais, cat):
    pais = pais.lower()
    cat = cat.lower()
    paises = catalogo['paises']
    catVid = catalogo['catVid']
    catID = me.getValue(mp.get(catalogo['categorias'], cat))
    Lpais = me.getValue(mp.get(paises, pais))['videos']
    Lcat = me.getValue(mp.get(catVid, catID))['videos']
    pIDs = []
    cIDs = []
    vidIDs = lt.newList('ARRAY_LIST', cmpfunction=cmpSTR)

    iterator = it.newIterator(Lpais)
    while it.hasNext(iterator):
        x = it.next(iterator)
        pIDs.append(x)

    iterator = it.newIterator(Lcat)
    while it.hasNext(iterator):
        x = it.next(iterator)
        cIDs.append(x)

    if len(pIDs) < len(cIDs):
        inter = list(set(pIDs).intersection(cIDs))
    else:
        inter = list(set(cIDs).intersection(pIDs))
    
    for x in inter:
        lt.addLast(vidIDs, me.getValue(mp.get(catalogo['videosID'], x)))
    orden = sortVideos(vidIDs, cmpViews, quick)
    return orden

def DiasPais(catalogo, pais):
    pais = pais.lower().strip()
    paises = catalogo['paises']
    vidP = me.getValue(mp.get(paises, pais))['videos']
    iterator = it.newIterator(vidP)
    maxdict = {}
    while it.hasNext(iterator):
        x = it.next(iterator)
        if x in maxdict:
            maxdict[x] +=1
        else:
            maxdict[x] = 1
    keys = list(maxdict.keys())
    values = list(maxdict.values())
    maxV = values.index(max(values))
    topD = keys[maxV]
    dTop = values[maxV]
    video = me.getValue(mp.get(catalogo['videosID'], topD))
    
    return video, dTop 




def DiasCat(catalogo, category_name):
    #num de categoria
    category_name = category_name.lower()
    categoria = mp.get(catalogo['categorias'], category_name)
    num = categoria['value']
    # map con videos por categoria
    vid = mp.get(catalogo['catVid'], num)
    
    final = {}
    maxi = 0
    fin = None
    if vid:
        #obtiene videos
        categorias = me.getValue(vid)['videos']
        iterator = it.newIterator(categorias)
        
        #recorrido
        while it.hasNext(iterator):
            x = it.next(iterator)
            if x in final:
                final[x]+=1
            
            else:
                final[x]=1

            if final[x]> maxi:
                maxi = final[x]
                fin = x

    print(fin, maxi)






    
    

    return None

# ==============================
# Funciones de Comparacion
# ==============================
def cmpViews(v1, v2):
    result = float(v1['views']) > float(v2['views'])
    return result

def cmpViewsReverse(v1, v2):
    result = float(v1['views']) < float(v2['views'])
    return result

def cmpSTR(name, cat): 
    entry = me.getKey(cat)
    if (name == entry):
        return 0
    elif (name > entry):
        return 1
    else:
        return -1

def cmpINT(id, categoria):
    tagentry = me.getKey(categoria)
    if (int(id) == int(tagentry)):
        return 0
    elif (int(id) > int(tagentry)):
        return 1
    else:
        return 0


# ==============================
# Funciones de ordenamiento
# ==============================
def sortVideos(lista, cmp_f, orde):
    lista = lista.copy()
    orde.sort(lista, cmp_f)
    return lista

# ==============================
# DEBUG
# ==============================
def debug(catalog):
    #print(me.getValue(mp.get(catalog['videosID'], 'rK9L7t0Pl-E')))
    print(catalog['videosID'])

 

