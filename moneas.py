class country:
    def __init__(self,name,currency,code):
        self.name = name
        self.currency = currency
        self.code = code
    
    def show(self):
        print("El País es:",self.name)
        print("La moneda del país es: ",self.currency)
        print("El código de la moneda es: ",self.code)
    
    def update_currency(self,choice,country):
        country = ""
        if choice == 1 and country == self.name:
            self.currency = input("Ingrese la nueva moneda: ")
            self.code = input("Ingrese el nuevo código: ")
            print("Se actualizó la moneda")
        else:
            print("No se actualizó la moneda")
        