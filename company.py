proveedores = ["Diego Diaz", "Laura Martinez", "David Alvarez"]
ciudad = ["Bogota", "Bucaramanga", "Cali"]
nArticulos = [120,350,58]
infoArticulos = ["ID 01, Iphone 12 Pro, 5000000 COP", "ID 02, Portatil Acer Aspire 3, 2000000 COP", "ID 03, Mouse Logitech G, 200000 COP"]

selector = (input("Ingrese el nombre del proveedor: "))
if selector in proveedores:
    busqueda = proveedores.index(selector)
    print(proveedores[busqueda] , "\nCiudad: ", ciudad[busqueda] , "\nNumero de articulos: ",nArticulos[busqueda] ,
    "\nInformacion de los articulos: ", infoArticulos[busqueda])

if selector == "":
    print("No se especifico un nombre")

else:
    print("El proveedor no esta dentro de la lista de proveedores")

selector2 = (input("Presione (y) si desea cambiar la ciudad de un proveedor o (Enter) para omitir: "))
if selector2 == "y":
    selector3 = (input("Ingrese el nombre del proveedor que se movera de ciudad: "))
    if selector3 in proveedores:
        busqueda2 = proveedores.index(selector3)
        newc = input("Ingrese la nueva ciudad: ")
        ciudad[busqueda2] = newc
        print("La lista de ciudades se ha actualizado: ", ciudad)
    else:
        print("El proveedor no esta dentro de la lista de proveedores")
else:
    print("El cambio de ciudad ha sido omitido")

selector4 = (input("Presione (s) si desea sumar articulos a la lista o (Enter) para omitir: "))
if selector4 == "s":
    selector5 = (input("Ingrese el nombre del proveedor al que se le agregaran articulos: "))
    if selector5 in proveedores:
        busqueda3 = proveedores.index(selector5)
        suma = int(input("Ingrese la cantidad de articulos a agregar: "))
        nArticulos[busqueda3] += suma
        print("La lista de articulos se ha actualizado: ", nArticulos)
    else:
        print("El proveedor no esta dentro de la lista de proveedores")
else:
    print("El cambio de articulos se ha sido omitido")

selector6 = (input("Presione (r) si desea eliminar articulos a la lista o (Enter) para omitir: "))
if selector6 == "r":
    selector7 = (input("Ingrese el nombre del proveedor al que se le eliminaran articulos: "))
    if selector7 in proveedores:
        busqueda4 = proveedores.index(selector7)
        resta = int(input("Ingrese la cantidad de articulos a eliminar: "))
        nArticulos[busqueda4] -= resta
        print("La lista de articulos se ha actualizado: ", nArticulos)
    else:
        print("El proveedor no esta dentro de la lista de proveedores")
else:
    print("El cambio de articulos se ha sido omitido")

selector8 = (input("Presione (a) si desea agregar un proveedor a la lista o (Enter) para omitir: "))
if selector8 == "a":
    newp = input("Ingrese el nombre del nuevo proveedor: ")
    proveedores.append(newp)
    print("La lista de proveedores se ha actualizado: ", proveedores)
else:
    print("El cambio de articulos se ha sido omitido")

selector9 = (input("Presione (e) si desea agregar un proveedor a la lista o (Enter) para omitir: "))
if selector9 == "e":
    eliminar = input("Ingrese el nombre del proveedor a eliminar: ")
    proveedores.remove(eliminar)
    print("La lista de proveedores se ha actualizado: ", proveedores)
else:
    print("El cambio de articulos se ha sido omitido")









