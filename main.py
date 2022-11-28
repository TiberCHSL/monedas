from moneas import country
#Hacer menú y más weas
def main():
    country5 = []
    i = 1
    while i < 6:
        country5.append(country(input(f"Ingrese nombre del país {i}: "),input("Ingrese la moneda: "),input("Ingrese el código de la moneda: ")))
        country5[i].show()
        i+=1
    country5[i].update_currency(int(input("Ingrese 1 si desea cambiar la moneda de algún país: "),input("Ingrese el nombre del País a cambiar: ")))

main()