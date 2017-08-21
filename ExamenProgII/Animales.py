import datetime
class Animal:
    def __init__(self,reproduccion,cantidadanimales):
        self.Animales =reproduccion
        self.cantidadanimales = cantidadanimales
        self.nacimiento = []
        self.fechanacimiento = []
        self.tipoalimento=""
        self.cantidadalimento=0
        self.cantidadagua=0

    def __Nacimiento(self, hembrasprenadas):
        nacidos = (self.AnimalesReproduccion*hembrasprenadas)
        self.cantidadanimales+=nacidos
        self.fechanacimiento.append(datetime.today())
        self.nacimiento.append(nacidos)
        print("La cantidad de animales nacidos es {0} ahora tiene {1} animales".format(nacidos,self.CantidadAnimales))

    def reproduccion(self,cantidadanimales):
        if(self.CantidadAnimales>=cantidadanimales):
            self.__Nacimiento(cantidadanimales)
        else:
            print("La cantiadad animales en reproduccion no puede ser mayor a la cantidad de animales existentes")

    def Decesos(self, cantidaddecesos):
        self.CantidadAnimales-=cantidaddecesos
        print("La cantidad actual de animales es {0}".format(self.Cantidadanimales))

    def ImprimirTodo(self):
        rango = len(self.nacimiento)
        print("Cantidad\tfecha de nacimiento")
        if(rango>0):
            for elemento in range(rango):
                print("{0}\t\t{1}".format(self.nacimiento[elemento],self.fechanacimiento[elemento]))
        elif(rango==0):
            print("{0}\t\t{1}".format(self.nacimiento[0],self.fechanacimiento[0]))
        else:
            print("No existen partos recientes")
