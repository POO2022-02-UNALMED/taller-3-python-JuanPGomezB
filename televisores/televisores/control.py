class Control:
    

    def enlazar(self,tv):    
        self.tv=tv 
        tv.control=self




    def turnOff(self):
        if self.tv.estado==True:
            self.estado=False

    def turnOn(self):
        if self.tv.estado==False:
            self.tv.estado=True

    def canalUp(self):
        if self.tv.estado==True:
            if self.tv.canal>=1 and self.tv.canal<120:
                self.tv.canal+=1

    def canalDown(self):
        if self.tv.estado==True:
            if self.canal>1 and self.tv.canal<=120:
                self.canal-=1

    def volumenUp(self):
        if self.tv.estado==True:
            if self.tv.volumen>=0 and self.tv.volumen<7:
                self.tv.volumen+=1

    def volumenDown(self):
        if self.tv.estado==True:
            if self.tv.volumen>0 and self.tv.volumen<=7:
                self.tv.volumen-=1

    def setCanal(self,canal):

        if canal>=1 and canal<=120 and self.tv.estado==True:
            self.tv.canal=canal 

    def getTv(self):
        return self.tv

    def setTv(self,tv):
        self.tv=tv    