"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def NCatalogo():
    catalogo = {'videos': None,
            'videosIds': None,
            'canales': None,
            'categorias': None,
            'catIds': None,
            'paises': None}

    #añade los videos a una singlelinked
    catalogo['videos'] = lt.newList('SINGLE_LINKED', cmpV_id)
    #map, llave = id video
    catalogo['videosIds'] = mp.newMap (375918, 
                                        maptype='CHAINING',
                                        loadfactor=4.0,  )
    
    #map llave= canal que subio el video
    catalogo['canales'] = mp.newMap(375918, maptype='CHAINING',
                                    loadfactor=4.0,
                                    comparefunction=compararCanalPorNombre)
   


    #map llave es la categoria
    catalogo['categorias'] = mp.newMap(5638770,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction= compararCatNombre)

    #map llave = id de la categoria
    catalogo['catIds'] = mp.newMap(5638770,
                                  maptype='CHAINING',
                                  loadfactor=4.0,
                                  comparefunction=compararCatIds)
    
    #map llave= pais
    catalogo['paises'] = mp.newMap(10,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction = compararMapPais)
    
    
    
    
    return catalogo

# ==============================
# Funciones para creación de datos
# ==============================
def nuevoCanal(name):
    #se guarda en una lista los videos del canal
    canal = {'name': "",
             'videos': None}
    canal['name'] = name
    canal['videos'] = lt.newList('SINGLE_LINKED', compararCanalPorNombre)
    return canal


def nuevoCatVideo(name, id):
    #relación entre un tag y los videos con el tag
    #tiene un total de videos con ese tag
    #crea una lista con los libros

    cat = {'name': '',
           'tag_id': '',
           'total_videos': 0,
           'videos': None,
           'count': 0.0}
    cat['name'] = name
    cat['tag_id'] = id
    cat['books'] = lt.newList()
    return cat

def nuevoPais(name):
    #crea una lista con los videos por pais
    pais = {'name':'', 'videos':None}
    pais['name'] = name
    pais['videos'] =lt.newList()

# ==============================
# Funciones para agregar info al catalogo
# ==============================
def addV(catalog, video):
    #agrega un video a la lista de videos
    #también guarda el video en un map, usa el id para eso
    #se agrega en los canales una referencia al video
    #crea una entrada en el map de paises
    lt.addLast(catalog['videos'], video)
    mp.put(catalog['videosIds'], video['video_id'], video)
    canal = video['channel_title']

    addVideoCanal(catalog, canal, video)
    addVideoPais(catalog, video)


def addVideoPais(catalog, video):
    #agrega un pais a la lista de paises
    paises = catalog['paises']
    pais = video['country']
    if mp.contains(paises, pais):
        entry = mp.get(paises, pais)
        paisf = me.getValue(entry)
    else:
        paisf = nuevoPais(pais)
        mp.put(paises, pais, video)
    
        

def addVideoCanal(catalog, nomcanal, video):
    #agrega un video a la lista de un canal
    channel = catalog['canales']
    existcanal = mp.contains(channel, nomcanal )
    if existcanal:
        entry = mp.get(channel, nomcanal)
        canall = me.getValue(entry)
    else:
        canall = nuevoCanal(nomcanal)
        mp.put(channel, nomcanal, canall)
    
    lt.addLast(canall['videos'], video)


def addCat(catalog, categoria):
    #actualiza una categoria a la tabla de categorias de catlogo
    newCat = newCat(categoria['tag_name'], tag['tag_id'])
    mp.put(catalogo['categorias'], tag['tag_name'], newCat)
    mp.put (catalogo['cat_vid'],tag['tag_id'], newCat)

def addVideoCat(catalog, categoria):
    videoid = categoria['video_id']
    catid = tag['tag_id']
    entry = mg.get(catalog['catIds'], catid)
    if entry:
        tagvideo = mp.get(catalog['categorias'], me.getValue(entry)['name'])
        tagvideo['value']['total_books'] += 1
        tagvideo['value']['count'] += int(tag['count'])
        video = mp.get(catalog['videosIds'], videoid)
        if video:
            lt.addLast(tagvideo['value']['books'], video['value'])


# ==============================
# Funciones de consulta
# ==============================

def getVideosPorCanal(catalog, nomcanal):
    canal = mp.get(catalog['canales'], nomcanal)
    if canal:
        return me.getValue(canal)
    return None

def getVideosPorCat(catalog, nomcat):
    cat = mp.get(catalog['categorias'], nomcat)
    videos = None
    if cat:
        videos = me.getValue(cat)['videos']
    return books

def getVideosPorPais(catalog, pais):
    pais = mp.get(catalog['paises'], pais)
    if pais:
        return me.getValue(pais)['videos']
    return None

def videosSize(catalog):
    
    return lt.size(catalog['videos'])

def canalesSize(catalog):
    """
    Numero de autores en el catalogo
    """
    return mp.size(catalog['canales'])


def tagsSize(catalog):
    """
    Numero de tags en el catalogo
    """
    return mp.size(catalog['tags'])



# ==============================
# Funciones de Comparacion
# ==============================

def cmpV_id(ide_1, id_2):
    #compara ids de dos videos
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1    



def compararMapVideoIds( id, entrada):
    # compara ids de videos, id = indentificador, 
    #entrada = pareja llave-valor
    identry = me.getKey(entrada)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compararCanalPorNombre(keyname, canal):
    authentry = me.getKey(canal)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def compararCatNombre(name, categoria):
    
    tagentry = me.getKey(categoria)
    if (name == tagentry):
        return 0
    elif (name > tagentry):
        return 1
    else:
        return -1


def compararCatIds(id, categoria):
    tagentry = me.getKey(categoria)
    if (int(id) == int(tagentry)):
        return 0
    elif (int(id) > int(tagentry)):
        return 1
    else:
        return 0

def compararMapPais(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return 0

