
def degreToArcsecond(x):
    return(3600*x)

def distAxe(a,b):
    """ renvoie la distance entre 2 abscisses ou 2 ordonnées"""
    return(max(a,b)-min(a,b))

def Dmax(listSat):
    """renvoie le plus grand champs de vision des satellites: dmax"""
    pas=0
    for sat in listSat:
        if sat.d>=pas:
            pas=sat.d
    return pas

def divideEarth(pas,l=[],g=[]):
    """
Permet de diviser la terre en un grand carré,contenant plusieurs petits carrés: renvoie une liste de sous listes representant la terre
    """
    i=0
    nbCarreLigne=(degreToArcsecond(180)*2)/pas #le nombre de carres par ligne=nb de sous liste par ligne 
    nbLigne=(degreToArcsecond(90)*2)/pas #le nombre de ligne representant la terre
    while i<nbLigne+1:#on cree ainsi une liste dont chaque sous liste represente un rectangle
        j=0
        l.append([])
        while j<nbCarreLigne+1:
            l[i].append(g)
            j+=1
        i+=1
    #on renvoie la liste
    return l
     

def dividePic(listCollec,liste,pas):
    """ajoute toutes les images des collections dans les bons rectangles
    renvoie liste complétée"""

    a=False
    for collection in listCollec:#on parcourt les collections
        for image in collection.listeImages:
            i,j=findArea(liste,image,pas)#recherche du rectangle correspondant à la position de l'image
            for jumeau in liste[i][j]:#on teste si on a pas deja la photo dans le carré
                if jumeau.latitude==image.latitude and jumeau.longitude==image.longitude:
                    a=True
                    break
            if a==False: #si la photo n'y est pas
                liste[i][j]=liste[i][j]+[image]#ajout de l'image
    return liste



def findArea(liste,objet,pas):
    """liste est la liste des rectangles.
    renvoie les indices de liste correspondant à la position de objet(image ou sat)"""
    
    #calcul des indices de la liste
    numRow=floor(distAxe(objet.latitude,degreToArcsecond(90))/pas)
    numCol=floor(distAxe(objet.longitude,degreToArcsecond(-180))/pas)
    
    #on renvoie les indices de la liste
    return (numRow,numCol)
