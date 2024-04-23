list_viajeros = []
import os   
sw = True                 

def fnt_limpiar():
    os.system("cls")
    print('Autor: Nelsy Salas')
    print('Fecha: 2021-05-20')
    print('Copyrigth(c) 2024')
    print('Universidad Católica Luis Amigó\n')


def fnt_agente(op):
    global sw
    fnt_limpiar()
    if op == '1':
        print('<<< AGREGAR VIAJERO >>>')
        viajero = ''
        nombre = input('Nombre:  ')
        apellido = input('Apellido:  ')
        edad = input('Edad:  ')
        if (int(edad) > 0 and int(edad) <=25):    
            viajero = nombre + ' ' + apellido + ' ' + edad
            list_viajeros.append(viajero)
            print('\nViajero agregado correctamente\n')
            input('Presione <ENTER>  para continuar...')
        else:
            print('Edad no valida\n')
            input('Presione <ENTER>  para continuar...')
    elif op == '2':
        fnt_limpiar()
        print('<<< MOSTRAR VIAJEROS >>>')
        if len(list_viajeros) == 0:
            print('\nNo hay viajeros registros')
            input('Presione <ENTER>  para continuar...')
        else:
            for i in list_viajeros:
                print(i)
            input('Presione <ENTER>  para continuar...')
    elif op == '3':
        sw == False


while sw == True:
    opcion = input('<<<MENU PRINCIPAL >>>\n1 AGREGAR\n2. MOSTRAR\n3. SALIR\n4. ->')
    fnt_agente(opcion)