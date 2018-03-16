from Satellite import *
from Collection_et_Image import *
from Camera import *
from earth import *
from input_output import *
from math import *


def mainLoop():
    """
boucle principale du projet
    """
    
    fichier=input("quel fichier pour la simulation; attention extension= .in \n")

    #récuperation des données
    t,listSat,listCollec=input1(fichier) #on recupere t, une liste de satellite et une liste de collection
    
    #Division de la terre en petit rectangles
    pas=Dmax(listSat) #on recupere le pas pour diviser la terre
    
    world=divideEarth(pas)#on cree la liste des listes representant  la terre
    images=dividePic(listCollec,world,pas)#on y ajoute les images dans les listes correspondantes
    picTaken=[]#liste pour les photos quon va prendre
    
    #boucle principale

    for i in range(t):
        tour=i
        for sat in listSat: #pour chaque satelitte
            o,j=findArea(images,sat,pas)#on cherche les indices du carré dans lequel se trouve le sat
            for image in images[o][j]: #on cherche une image dans le carré du sat
                test=sat.camera.checkPic(sat,image,listCollec,tour)
                if test:
                    image.setIdSatT(sat.id,z)#on indique quel satelitte a pris la photo et à quel tour
                    picTaken.append(image)#on ajoute à la liste des images prises
                    break #un sat ne peut pas prendre 2 photos pendant le même tour
            sat.update()#mises à jour position du sat pour prochain tour
    print(len(picTaken))
    output("output.out",picTaken)#on ecrit le fichier de sortie

    return(0)
