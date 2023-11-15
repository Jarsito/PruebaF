class ProductoMusical:
    def __init__(self, nombre, marcas):
        self.nombre = nombre
        self.marcas = marcas

    def mostrar_marcas(self):
        for marca, precio in self.marcas.items():
            print(f"{marca}: ${precio:.2f}")

class CarritoItem:
    def __init__(self, producto, marca, cantidad):
        self.producto = producto
        self.marca = marca
        self.cantidad = cantidad

    def calcular_precio_total(self):
        return self.producto.marcas[self.marca] * self.cantidad

usuarios = {"usuario1": "contrasena1", "usuario2": "contrasena2"}

productos_musicales = {
    "guitarra": ProductoMusical('guitarra', {"Fender": 299.99, "Gibson": 399.99, "Ibanez": 249.99}),
    "teclado": ProductoMusical('teclado', {"Roland": 199.5, "Yamaha": 249.99, "Korg": 189.99}),
    "batería": ProductoMusical('batería', {"Pearl": 499.75, "DW": 699.99, "Mapex": 449.99}),
    "micrófono": ProductoMusical('micrófono', {"Shure": 79.99, "AKG": 89.99, "Sennheiser": 99.99}),
    "amplificador": ProductoMusical('amplificador', {"Marshall": 149.99, "Fender": 179.99, "Orange": 199.99}),
    "piano": ProductoMusical('piano', {"Steinway": 599.99, "Kawai": 799.99, "Casio": 499.99}),
    "violín": ProductoMusical('violín', {"Stradivarius": 199.0, "Yamaha": 249.99, "Stentor": 189.99}),
    "flauta": ProductoMusical('flauta', {"Yamaha": 99.5, "Pearl": 119.99, "Gemeinhardt": 89.99}),
}

def mostrar_inventario():
    print("\nProductos Disponibles en LIMA MUSIC:")
    for key, producto in productos_musicales.items():
        print(f"{key.capitalize()}:")
        producto.mostrar_marcas()

def iniciar_sesion():
    while True:
        opcion = input("¿Desea iniciar sesión (S) o crear un nuevo usuario (C)? ").lower()
        
        if opcion == "s":
            usuario = input("Ingrese su nombre de usuario: ")
            contrasena = input("Ingrese su contraseña: ")

            if usuarios.get(usuario) == contrasena:
                print(f"Bienvenido, {usuario}!")
                return True
            else:
                print("Nombre de usuario o contraseña incorrectos. Intente nuevamente.")
        elif opcion == "c":
            nuevo_usuario = input("Cree un nuevo nombre de usuario: ")
            nueva_contrasena = input("Cree una nueva contraseña: ")
            usuarios[nuevo_usuario] = nueva_contrasena
            print("Usuario creado exitosamente. Ahora puede iniciar sesión.")
        else:
            print("Opción no válida. Intente nuevamente.")

def main():
    print("Bienvenido a LIMA MUSIC")

    if not iniciar_sesion():
        return

    carrito = []

    while True:
        mostrar_inventario()
        producto_seleccionado = input("Seleccione un producto musical (o '0' para salir): ").lower()
        if producto_seleccionado == '0':
            break

        producto = productos_musicales.get(producto_seleccionado)
        if producto:
            print(f"Marcas disponibles para {producto.nombre.capitalize()}:")
            producto.mostrar_marcas()
            
            marca_seleccionada = input("Seleccione una marca: ").capitalize()
            
            if marca_seleccionada in producto.marcas:
                cantidad = int(input(f"Ingrese la cantidad de {marca_seleccionada} {producto.nombre} que desea comprar: "))
                if 0 < cantidad:
                    carrito_item = CarritoItem(producto, marca_seleccionada, cantidad)
                    carrito.append(carrito_item)
                    print(f"Se han agregado {cantidad} {marca_seleccionada} {producto.nombre}(s) al carrito.")
                else:
                    print("Cantidad no válida.")
            else:
                print(f"Marca no válida para {producto.nombre.capitalize()}.")
        else:
            print("Producto no encontrado en LIMA MUSIC.")
        
        seguir_comprando = input("¿Desea seguir comprando? (si/no): ").lower()
        if seguir_comprando != "si":
            break

    if carrito:
        print("\nRecibo de Compra:")
        total_compra = sum(item.calcular_precio_total() for item in carrito)
        for item in carrito:
            print(f"{item.producto.nombre.capitalize()} - Marca: {item.marca} - Cantidad: {item.cantidad} - Precio unitario: ${item.producto.marcas[item.marca]:.2f} - Precio total: ${item.calcular_precio_total():.2f}")
        print(f"Total de la compra: ${total_compra:.2f}")
        print("¡Gracias por comprar en LIMA MUSIC!")

if __name__ == "__main__":
    main()
