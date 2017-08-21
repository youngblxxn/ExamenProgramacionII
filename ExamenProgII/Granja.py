import Conejo
import Elefante
import Delfin

def ConstruirConejo(CantidadReproduccion,CantidadAnimales):
    conejo = Conejo.Conejo(CantidadReproduccion,CantidadAnimales)
    return Conejo

def ConstruirElefante(CantidadReproduccion,CantidadAnimales):
    elefante = Elefante.Elefante(CantidadReproduccion,CantidadAnimales)
    return Elefante

def ConstruirDelfin(CantidadReproduccion,CantidadAnimales):
    delfin = Delfin.Delfin(CantidadReproduccion,CantidadAnimales)
    return Delfin

def ImprimirMenu():
    print("1 Agregar Nuevo Animal\n2 Animales pregnados\n3 Alimentar Animales\n4Dar de beber")
    print("5 Salir")
    accion= int(input("Ingrese el numero de la accion que desea hacer "))
    return accion

def ImprimirAnimales():
    print("1 Conejos\n2 Elefante\n3 Delfin")
    accion = int(input("Ingrese el numero de la accion que desea hacer "))
    return accion

conejoconstruido=False
elefanteconstruido=False
delfinconstruido=False
salir=False

while not salir:
    accion = ImprimirMenu()
    if(accion==1):
        tipoanimal=ImprimirAnimales()
        if(tipoanimal==1):
            cantidadanimales=int(input("Ingrese la cantidad de conejos que tiene"))
            cantidadreproduccion=int(input("Ingrese la cantidad de animales por parto que puede tener un conejo"))
            conejoconstruido=ConstruirConejos(cantidadreproduccion,cantidadanimales)
        elif(tipoanimal==2):
            cantidadanimales=int(input("Ingrese la cantidad de elefantes que tiene"))
            cantidadreproduccion=int(input("Ingrese la cantidad de animales por parto que puede tener un elefante"))
            elefanteconstruido=ConstruirElefante(cantidadreproduccion,cantidadanimales)
        elif(tipoanimal==3):
            cantidadanimales=int(input("Ingrese la cantidad de delfines que tiene"))
            cantidadreproduccion=int(input("Ingrese la cantidad de animales por parto que puese tener un delfin"))
            delfinconstruido=ConstruirDelfin(cantidadreproduccion,cantidadanimales)
        else:
            print("El comando ingresado no se reconoce")
    elif(accion==2):
        tipoanimal=ImprimirAnimales()
        if(tipoanimal==1):
            if(conejoconstruido!=False):
                cantidadanimalespreniados = int(input("Ingrese la cantidad de animales pregnados"))
                conejoconstruido.Reproduccion(cantidadanimalespreniados)
            else:
                print("No tiene conejos en su granja")
        elif(tipoanimal==2):
            if(elefanteconstruido!=False):
                cantidadanimalespreniados = int(input("Ingrese la cantidad de animales pregnados"))
                elefanteconstruido.Reproduccion(cantidadanimalespreniados)
            else:
                print("No tiene elefantes en su granja")
        elif(tipoanimal==3):
            if(delfinconstruido!=False):
                cantidadanimalespreniados = int(input("Ingrese la cantidad de animales pregnados"))
                delfinconstruido.Reproduccion(cantidadanimalespreniados)
            else:
                print("No tiene delfines en su granja")
    elif(accion==3):
        tipoanimal=ImprimirAnimales()
        if(tipoanimal==1):
            if(conejoconstruido!=False):
                tipoalimento=input("Ingrese el tipo de alimento que da a los conejos")
                cantidadalimento =int(input("Ingrese la cantidad de alimento"))
                conejoconstruido.Alimentar(tipoalimento,cantidadalimento)
            else:
                print("No tiene conejos en su granja")
        elif(tipoanimal==2):
            if(elefanteconstruido!=False):
                tipoalimento=input("Ingrese el tipo de alimento que le da a los elefantes")
                cantidadalimento=int(input("Ingrese la cantidad de alimento"))
                elefanteconstruido.Alimentar(tipoalimento,cantidadalimento)
            else:
                print("No tiene elefantes en su granja")
        elif(tipoanimal==3):
            if(delfinconstruido!=False):
                tipoalimento=input("Ingrese el tipo de alimento que le da a los delfines")
                cantidadalimento=int(input("Ingrese la cantidad de alimento"))
                elefanteconstruido.Alimentar(tipoalimento,cantidadalimento)
            else:
                print("No tiene delfines en su granja")
        else:
            print("No se reconoce el comando ingresado")
    elif(accion==4):
        tipoanimal=ImprimirAnimales()
        if(tipoanimal==1):
            if(conejoconstruido!=False):
                print("No puede dar de beber a los conejos")
            else:
                print("No tiene conejos en su granja")
        elif(tipoanimal==2):
            if(elefanteconstruido!=False):
                cantidadagua=int(input("Ingrese la cantidad de agua para los elefantes"))
                elefanteconstruido.TomarAgua(cantidadagua)
            else:
                print("No tiene elefantes en su granja")
        elif(tipoanimal==3):
            if(delfinconstruido!=False):
                cantidadagua=int(input("Ingrese la cantidad de agua para los delfines"))
                delfinconstruido.TomarAgua(cantidadagua)
            else:
                print("No tiene delfines en su granja")
        else:
            print("Comando ingresado desconocido")
    elif(accion==5):
        salir=True
    else:
        print("El comando ingresado no se reconoce")
