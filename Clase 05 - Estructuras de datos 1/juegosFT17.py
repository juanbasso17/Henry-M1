import random

class juegoPila(object):
    def __init__(self):
        self.__list = []
        # Rellenar la pila con números del 1 al 20
        while len(self.__list) < 20:
            numero = random.randint(1,20)
            if numero not in self.__list:
                self.__list.append(numero)
    
    # Quitar el ultimo elemento de la pila
    def __pop(self):
        return self.__list.pop()

    # Mostrar la pila
    def __mostrar(self):
        if len(self.__list) > 0:
            for item in self.__list:
                print(item)
        else:
            print('No hay elementos')

    def jugar(self):
        # Empieza el juego

        while True:
            nro = input('Ingrese la cantidad de elementos a sacar: ')   # Le pedimos al usuario que ingrese cantidad de elementos, type(str)

            if not nro.isdecimal():     # Devuelve True o False, si el str se puede convertir a int
                nro = input('Ingresar la cantidad de elementos en numerico(int): ')
            elif nro.isdecimal():
                nro = int(nro)
                break
        
        # Empiezal a acción!!!!
        print('Pila original: ')
        self.__mostrar()

        calificacion = 10                           # Para calcular la califiacion
        suma = 0                                    # Para sumar los elementos

        for i in range(nro):
            suma += self.__pop()
        
        print('Pila obtenida: ')
        self.__mostrar()

        print(f'Se suma la cantidad total de: {suma}')

        if suma > 50:                                           # Si la suma es mayor a 50, significa que el usuario perdio
            print('No cumpliste con el objetivo, perdiste D:')
        else:                                                   # Si no super la suma de 50, gano asi que debemos calcular la calificacion
            while suma <= 50:                                   # Mientras que la suma no supere los 50, se va a repetir este ciclo
                suma += self.__pop()                            # Quitamos un elemento y lo sumamos a lo que ya teniamos
                if suma <= 50:                                  # Si suma sigue sin llegar a 50:
                    calificacion -= 1                           # Calificacion va bajando en 1 por cada iteracion
            print(f'OBJETIVO CUMPLIDO!!!! FELICITACIONES :D TU PUNTAJE FUE DE: {calificacion}')

class Jarra():
    def __init__(self, cap):
        self.__elemento_agua = '*'
        self.__elemento_vacio = ' '
        self.__capacidad = cap
        self.__list = []
        i = 0
        while i < cap:
            self.__list.append(self.__elemento_vacio)
            i += 1
    
    def vaciar(self):
        i = 0
        while i < self.__capacidad:
            self.__list[i] = self.__elemento_vacio
            i += 1

    def llenar(self):
        i = 0
        while i < self.__capacidad:
            self.__list[i] = self.__elemento_agua
            i += 1
    
    def mostrar_jarra(self):
        print(f'Jarra de {self.__capacidad} litros')
        for elemento in self.__list:
            print('|',elemento,'|')
        print('-----')
    
    def cantidad_litros(self):
        cantidad = 0
        for elemento in self.__list:
            if elemento == self.__elemento_agua:
                cantidad += 1
        return cantidad
    

    def quitar_litros(self, litros):
        i = 0
        encontrado = False
        while (not encontrado): # encontrado = False
          
            if (self.__list[i] == self.__elemento_agua):
                encontrado = True
            i += 1
        
        i -= 1
        while (litros > 0):
            self.__list[i] = self.__elemento_vacio
            i += 1
            litros -= 1
    def agregar_litros(self, litros):
        i = 0
        while((i < self.__capacidad) and (self.__list[i] == self.__elemento_vacio)):
            i += 1
        while (litros > 0):
            i -= 1
            self.__list[i] = self.__elemento_agua
            litros -= 1


class JuegoJarra():
    def __init__(self):
        self.__j3L = Jarra(3)
        self.__j5L = Jarra(5)
        self.__opciones_validas = ['1','2','3','4','5','6','7']


    def jugar(self):
        nro = 0
        counter = 0

        while nro < 7:
            print('JUEGO DE LAS JARRAS !!!:')
            print('************************************')
            print('1- LLenar la jarra de 3L')
            print('2- Llenar la jarra de 5L')
            print('3- Vacia la jarra de 3L')
            print('4- Vaciar la jarra de 5L')
            print('5- Verter el contenido de la jarra de 3L en la de 5L')
            print('6- Verter el contenido de la jarra de 5L en la de 3L')
            print('7- SALIR')
            print('************************************')
            

            self.__j3L.mostrar_jarra()
            self.__j5L.mostrar_jarra()
            print('************************************')
            nro = input('Ingrese una opcion: ')                     # Se le pide al usuario que elija una opcion
            counter += 1                                            # Nuestro contador contabiliza la cantidad de jugadas
            if nro not in self.__opciones_validas:
                nro = 0
            else:
                nro = int(nro) 

            if nro == 1:
                self.__j3L.llenar()
            elif nro == 2:
                self.__j5L.llenar()
            elif nro == 3:
                self.__j3L.vaciar()
            elif nro == 4:
                self.__j5L.vaciar()
            elif nro == 5:
                jarra3L = self.__j3L.cantidad_litros()
                jarra5L = self.__j5L.cantidad_litros()
                disponible_5L = 5 - jarra5L

                if disponible_5L < jarra3L:
                    intercambio = disponible_5L
                else:
                    intercambio = jarra3L

                self.__j5L.agregar_litros(intercambio)
                self.__j3L.quitar_litros(intercambio)
            
            elif nro == 6:
                jarra3L = self.__j3L.cantidad_litros()
                jarra5L = self.__j5L.cantidad_litros()
                disponible_3L = 3 - jarra3L
                if disponible_3L < jarra5L:
                    intercambio = disponible_3L
                else:
                    intercambio = jarra5L
                
                self.__j3L.agregar_litros(intercambio)
                self.__j5L.quitar_litros(intercambio)
            
            if (self.__j5L.cantidad_litros() == 4):
                print(f'FELICIDADES !!! TU PUNTAJE ES DE: {100 - counter * 10}')
                print('*************************************')
                self.__j3L.mostrar_jarra()
                self.__j5L.mostrar_jarra()              # Aca tienen que haber 4 Lts (****)
                print('**************************')
                print('1- Jugar de nuevo')
                print('2- Terminar')
                nro = input('Ingrese una opcion: ')
                if nro not in self.__opciones_validas:
                    nro = 0
                else:
                    nro = int(nro)
                    if nro == 1:
                        self.__j3L.vaciar()
                        self.__j5L.vaciar()
                    elif nro == 2:
                        exit()
                    

if __name__ == '__main__':
    j = JuegoJarra()
    j.jugar()