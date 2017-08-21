import Animales

class Delfin(Animales.Animal):
    def TomarAgua(self,cantidadagua):
        self.cantidadagua+=cantidadagua
        print("El delfin tiene {0} litros de agua".format(self.cantidadagua))

    def Alimentar(self,cantidadalimento):
        if(tipoalimento.lower()=="atun"):
            self.cantidadalimento+=cantidadalimento
        else:
            print("Solo me alimento de atun")
