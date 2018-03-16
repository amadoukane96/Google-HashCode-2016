
class Collection:
    def __init__(self,val=None):
        self.val=val
        self.listeImages=[] #Liste des images a photographier pour cette collection
        self.plagePossible=[]#Les plages de tours pendant lesquelles nous sommes autorisés à prendre des photod
      
    def __repr__(self):
        return ("Collection(val {})".format(self.val))
    
    def __str__(self):
        return ("Collection(val {})".format(self.val)	)
    
    def ajoutImage(self,Image):
        """ajoute Image à la liste d'images de la collection"""
        self.listeImages.append(Image) #Image de type Image
        
    def ajoutPlage(self,x):
        """ajoute une plage de tours: x est un tuple(debut,fin)"""
        self.plagePossible.append(x)
        
 	    
 	    
#Classe representant une image	
class Image:    
    def __init__(self,latitude=None,longitude=None,IdCollec=None,idsat=None,t=None):
    	self.longitude=longitude    
    	self.latitude=latitude
    	self.idSat=idsat #id du sat qui a pris la photo #Utile pour savoir si une photo a ete prise
    	self.t=t #tour pdt lequel la photo a été prise
    	self.idCollec=IdCollec #l'indice de la collection a laquelle l'image appartient 	

    def __str__(self):
        return "Image(latitude:{}, longitude{}, idsat{})".format(self.latitude,self.longitude,self.idSat)
    
    def __repr__(self):
        return "Image(latitude:{}, longitude{}, idsat{})".format(self.latitude,self.longitude,self.idSat)
    
    def setIdSatT(self,idsat,t):
        """ indique quel satellite a pris l'image en photo et à quel tour"""
        self.idSat=idsat
        self.t=t
        
    def checkRange(self,listeCollec,t):
        """ verifie qu'on peut prendre une photo à t. idCollec correspond a l'indice de la collection à laquelle appartient l'imag"""
        for i in listeCollec[self.idCollec].plagePossible:
            start,end=i
            if t>=start and t<=end:
                return True
        return False       
