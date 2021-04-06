import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
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
    #print("2- Consultar los n videos con más views en tendencia por país.")
    #print("3- Consultar el video que más días ha sido tendencia por país.")
    #print("4- Consultar el video que más días ha sido tendencia por categoría.")
    print("5- Consultar los n videos con más likes con un tag específico.")
    print("0- Salir."+ text.END)

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
    if lt.size(videos) != 0:
        if lt.size(videos) >= n:
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
        else:
            print('\n', text.RED, 'Solo hay', str(n), 'videos que cumplen con los criterios de búsqueda: ',
            text.END)
            i = 1
            while i < (lt.size(videos) + 1):
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
    else:
        print('\n', text.RED, 'No hay videos que cumplan con los criterios de búsqueda.\n', text.END)
        sys.exit()

def printDiasPais(video, pais):
    print('\nEl video con más días en tendencia en el país', pais, 'es: ')
    print(text.YELLOW + text.UNDERLINE + 'Título:' + text.END, video['title'],
    text.YELLOW + text.UNDERLINE + 'Canal:' + text.END, video['channel_title'],
    text.YELLOW + text.UNDERLINE + 'Categoría:' + text.END, video['category_id'],
    text.YELLOW + text.UNDERLINE + 'Número de días en tendencia:' + text.END, video[1], '\n')

def printDiasCat(video, cat):
    print('\nEl video con más días en tendencia en la categoría', cat, 'es: ')
    print(text.YELLOW + text.UNDERLINE + 'Título:' + text.END, video[0]['title'],
    text.YELLOW + text.UNDERLINE + 'Canal:' + text.END, video[0]['channel_title'],
    text.YELLOW + text.UNDERLINE + 'Categoría:' + text.END, video[0]['category_id'],
    text.YELLOW + text.UNDERLINE + 'Número de días en tendencia:' + text.END, video[1], '\n')

def printLikesTag(videos, tag):
    n = 3
    if lt.size(videos) != 0:
        if lt.size(videos) >= n:
            print('\nLos', str(n), 'videos con más likes con el tag', tag, 'son: ')
            i = 1
            while i < (n + 1):
                video = lt.getElement(videos, i)
                print(text.YELLOW + text.UNDERLINE + 'Título:' + text.END, video['title'],
                text.YELLOW + text.UNDERLINE + 'Canal:' + text.END, video['channel_title'],
                text.YELLOW + text.UNDERLINE + 'Hora de publicación:' + text.END, video['publish_time'],
                text.YELLOW + text.UNDERLINE + 'Visitas:' + text.END, video['views'],
                text.YELLOW + text.UNDERLINE + 'Likes:' + text.END, video['likes'],
                text.YELLOW + text.UNDERLINE + 'Dislikes:' + text.END, video['dislikes'],
                text.YELLOW + text.UNDERLINE + 'Tags:' + text.END, video['tags'],video['video_id'], '\n')

                i +=1
        else:
            print(text.RED, '\nSolo hay', str(n), 'videos que cumplen con los criterios de búsqueda: ', text.END)
            i = 1
            while i < (lt.size(videos) + 1):
                video = lt.getElement(videos, i)
                print(text.YELLOW + text.UNDERLINE + 'Título:' + text.END, video['title'],
                text.YELLOW + text.UNDERLINE + 'Canal:' + text.END, video['channel_title'],
                text.YELLOW + text.UNDERLINE + 'Hora de publicación:' + text.END, video['publish_time'],
                text.YELLOW + text.UNDERLINE + 'Visitas:' + text.END, video['views'],
                text.YELLOW + text.UNDERLINE + 'Likes:' + text.END, video['likes'],
                text.YELLOW + text.UNDERLINE + 'Dislikes:' + text.END, video['dislikes'],
                text.YELLOW + text.UNDERLINE + 'Tags:' + text.END, video['tags'],video['video_id'], '\n')

                i +=1
    else:
        print(text.RED, '\nNo hay videos que cumplan con los criterios de búsqueda.\n', text.END)
        sys.exit()
catalog = None

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
        print(catalog['categorias']['elements'])

    elif int(inputs[0]) == 2:
        n = int(input('\n' + text.GREEN + "Escriba el número de los top videos que desea consultar: " + text.END))
        if lt.size(catalog['videos']) >= n:
            pais = input(text.GREEN + 'Escriba el país en el que desee consultar las tendencias: ' + text.END)
            if lt.isPresent(catalog['paises'], pais) != 0:
                cate = input(text.GREEN + 'Escriba el nombre de la categoría que desea consultar: ' + text.END)
                if lt.isPresent(catalog['categorias'], cate) != 0:
                    print(text.PURPLE, '\nCargando datos...\n', text.END)
                    videos = controller.getTendPais(catalog, pais, cate)
                    printTendPais(videos, n, pais)
                else:
                    print(text.RED, '\nCategoría no encontrada.\n', text.END)
                    sys.exit()
            else:
                print(text.RED, '\nPaís no encontrado.\n', text.END)
                sys.exit()

        else: 
            print(text.RED, '\nNúmero de tendencias excedido.\n', text.END)
            sys.exit()
        
    elif int(inputs[0]) == 3:
        p = input(text.GREEN + "\nEscriba el país que desea consultar: " + text.END)
        if lt.isPresent(catalog['paises'], p) != 0:
            print(text.PURPLE, '\nCargando datos...\n', text.END)
            video = controller.getDiasPais(catalog, p)
            printDiasPais(video, p)
        else:
            print(text.RED, '\nEl país no fue encontrado o no contiene videos.\n', text.END)
            sys.exit()
        
    elif int(inputs[0]) == 4:
        c = input(text.GREEN + "\nEscriba la categoría que desea consultar: " + text.END)
        pos = lt.isPresent(catalog['categorias'], c)
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
