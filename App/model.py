from DISClib.DataStructures.arraylist import getElement, isPresent
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
import DISClib.DataStructures.listiterator as it
from DISClib.Algorithms.Sorting import quicksort as quick
assert cf

# Construccion de modelos
def NCatalogo():
    catalogo = {'videos': None,
            'videosID': None,
            'categorias': None,
            'categoriasID': None,
            'paises': None,
            'cat_vid': None}

    catalogo['videos'] = lt.newList('ARRAY_LIST', cmpfunction = cmpV_id)
    catalogo['videosID'] = mp.newMap(10000, maptype='CHAINING', loadfactor=4.0, comparefunction=cmpMapV_id)
    
    catalogo['paises'] = lt.newList('ARRAY_LIST', cmpfunction = cmpPais)
    

    catalogo['categorias'] = mp.newMap(64, maptype= 'PROBING', loadfactor=0.5, comparefunction=cmpMapCatN)
    catalogo['categoriasID'] = mp.newMap(64, maptype='CHAINING', loadfactor=4.0, comparefunction=cmpMapCatID)

    catalogo['cat_vid'] = lt.newList('ARRAY_LIST', cmpfunction = cmpPais)
    return catalogo
   
# Funciones para agregar informacion al catalogo
def addV(catalog, video):
    lt.addLast(catalog['videos'], video)
    mp.put(catalog['videosID'], video['video_id'], video)
    paises = video['country']
    categorias = video['category_id']
    addPais(catalog, paises, video)
    addCatVid(catalog, categorias, video)

def addCat(catalog, categoria):
    newC = newCat(categoria['name'], categoria['id'])
    mp.put(catalog['categorias'], categoria['name'], newC)
    mp.put(catalog['categoriasID'], categoria['id'], newC)

def addPais(catalog, pais, video):
    paises = catalog['paises']
    existP = mp.contains(paises, pais)
    if existP:
        entry = mp.get(paises, pais)
        p = me.getValue(entry)
    else:
        p = newP(pais)
        mp.put(paises, pais, p)
    lt.addLast(p['videos'], video)

def addCatVid(catalog, cate, video):
    vidID = video['video_id']
    catID = video['category_id']
    entry = mp.get(catalog['categoriasID'], catID)

    if entry:
        catbook = mp.get(catalog['categorias'], me.getValue(entry)['name'])
        catbook['value']['totalV'] += 1
        catbook['value']['count'] += int(video['count'])


    categorias = catalog['cat_vid']
    posC = lt.isPresent(categorias, cate)
    if posC > 0:
        catN = lt.getElement(categorias, posC)
    else:
        catN = newP(cate)
        lt.addLast(categorias, catN)
    lt.addLast(catN['videos'], video)

# Funciones para creacion de datos
def newCat(name, id):
    cat = {'nombre': '', 'cat_id': '', 'total_v': 0, 'videos': None, 'count': 0.0}
    cat['nombre'] = name
    cat['cat_id'] = id
    cat['videos'] = lt.newList('ARRAY_LIST', cmpfunction = cmpPais)
    return cat

def newP(name):
    pais = {'nombre': '', 'videos': None}
    pais['nombre'] = name
    pais['videos'] = lt.newList('ARRAY_LIST', cmpfunction = cmpV_id)
    return pais

# Funciones de consulta
def TendPais(catalogo, pais, cate):
    pais = pais.lower()
    cate = cate.lower()
    ide = getID(catalogo, cate)
    paises = getLtPais(catalogo, pais)
    categorias = getltCat(catalogo, ide['cat_id'])
    pCheat = []
    cCheat = []
    final = lt.newList('ARRAY_LIST', cmpfunction = cmpV_id)
    iterator = it.newIterator(paises['videos'])
    while it.hasNext(iterator):
        x = it.next(iterator)
        x = frozenset(x.items())
        pCheat.append(x)
    iterator = it.newIterator(categorias['videos'])
    while it.hasNext(iterator):
        x = it.next(iterator)
        x = frozenset(x.items())
        cCheat.append(x)
    if len(pCheat) < len(cCheat):
        SuperCheat = list(set(pCheat).intersection(cCheat))
    else:
        SuperCheat = list(set(cCheat).intersection(pCheat))
    for x in SuperCheat:
        lt.addLast(final, dict(x))
    top = sortVideos(final, cmpViews, quick)
    return top

def DiasPais(catalogo, pais):
    #video que más días ha sido trending para un país específico.
     pospais = lt.isPresent(catalogo['paises'],pais)
     lista = lt.getElement(catalogo['paises'], pospais)

     mayor = 0
     final = lt.newList()

     videos = lista['videos']['elements']
    
    
     for video in videos:
         publicado = video['publish_time']
         trending = video ['trending_date']

         dias= int(trending[3:5])-int(publicado[8:10])
         mes =(int(trending[6:8])-(int(publicado[5:7])))*30 
         
         año =(int(trending[0:2])-int(publicado[2:4]))*365
         dias_d = año+mes+dias
         print(dias_d)
         if dias_d>mayor:
             final = video
             mayor = dias_d
     final[1]= mayor
     
     return (final)
 
def DiasCat(catalogo, categoria):
    cat = categoria.lower()
    c_id = getID(catalogo, cat)
    videos = getltCat(catalogo, c_id['cat_id'])
    #Para usar videos hay que usar videos['videos']
    cont = {}
    iterator = it.newIterator(videos['videos'])
    while it.hasNext(iterator):
        x = it.next(iterator)
        if x['video_id'] in cont:
            cont[x['video_id']] +=1
        else:
            cont[x['video_id']] = 1
    if '#NAME?' in cont:
        cont.pop('#NAME?')     
    v_id = list(cont.keys())
    days = list(cont.values())
    id_max = v_id[days.index(max(days))]
    return lt.getElement(videos['videos'], lt.isPresent(videos['videos'], id_max)), max(days)

def LikesTag(catalogo, tag):
    videos = catalogo['videos']
    tag = tag.lower()
    iterator = it.newIterator(videos)
    likes = lt.newList('ARRAY_LIST', cmpfunction = cmpV_id)
    while it.hasNext(iterator):
        x = it.next(iterator)
        if tag in x['tags'].lower():
            lt.addLast(likes, x)
    topDup = sortVideos(likes, cmpLikes, quick)
    top = lt.newList('ARRAY_LIST', cmpfunction = cmpV_id)
    iterator = it.newIterator(topDup)
    vidIDs = set()
    while it.hasNext(iterator):
        x = it.next(iterator)
        if x['video_id'] not in vidIDs:
            lt.addLast(top, x)
            vidIDs.add(x['video_id'])
    return top

# Funciones adicionales
def getLtPais(catalogo, pais):
    pos = lt.isPresent(catalogo['paises'], pais)
    if pos != 0:
        videos = lt.getElement(catalogo['paises'], pos)
        return videos

def getID(catalogo, cate):
    pos = lt.isPresent(catalogo['categorias'], cate)
    if pos != 0:
        ide = getElement(catalogo['categorias'], pos)
        return ide

def getltCat(catalogo, c_id):
    pos = lt.isPresent(catalogo['cat_vid'], c_id)
    if pos != 0:
        videos = lt.getElement(catalogo['cat_vid'], pos)
        return videos

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpViews(v1, v2):
    result = float(v1['views']) > float(v2['views'])
    return result

def cmpPais(name, pais):
    if (name.lower() in pais['nombre'].lower()):
        return 0
    return -1

def cmpV_id(name, vid):
    if (name.lower() in vid['video_id'].lower()):
        return 0
    return -1

def cmpLikes(v1, v2):
    result = float(v1['likes']) > float(v2['likes'])
    return result

def cmpMapV_id(id, entry):
    IDent = me.getKey(entry)
    if int(id) == int(IDent):
        return 0
    elif int(id) > int(IDent):
        return 1
    else:
        return -1

def cmpMapPais(keyname, pais):
    pent = me.getKey(pais)
    if keyname == pent:
        return 0
    elif keyname > pent:
        return 1
    else:
        return -1

def cmpMapCatN(name, cat):
    catE = me.getKey(cat)
    if name == catE:
        return 0
    elif name > catE:
        return
    else: 
        return -1

def cmpMapCatID(id, cat):
    catE = me.getKey(cat)
    if int(id) == int(catE):
        return 0
    elif int(id) > int(catE):
        return
    else: 
        return -1

# Funciones de ordenamiento
def sortVideos(lista, cmp_f, orde):
    lista = lista.copy()
    orde.sort(lista, cmp_f)
    return lista

#DEBUG
def debug(catalogo):
    '''Para que el computador no muera hay que hacer un break en
    controller.py con la cantidad de archivos deseados.'''
    print('\n', '\033[30m', '\033[1m', '\033[103m', 'No se han configurado opciones de debug.', '\033[0m', '\n')
    #print(catalogo['videos'])
    #print(catalogo['cat_vid'])
    #print(catalogo['paises'])
    #print(catalogo['categorias'])
    #print(lt.getElement(catalogo['paises'], 1))
    #print(lt.getElement(catalogo['cat_vid'], 1))
