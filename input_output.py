def input1(fichier,t=0,listeSat=[],listeCollection=[]):
    
    """fonction de recupération des données d'entrées. renvoie la durée de simulation
    une liste de sat et de collection"""
    file = open(fichier, "r")
    t=int(file.readline()) # t est la duree de simulation
       

#traitement satellites
    nombreSat=int(file.readline())
    for i in range (nombreSat):
        infosat=file.readline()
        infosat=infosat.split(' ')#recuperation données
        sat=Satellite(int(infosat[0]),int(infosat[1]),int(infosat[2]),int(infosat[3]),int(infosat[4]),i) #creation objet satellite
        listeSat.append(sat)#ajoute sat à la liste des sat
                  
#traitement Collections
    nbCollections=int(file.readline())  #recuperation donnée
    
      
    for i in range(0,nbCollections):
        numCollec=i
        infoCollec=file.readline()#recuperation données
        
        infoCollec=infoCollec.split(' ')
        nbPlages=int(infoCollec[2])
        nbPic=int(infoCollec[1])#nb de lieu à photographier pour cette collection
        x=Collection(int(infoCollec[0])) #création objet collection
        
            
#traitement Images
        for i in range (0,nbPic):
            infoImage=file.readline()#recuperation données
            infoImage=infoImage.split(' ')
            y=Image(int(infoImage[0]),int(infoImage[1]),numCollec)
            #création objet Image
            x.ajoutImage(y) #ajout Image à la liste des images à photographier
        for i in range(0,nbPlages):   
            plage=file.readline()#recuperation des plages de temps autorisées
            plage=plage.split(' ')
            x.ajoutPlage((int(plage[0]),int(plage[1])))#ajout des plages à la liste
            listeCollection.append(x) #ajout  collection à la liste des collections
    file.close()
    return(t,listeSat, listeCollection)
######################################"

def output(fichier,liste):
    """
liste contient les photos prises.
fonction d'écriture des resultats dans fichier
    """
    file=open(fichier,"w")
    file.write(str(len(liste)))#on ecrit le nombre de photo prises en premier
    file.close()
    for image in liste:#pour chaque image on ecrit les infos
        file=open(fichier,"a")
        file.write("\n")
        file.write(str(image.latitude))
        file.write(" ")
        file.write(str(image.longitude))
        file.write(" ")
        file.write(str(image.t))
        file.write(" ")
        file.write(str(image.idSat))
    file.close()
    
    return 0

    
