class Node:
  __slots__ = 'value', 'next', 'prev'

  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

  def __str__(self):
    return str(self.value)


class DoubleLinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def __iter__(self):
    curr_node = self.head
    while curr_node is not None:
      yield curr_node
      curr_node = curr_node.next

  def __str__(self):
    result = [str(x.prev) + '<--' + str(x.value)+ '-->'+ str(x.next) for x in self]
    return '  '.join(result)

  def append(self, value):
    new_node = Node(value)
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.length += 1

  def prepend(self, value):
    new_node = Node(value)
    if self.head == None:
       self.head = new_node
       self.tail = new_node
    else:
       new_node.next = self.head
       self.head.prev = new_node
       self.head = new_node
    self.length += 1

  def get(self, index):
    if index == -1 or index == self.length-1:
       return self.tail
    elif index < -1 or index >= self.length :
       return None

    indextemp = 0
    for cur_node in self:
      if indextemp == index:
        return cur_node
      indextemp += 1

  def insert(self, value, index):
    if index == 0:
      self.prepend(value)
      return True
    elif index == -1 or index == self.length-1:
      self.append(value)
      return True
    elif index < -1 or index > self.length-1:
      return False
    else:
      new_node = Node(value)
      prev_node = self.get(index-1)
      next_node = self.get(index)
      new_node.next = prev_node.next
      new_node.prev = prev_node
      prev_node.next = new_node
      next_node.prev = new_node
      self.length += 1
      return True

  def traverse(self):
    for cur_node in self:
      print(cur_node.value)

  def search(self, target):
    index = 0
    for cur_node in self:
      if cur_node.value == target:
        return index
      index += 1
    return -1

  def set(self, index, value):
    temp = self.get(index)
    if temp:
      temp.value = value
      return True
    return False

  def pop_first(self):
    if self.length == 0:
      return None
    popped_node = self.head
    if self.length == 1:
      self.head = self.tail = None
    else:
      self.head = self.head.next
      self.head.prev = None
      popped_node.next = None
    self.length -= 1
    return popped_node

  def pop(self):
    if self.length == 0:
      return None
    popped_node = self.tail
    if self.length == 1:
      self.head = self.tail = None
    else:
      prevtail_node = self.get(self.length-2)
      prevtail_node.next = None
      self.tail = prevtail_node
    self.length -= 1
    return popped_node

  def remove(self, index):
    if index < -1 and index >= self.length:
      return None
    if index == 0:
      return self.pop_first()
    if index == -1 or index == self.length -1:
      return self.pop()
    prev_node = self.get(index-1)
    next_node = self.get(index)
    popped_node = prev_node.next
    prev_node.next = popped_node.next
    next_node.prev = prev_node
    popped_node.next = None
    self.length -= 1
    return popped_node

  def delete_all(self):
    self.head = None
    self.tail = None
    self.length = 0



class Libro:
    def __init__(self, numero_libro, genero, autor, titulo, ano_publicacion, tarifa_diaria, alquilado=False):
        self.numero_libro = numero_libro
        self.genero = genero
        self.autor = autor
        self.titulo = titulo
        self.ano_publicacion = ano_publicacion
        self.tarifa_diaria = int(tarifa_diaria)
        self.alquilado = alquilado

    def __str__(self):
        estado_alquiler = "Alquilado" if self.alquilado else "Disponible"
        return f"Número de libro: {self.numero_libro}, Género: {self.genero}, Autor: {self.autor}, Título: {self.titulo}, Año de publicación: {self.ano_publicacion}, Tarifa diaria: {self.tarifa_diaria}, Estado: {estado_alquiler}"


def agregar_libro(lista_libros):
    numero_libro = input("Ingrese el número de libro (ID): ")
    genero = input("Ingrese el género del libro: ")
    autor = input("Ingrese el autor del libro: ")
    titulo = input("Ingrese el título del libro: ")
    ano_publicacion = input("Ingrese el año de publicación del libro: ")
    tarifa_diaria = input("Ingrese la tarifa diaria del libro para su alquiler: ")

    libro = Libro(numero_libro, genero, autor, titulo, ano_publicacion, tarifa_diaria)
    lista_libros.append(libro)
    print("El libro fue correctamente agregado")


def eliminar_libro(lista_libros):
    numero_libro = input("Ingrese el número (ID) del libro que va a eliminar: ")
    for i, libro in enumerate(lista_libros):
        if libro.numero_libro == numero_libro:
            lista_libros.remove(i)
            print("El libro fue eliminado")
            return
    print("El libro no se encontró")


def buscar_libros_por_genero(lista_libros):
    genero_libro = input("Ingrese el género de los libros que quiere buscar: ")
    libros_encontrados = [libro for libro in lista_libros if libro.genero == genero_libro]
    if libros_encontrados:
        print(f"Se encontraron {len(libros_encontrados)} libros del género '{genero_libro}':")
        for i in libros_encontrados:
            print(i)
    else:
        print(f"No se encontraron libros de '{genero_libro}'.")


def buscar_libro_por_titulo(lista_libros):
    titulo_libro = input("Ingrese el título del libro que quiere buscar: ")
    for i in lista_libros:
        if i.titulo == titulo_libro:
            estado = "disponible" if not i.alquilado else "no disponible"
            print(f"El libro '{titulo_libro}' está en la biblioteca y está {estado} para alquilarlo")
            return
    print(f"No se encontró el libro '{titulo_libro}' en la biblioteca")

def buscar_libro_por_autor(lista_libros):
    autor_del_libro = input("Ingrese el autor del libro que quiere buscar: ")
    for libro in lista_libros:
        if libro.autor == autor_del_libro:
            estado = "disponible" if not libro.alquilado else "no disponible"
            print(f"El libro del autor '{autor_del_libro}' está en la biblioteca y está {estado} para alquilarlo")
            return
    print(f"No se encontró ningún libro del autor '{autor_del_libro}' en la biblioteca")

def buscar_libro_por_ano(lista_libros):
    ano_del_libro = input("Ingrese el año de publicación del libro que quiere buscar: ")
    for libro in lista_libros:
        if libro.anio_publicacion == ano_del_libro:
            estado = "disponible" if not libro.alquilado else "no disponible"
            print(f"El libro publicado en el año '{ano_del_libro}' está en la biblioteca y está {estado} para alquilarlo")
            return
    print(f"No se encontró ningún libro publicado en el año '{ano_del_libro}' en la biblioteca")

def listar_libros_disponibles(lista_libros):
    libros_disponibles = [libro for libro in lista_libros if not libro.alquilado]
    if libros_disponibles:
        print("La lista de los libros disponibles para alquilarlos:")
        for libro in libros_disponibles:
            print(libro)
    else:
        print("No hay libros disponibles para alquilar")

def listar_libros_alquilados(lista_libros):
    libros_alquilados = [libro for libro in lista_libros if libro.alquilado]
    if libros_alquilados:
        print("Lista de libros alquilados:")
        for libro in libros_alquilados:
            print(libro)
    else:
        print("No hay libros alquilados en este momento")

def listar_libros_disponibles_por_genero(lista_libros):
    genero = input("Ingrese el género de los libros disponibles para alquilar: ")
    libros_disponibles = [libro for libro in lista_libros if libro.genero == genero and not libro.alquilado]
    if libros_disponibles:
        print(f"Lista de libros disponibles del género '{genero}' para alquilarlos es:")
        for i in libros_disponibles:
            print(i)
    else:
        print(f"No hay libros de '{genero}' disponibles para alquilar")

def listar_libros_alquilados_por_genero(lista_libros):
    genero = input("Ingrese el género de los libros alquilados: ")
    libros_alquilados = [libro for libro in lista_libros if libro.genero == genero and libro.alquilado]
    if libros_alquilados:
        print(f"Lista de libros alquilados de '{genero}':")
        for n in libros_alquilados:
            print(n)
    else:
        print(f"No hay libros de '{genero}' alquilados")

def alquilar_libro_por_genero(lista_libros):
    genero = input("Ingrese el género del libro que quiere alquilar: ")
    libros_disponibles = [libro for libro in lista_libros if libro.genero == genero and not libro.alquilado]
    if libros_disponibles:
        print(f"Lista de libros disponibles de '{genero}' para alquilarlos:")
        for i, libro in enumerate(libros_disponibles):
            print(f"{i + 1}. {libro}")
        opcion = int(input("Seleccione el número del libro que desea alquilar: "))
        if 1 <= opcion <= len(libros_disponibles):
            libro_seleccionado = libros_disponibles[opcion - 1]
            libro_seleccionado.alquilado = True
            print(f"Ha alquilado el libro '{libro_seleccionado.titulo}'")
        else:
            print("Opción inválida")
    else:
        print(f"No hay libros de '{genero}' disponibles para alquilar")

def alquilar_libro(lista_libros):
    titulo = input("Ingrese el título del libro que quiere alquilar: ")
    for j in lista_libros:
        if j.titulo == titulo and not j.alquilado:
            j.alquilado = True
            print(f"Ha alquilado el libro '{titulo}'")
            return
    print(f"No se encontró el libro '{titulo}' disponible")

def devolver_libro(lista_libros):
    titulo_libro = input("Ingrese el título del libro que quiere devolver: ")
    for i in lista_libros:
        if i.titulo == titulo_libro and i.alquilado:
            i.alquilado = False
            print(f"Ha devuelto el libro '{titulo_libro}'")
            return
    print(f"No se encontró el libro '{titulo_libro}' para devolver o ya ha sido devuelto")

def descuento_por_alquiler_multiple(lista_libros):
    
    libros_alquilados = [libro for libro in lista_libros if libro.alquilado]

    precio_libros = sum(libro.tarifa_diaria for libro in libros_alquilados)

    print(f"el descuento del 10% fue '{precio_libros * 0.1}' y el precio queda en '{precio_libros * 0.9}'")

def ingreso_total_alquileres(lista_libros):
    ingreso_total = sum(float(libro.tarifa_diaria) for libro in lista_libros if libro.alquilado)
    print(f"El ingreso obtenido por los alquileres es de: ${ingreso_total:.3f}")
    return ingreso_total

def intercambiar_libros_deteriorados(lista_libros):
    titulo_deteriorado = input("Ingrese el título del libro deteriorado: ")
    titulo_nuevo = input("Ingrese el título del libro nuevo para reemplazarlo: ")

    index_deteriorado = -1
    index_nuevo = -1
    for i, libro in enumerate(lista_libros):
        if libro.titulo == titulo_deteriorado:
            index_deteriorado = i
        elif libro.titulo == titulo_nuevo:
            index_nuevo = i

    if index_deteriorado == -1 or index_nuevo == -1:
        print("Uno o ambos libros no fueron encontrados en la biblioteca")
        return

    lista_libros[index_deteriorado], lista_libros[index_nuevo] = lista_libros[index_nuevo], lista_libros[index_deteriorado]
    print(f"Se intercambió el libro '{titulo_deteriorado}' por el libro '{titulo_nuevo}'")

lista_libros = []

while True:
    print("\n---- PRÁCTICA DE GESTIÓN DE ALQUILER DE LIBROS ----")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Buscar libros por género")
    print("4. Buscar un libro por título")
    print("5. Buscar un libro por autor")
    print("6. Buscar un libro por año de publicación")
    print("7. Listar libros disponibles para alquilar")
    print("8. Listar libros que se encuentran alquilados")
    print("9. Listar libros disponibles para alquilar por género")
    print("10. Listar libros que se encuentran alquilados por género")
    print("11. Alquilar un libro por género")
    print("12. Alquilar un libro")
    print("13. Devolver un libro")
    print("14. Descuento por alquiler múltiple")
    print("15. Ingreso total por alquileres")
    print("16. Intercambiar libros deteriorados")
    print("q. Salir del programa")

    opcion = input("Elija una opción: ")

    if opcion == '1':
        agregar_libro(lista_libros)
    elif opcion == '2':
        eliminar_libro(lista_libros)
    elif opcion == '3':
        buscar_libros_por_genero(lista_libros)
    elif opcion == '4':
        buscar_libro_por_titulo(lista_libros)
    elif opcion == '5':
        buscar_libro_por_autor(lista_libros)
    elif opcion == '6':
        buscar_libro_por_ano(lista_libros)
    elif opcion == '7':
        listar_libros_disponibles(lista_libros)
    elif opcion == '8':
        listar_libros_alquilados(lista_libros)
    elif opcion == '9':
        listar_libros_disponibles_por_genero(lista_libros)
    elif opcion == '10':
        listar_libros_alquilados_por_genero(lista_libros)
    elif opcion == '11':
        alquilar_libro_por_genero(lista_libros)
    elif opcion == '12':
        alquilar_libro(lista_libros)
    elif opcion == '13':
        devolver_libro(lista_libros)
    elif opcion == '14':
        descuento_por_alquiler_multiple(lista_libros)
    elif opcion == '15':
        ingreso_total_alquileres(lista_libros)
    elif opcion == '16':
        intercambiar_libros_deteriorados(lista_libros)
    elif opcion.lower() == 'q':
        print("PROGRAMA CERRADO")
        break
    else:
        print("Opción no válida. Seleccione una opción válida.")
