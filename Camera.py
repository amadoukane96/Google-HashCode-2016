    
class Camera:
    def __init__ (self):
        self.dLat=0 #position relatif au satellite de la camera selon la latitude
        self.dLon=0 #position relatif au satellite de la camera selon la longitude
        self.t=0 #le tour pendant lequel la dernière photo a été prise

    def __str__(self):  
        return ("camera pointe({})".format(self.camPosition(),self.t))

    def __repr__(self):  
        return ("camera pointe({})".format(self.camPosition(),self.t))

    def camPosition(self,sat):
        """renvoie la position(absolue) sur laquelle pointe la caméra. Prend en paramètre le satellite auquel elle est reliée."""
        return (sat.latitude+self.dLat,sat.latitude+self.dLat)

    def update(self,dLat,dLon,t):
        """mise à jour: ajoute(dLat,dLon)à la position relative de la camera et note t comme le dernier tour ou elle a bougé)"""
        self.deltaLatitude+=dLat
        self.deltaLongitude+=dLon
        self.t=t 
        
    def checkUpdate(self,dLat,dLon):
        """renvoie true si la camera peut parcourir dLat,dLon sans sortir du carré de côté 2D"""
        if (self.deltaLatitude+dLat)<=sat.d and (self.deltaLatitude+dLat)>=-sat.d and (self.deltaLongitude+dLon)<=sat.d and (self.deltaLongitude+dLon)>=-sat.d:#test pour la latitude test pour la longitude
            return True
        return False

    def checkDistance(self,sat,image,t):
        """verifie qu'en terme de distance l'image est atteignable par rapport au dernier tour ou la camera n'a pas bougé"""
        cameraLatitude,cameraLongitude=self.camPosition(sat)#position absolue de la camera
        T=sat.camera.t #le dernier tour auquel la camera a bougé
        if t==0:#au tour 0 on n'a qu'une option: bouger de w selon chaque axe
            if distAxe(cameraLatitude,image.latitude)<=sat.w and distAxe(cameraLongitude,image.longitude)<=sat.w: #si l'image est à w ou moins de la camera selon chaque axe, on renvoie True
                return True
            else:
                return False
        else:
            if distAxe(cameraLatitude,image.latitude)<=(t-T)*sat.w and distAxe(cameraLongitude,image.longitude)<=(t-T)*sat.w:#sinon on verfie qu'on aurait eu le temps d'arriver à l'image selon chaque axe
                return True
            else:
                return False
            
    def findMove(self,sat,image):
        """renvoie la distance algebrique pour la camera à parcourir selon chaque axe pour avoir la photo"""
        dLat,dLon=0,0#les distances à renvoyer
        lat,lon=self.camPosition(sat)#position absolue de la caméra
        if lat<=image.latitude:#si la camera est en dessous de l'image selon la latitude, alors elle parcourera une distance algébrique positive
            dLat=distAxe(lat,image.lat)
        else:
            dLat=-distAxe(lat,image.lat)#sinon une distance algébrique negative
            
        if lon<=image.longitude:#même travail sur la longitude
            dLon=distAxe(lon,image.lon)
        else:
            dLon=-distAxe(lon,image.lon)
        return dLat,dLon
            

    def checkPic(self,sat,image,listeCollection,t):
        """ test si la camera de sat peut prendre en photo image au tour t: reunie les fonctions de la caméra """
        
        #si le sat n'est pas au desus d'un pôle, qu'on est dans le bon intervalle de temps, que la distance est atteignable par la camera:
        if (sat.checkPole==False)and image.checkRange(listeCollec,t)and self.checkDistance(sat,image,t) :
            
            #on verifie que la camera ne sort pas du carré
            dLat,dLon=self.findMove(sat,image)#pour ca on cherche les deplacements algebrique que la camera aurait à faire

            if self.checkUpdate(dLat,dLon): #si parcourir dLat, et dLon ne fait pas sortir la caméra du carré de cote 2d
                self.update(dLat,dLon,t)#on met à jour la caméra(deplacement+numero tour pour la photo) et on renvoie vrai
                return True
        return False
            
