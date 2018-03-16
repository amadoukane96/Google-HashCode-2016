class Satellite:
    
    def __init__ (self,latitude=None,longitude=None,velocity=None,w=None,d=None,id=None):
        self.latitude=latitude
        self.longitude=longitude
        self.velocity=velocity
        self.w=w # w representant la valeur max possible de deplacement du satellite sur chaqie axe
        self.d=d # d representant la distance de la cote du carre que vise le satellite
        self.id=id #id du satellite
        self.camera=Camera()# l'attribut camera un objet de type Camera

    def __str__(self):  
        return ("Satellite(latitude:{}, longitude:{}, v:{}, w:{}, id:{})".format(self.latitude,self.longitude,self.velocity,self.w,self.id))
    
    def __repr__(self):  
        return ("Satellite(latitude:{}, longitude:{}, v:{}, w:{}, id:{})".format(self.latitude,self.longitude,self.velocity,self.w,self.id))

    def checkPole(self):
        """renvoie true si le satellite est au dessus dun pole"""
        if abs(self.latitude)>=degreToArcsecond(85) and abs(self.latitude)<=degreToArcsecond(90):
            return True
        return False
        
    def update(self): #mise à jour du satellite
        """fonction de mise à jour de la position du satellite et de sa caméra"""
        if self.latitude+self.velocity>=-90*3600 and self.latitude+self.velocity<=90*3600:#lorsque le satellite est entre les deux poles
            self.latitude=self.latitude+self.velocity
            self.longitude=self.longitude-15
            self.velocity=self.velocity
        if self.latitude+self.velocity>90*3600:
            self.latitude=180*3600-(self.latitude+self.velocity)
            self.longitude=-180*3600+(self.longitude-15)
            self.velocity=-self.velocity
        
        if self.latitude+self.velocity<-90*3600:
            self.latitude=-180*3600-(self.latitude+self.velocity)
            self.longitude=-180*3600+(self.longitude-15)
            self.velocity=-self.velocity

        if self.longitude<-648000:
            self.longitude=self.longitude%648000
        if self.longitude>=647999:
            self.longitude=self.longitude%-648000
            
