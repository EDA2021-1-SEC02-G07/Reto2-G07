import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import map as mp
sys.setrecursionlimit(1000000)
class text:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    RED = '\033[91m'
    BLUE = '\033[34m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    END = '\033[0m'

def printMenu():
    print(text.CYAN + "\nBienvenido" + text.END)
    print(text.BLUE + "1- Cargar información en el catálogo.")
    print("2- Consultar los n videos con más views en tendencia por país.")
    print("3- Consultar el video que más días ha sido tendencia por país.")
    print("4- Consultar el video que más días ha sido tendencia por categoría.")
    print("5- Consultar los n videos con más likes con un tag específico.")
    print("0- Salir."+ text.END)

def iniciarC():
    return controller.iniciarC()

def loadData(catalog):
    controller.loadData(catalog)

def printTendPais(videos, n, pais):
    try:
        print('\nLos', str(n), 'videos con mas visitas de', str(pais).capitalize(), 'son: ')
        i = 1
        while i < (n + 1):
            video =  lt.getElement(videos, i)
            print(text.UNDERLINE + text.YELLOW + str(i) + '.',
            'Fecha en tendencia:' + text.END, video['trending_date'],
            text.YELLOW + text.UNDERLINE + 'Título:' + text.END, video['title'],
            text.YELLOW + text.UNDERLINE + 'Canal:' + text.END, video['channel_title'],
            text.YELLOW + text.UNDERLINE + 'Hora de publicación:' + text.END, video['publish_time'],
            text.YELLOW + text.UNDERLINE + 'Visitas:' + text.END, video['views'],
            text.YELLOW + text.UNDERLINE + 'Likes:' + text.END, video['likes'],
            text.YELLOW + text.UNDERLINE + 'Dislikes:' + text.END, video['dislikes'], '\n')
                
            i +=1
 
    except:
        print(text.BOLD, text.RED, text.UNDERLINE, 'SE HA PRODUCIDO UN ERROR',  text.END)


def printDiasPais(video, pais):
    print('El video con más días en tendencia en', pais.capitalize(), 'es: ')
    print(text.UNDERLINE + text.YELLOW +
            text.YELLOW + text.UNDERLINE + 'Título:' + text.END, video[0]['title'],
            text.YELLOW + text.UNDERLINE + 'Canal:' + text.END, video[0]['channel_title'],
            text.YELLOW + text.UNDERLINE + 'País:' + text.END, pais.capitalize(),
            text.YELLOW + text.UNDERLINE + 'Número de días en tendencia:' + text.END, video[1])

def printDiasCat(video, cat):
    pass

def printLikesTag(videos, tag):
    pass


#Menú principal
while True:
    printMenu()
    inputs = input(text.YELLOW + 'Seleccione una opción para continuar\n' + text.END)
    if int(inputs[0]) == 1:
        print(text.PURPLE + "Cargando información de los archivos...\n" + text.END)
        catalog = iniciarC()
        loadData(catalog)
        print(text.UNDERLINE + text.BOLD + 'Videos cargados:' + text.END + ' ',
        str(lt.size(catalog['videos'])))
        video = lt.getElement(catalog['videos'],1)
        print(text.UNDERLINE + text.BOLD + 'El primer elemento cargado es: '+ text.END + ' ')
        print('Titulo: ' + video['title'] + ', Canal: ' + video['channel_title'] + ', Trending date: ' + \
             video['trending_date'] + ', País :' + video['country'] + ', Vistas :'+ video['views'] +\
                  ', Likes :' + video['likes'] + ', Dislikes :' + video['dislikes'])
      
        
        print( text.UNDERLINE + text.BOLD + 'Categorías cargadas:' + text.END + ' '+  str(lt.size(catalog['categorias'])), '\n')
        #print(catalog['categorias']['elements'])
        


    elif int(inputs[0]) == 2:
        n = int(input('\n' + text.GREEN + "Escriba el número de los top videos que desea consultar: " + text.END))
        pais = input(text.GREEN + 'Escriba el país en el que desee consultar las tendencias: ' + text.END)
        cate = input(text.GREEN + 'Escriba el nombre de la categoría que desea consultar: ' + text.END)
        print(text.PURPLE, '\nCargando datos...\n', text.END)
        try:
            videos = controller.getTendPais(catalog, pais, cate)
            printTendPais(videos, n, pais)
        except:
            print(text.BOLD, text.RED, text.UNDERLINE, 'SE HA PRODUCIDO UN ERROR',  text.END)
        
    elif int(inputs[0]) == 3:
        p = input(text.GREEN + "\nEscriba el país que desea consultar: " + text.END)
        print(text.PURPLE, '\nCargando datos...\n', text.END)
        try: 
            video = controller.getDiasPais(catalog, p)
            printDiasPais(video, p)
        except:
            print(text.BOLD, text.RED, text.UNDERLINE, 'SE HA PRODUCIDO UN ERROR',  text.END)



        
    elif int(inputs[0]) == 4:
        c = input(text.GREEN + "\nEscriba la categoría que desea consultar: " + text.END)
        pos = mp.contains(catalog['categorias'], c)
        
        if pos != 0: 
            print(text.PURPLE, '\nCargando datos...\n', text.END)
            video = controller.getDiasCat(catalog, c)
            printDiasCat(video, c)
        else:
            print(text.RED, '\nLa categoría especificada no fue encontrada o no contiene videos.\n', text.END)
            sys.exit()

    elif int(inputs[0]) == 5:
        t = input(text.GREEN + "\nEscriba el tag que desea consultar: " + text.END)
        videos = controller.getLikesTag(catalog, t)
        printLikesTag(videos, t)

    elif int(inputs[0]) == 6:
        controller.getdebug(catalog)
    else:
        sys.exit(0)
sys.exit(0)
