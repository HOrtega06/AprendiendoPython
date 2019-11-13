import json
class Bicicletas():
    def __init__(self,Color):
       self.Altura=90
       self.Largo=150
       self.Llantas=2
       self.Color=Color
       self.Avanza=False

    def Avanzar(self):
        self.Avanza=True

     def Informe(self):
         print("La bicicleta tiene ",self.Altura,"cm de altura y",self.Largo,",cm de largo,","y tiene", 
               self.Llantas, "llantas.")

bicicleta1=Bicicletas("Negro")
bicicleta2=Bicicletas("Amarillo")
bicicleta3=Bicicletas("Azul")

lista_bici=(bicicleta1,bicicleta2,bicicleta3)
print(lista_bici)

json=json.dumps(lista_bici,default=lambda o: o.__dict__, indent=5)
print(json)

print(isinstance(bicicleta1, Bicicletas))




























