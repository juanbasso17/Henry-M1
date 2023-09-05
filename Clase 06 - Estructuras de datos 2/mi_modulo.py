class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, val):
        self.data = val

    def setNext(self, val):
        self.next = val

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        """Check if the list is empty"""
        if (self.head == None):
            return True
        else:
            return False

    def add(self, item):
        """Add the item to the list"""
        new_node = Node(item)
        new_node.setNext(self.head)
        self.head = new_node

    def size(self):
        """Return the length/size of the list"""
        count = 0
        current = self.head
        while (not(current == None)):
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        """Search for item in list. If found, return True. If not found, return False"""
        current = self.head
        found = False
        while ((current != None) and (not found)):
            if current.getData() is item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        """Remove item from list. If item is not found in list, raise ValueError"""
        current = self.head
        previous = None
        found = False
        while((current != None) and (not found)):
            if(current.getData() == item):
                found = True
            else:
                previous = current
                current = current.getNext()
        if found:
            if(previous == None):
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        else:
            raise ValueError
            print('Value not found.')

    def insert(self, position, item):
        """
        Insert item at position specified. If position specified is
        out of bounds, raise IndexError
        """
        if position > self.size() - 1:
            raise IndexError
            print('Index out of bounds.')
        current = self.head
        previous = None
        pos = 0
        if position == 0:
            self.add(item)
        else:
            new_node = Node(item)
            while pos < position:
                pos += 1
                previous = current
                current = current.getNext()
            previous.setNext(new_node)
            new_node.setNext(current)

    def index(self, item):
        """
        Return the index where item is found.
        If item is not found, return None.
        """
        current = self.head
        pos = 0
        found = False
        while ((current != None) and (not found)):
            if (current.getData() == item):
                found = True
            else:
                current = current.getNext()
                pos += 1
        if found:
            pass
        else:
            pos = None
        return pos

    def pop(self, position = None):
        """
        If no argument is provided, return and remove the item at the head. 
        If position is provided, return and remove the item at that position.
        If index is out of bounds, raise IndexError
        """
        current = self.head
        if (position == None):
            ret = current.getData()
            self.head = current.getNext()
        else:
            if position > self.size():
                print('Index out of bounds')
                raise IndexError
            pos = 0
            previous = None
            while pos < position:
                previous = current
                current = current.getNext()
                pos += 1
                ret = current.getData()
            previous.setNext(current.getNext())
        return ret

    def append(self, item):
        """Append item to the end of the list"""
        current = self.head
        previous = None
        pos = 0
        length = self.size()
        while pos < length:
            previous = current
            current = current.getNext()
            pos += 1
        new_node = Node(item)
        if (previous == None):
            new_node.setNext(current)
            self.head = new_node
        else:
            previous.setNext(new_node)

    def printList(self):
        """Print the list"""
        current = self.head
        while (not(current == None)):
            print(current.getData())
            current = current.getNext()

class Estructura_pila(object):
    def __init__(self):
        self.__list = []

    # Agregar un elemento
    def push(self, item):
        self.__list.append(item)
    
    # Quitar un elemento de la pila
    def pop(self):
        return self.__list.pop()
    
    # Obtener el elemento superior de la pila
    def peek(self):
        if self.__list:
            return self.__list[-1]                  # Devuelve el ultimo de la pila
        else:
            return None
    
    # Preguntar si la lista esta vacia
    def is_empty(self):
        if self.__list == []:
            return True
        else:
            return False
    
    # Numero de elementos de la pila
    def size(self):
        return len(self.__list)

class Estructura_cola(object):
    def __init__(self):
        self.__list = []

    # Agregar un elemento
    def enqueue(self, item):
        self.__list.append(item)

    # Quitar un elemento 
    def dequeue(self):
        return self.__list.pop(0)

    # Obtener el proximo elemento a eliminar
    def first(self):
        if self.__list != []:
            return self.__list[0]
        else:
            return None

    # Verificar si esta vacia
    def is_empty(self):
        return self.__list == []

    # Devolver la cantidad de elementos
    def size(self):
        return len(self.__list)