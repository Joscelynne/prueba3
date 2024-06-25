import csv 

Lista_personas=[]
lista_datos_personas=[]
Lista_cargo_mesero=[]
lista_cargo_cocinero=[]
Lista_cargo_cajero=[]
datos_cargados=[]
descuento_salud=0.07
descuento_afp=1.0
nombre=""
apellido=""
cargo=""
cargo_validados=""
sueldo=0
sueldo_liquido=0
todos_los_trabajadores=[]
cargo_validado=""
opc=0

 #operacion con salud y afp


#guardoinformacion en lista ddatos de personas, y esa lista estara en una lista de personas, validar la opcion de 
#si es Mesero, Cocinero, Cajero (1.2.3)
#si la opc esuno se va a guardar en 

def Guardar_datos_csv(Lista_personas):
    archivo_datos="archivo.csv"
    with open(archivo_datos, "w", newline="") as archivo:
        escritor=csv.writer(archivo)
        escritor.writerow(["nombre", "apellido", "sueldo", "cargo"])
        escritor.writerows(Lista_personas)

def Cargar_archivos_csv():
    try:
        archivo_datos="archivo.csv"
        with open(archivo_datos, "r", newline="") as archivo:
            lector=csv.reader(archivo)
            for i in lector:
                datos_cargados.append(i)
        global Lista_personas
        Lista_personas=datos_cargados
    except:
        print(":)")

def menu():
    print('''
          bienvenido a restaurante.
          1. registrar trabajador
          2. enlistar trabajador
          3. imprimir sueldos por cargo
          4. salir del programa 
          
        '''  )
    
def validacion_cargo(cargo,Lista_personas):
    if cargo==1:
        print("Cargo: mesero")
        cargo_validado="mesero"
        
        Lista_cargo_mesero.append(Lista_personas)
        print(Lista_cargo_mesero)

      
        todos_los_trabajadores.append(Lista_cargo_mesero)
        print("se a guardado perfectamente")

    elif cargo==2:
        print("cargo: cocinero")
        cargo_validado="cocinero"

        lista_cargo_cocinero.append(lista_cargo_cocinero)

        todos_los_trabajadores.append(Lista_personas)
        print("se a guardado perfectamente")


    elif cargo==3:
        print("cargo: cajero")
        Lista_cargo_cajero.append(Lista_personas)
        cargo_validado="cajero"

        todos_los_trabajadores.append(Lista_cargo_cajero)
        print("se a guardado perfectamente")
        
def Sueldos_finales(sueldo):
    sueldo=sueldo*descuento_salud
    sueldo=sueldo*descuento_afp
    
def actualizar_trabajador(lista_datos_personas):
    for i in lista_datos_personas:
        i[2]=sueldo
        i[3]=cargo
    
    
def Crear_Trabajador(nombre, apellido, sueldo):
    lista_datos_personas=[nombre, apellido, sueldo]
    Lista_personas.append(lista_datos_personas)


def enlistar_trabajadores(todos_los_trabajadores):
    for i in todos_los_trabajadores:
        print(i)


Cargar_archivos_csv()
while True:
    menu()
    opc=input("Ingrese opcion que desee: ")

    if opc.isnumeric():
        opc=int(opc)
    else:
        print("Debe ser numero:)")

    if opc==1:
        print("Registrar trabajador")
        nombre=input("Ingrese nombre del trabajador: ")
        apellido=input("ingrese apellido del trabajador: ")
        while True:
            sueldo=input("Ingrese sueldo (numeros)")
            if sueldo.isnumeric():
                sueldo=float(sueldo)
                Sueldos_finales(sueldo)
                break
            else:
                print("solo numeros")
        while True:
            cargo=input('''
                        Ingrese cargo:
                        1. mesero
                        2. cocinero
                        3. cajero
                        ''' )
            if cargo.isnumeric():
                Crear_Trabajador(nombre,apellido,sueldo)
                cargo=int(cargo)
                validacion_cargo(cargo,Lista_personas)
                Sueldos_finales(sueldo)
                actualizar_trabajador(lista_datos_personas)

                Guardar_datos_csv(Lista_personas)
                break
            else: 
                print("el cargo debe ser numero")
    if opc==2:
        enlistar_trabajadores(todos_los_trabajadores)
    if opc==3:
        while True:
            cargo=input('''
                        Ingrese cargo:
                        1. mesero
                        2. cocinero
                        3. cajero
                        ''' )
            if cargo.isnumeric():
                cargo=int(cargo)
                if cargo==1:
                    print("meseros:")
                    for i in Lista_cargo_mesero:
                        print(i)
                    break
                elif cargo==2:
                    print("cocinero")

                    for i in lista_cargo_cocinero:
                        print (i)
                    break
                elif opc==3:
                    print("cajeros")
                    for i in Lista_cargo_cajero:
                       print(i)
                    break

        
            
    if opc==4:
        print("salir")
                
                    


