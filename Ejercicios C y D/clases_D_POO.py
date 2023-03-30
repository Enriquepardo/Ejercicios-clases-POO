class logger:
    def __init__(self,archivo):
        self.archivo = archivo
        self.contador = 0
        with open (self.archivo, "w") as log:
            log.write("--Log start--: \n")
    def log(self, mensaje):#Metodo para escribir en el archivo
        with open (self.archivo, "a") as log:
            log.write(mensaje + "\n")
            self.contador += 1
    def __del__(self):#Destructor
        with open (self.archivo, "a") as log:
            log.write("--Log end--: \n")

class test(logger):
    def __init__(self):
        super().__init__("log.txt")
    def funcion_llamada(self,mensaje):
        self.log("mensaje")
    
Test=test()
for i in range(1,6):
    if i==1:
        Test.funcion_llamada("1ªllamada")
    if i>1:
        Test.funcion_llamada(str(i)+"ªllamada")
    else:
        pass
    

    

    

        
        

    


   