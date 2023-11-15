class ProductoMusical:
    def __init__(self, nombre, precio, stock, marcas):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.marcas = marcas

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} - Stock: {self.stock} - Marcas: {', '.join(self.marcas)}"

usuarios = {"usuario1": "contrasena1", "usuario2": "contrasena2"}

productos_musicales = {
    1: ProductoMusical('guitarra', 299.99, 5, ["Fender", "Gibson", "Ibanez"]),
    2: ProductoMusical('teclado', 199.5, 7, ["Roland", "Yamaha", "Korg"]),
    3: ProductoMusical('batería', 499.75, 2, ["Pearl", "DW", "Mapex"]),
    4: ProductoMusical('micrófono', 79.99, 10, ["Shure", "AKG", "Sennheiser"]),
    5: ProductoMusical('amplificador', 149.99, 4, ["Marshall", "Fender", "Orange"]),
    6: ProductoMusical('piano', 599.99, 3, ["Steinway", "Kawai", "Casio"]),
    7: ProductoMusical('violín', 199.0, 6, ["Stradivarius", "Yamaha", "Stentor"]),
    8: ProductoMusical('flauta', 99.5, 8, ["Yamaha", "Pearl", "Gemeinhardt"]),
}

def mostrar_inventario():
    print("\nProductos Disponibles en LIMA MUSIC:")
    for key, producto in productos_musicales.items():
        marcas = ', '.join(producto.marcas)
        print(f"{key}: {producto.nombre} - Marcas: {marcas}")

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
        producto_seleccionado = int(input("Selecciona un producto musical por número (0 para salir): "))
        if producto_seleccionado == 0:
            break

        producto = productos_musicales.get(producto_seleccionado)
        if producto:
            print(f"Marcas disponibles para {producto.nombre}: {', '.join(producto.marcas)}")
            marca_seleccionada = input("Selecciona una marca: ")
            
            if marca_seleccionada in producto.marcas:
                cantidad = int(input(f"Ingrese la cantidad de {marca_seleccionada} {producto.nombre} que desea comprar: "))
                if 0 < cantidad <= producto.stock:
                    carrito.append((producto, marca_seleccionada, cantidad))
                    producto.stock -= cantidad
                    print(f"Se han agregado {cantidad} {marca_seleccionada} {producto.nombre}(s) al carrito.")
                else:
                    print("Cantidad no válida o no hay suficiente stock.")
            else:
                print(f"Marca no válida para {producto.nombre}.")
        else:
            print("Producto no encontrado en LIMA MUSIC.")
        
        seguir_comprando = input("¿Desea seguir comprando? (si/no): ").lower()
        if seguir_comprando != "si":
            break

    if carrito:
        print("\nRecibo de Compra:")
        total_compra = sum(producto.precio * cantidad for producto, _, cantidad in carrito)
        for producto, marca, cantidad in carrito:
            print(f"{producto.nombre} - Marca: {marca} - Cantidad: {cantidad} - Precio unitario: ${producto.precio:.2f} - Precio total: ${producto.precio * cantidad:.2f}")
        print(f"Total de la compra: ${total_compra:.2f}")
        print("¡Gracias por comprar en LIMA MUSIC!")

if __name__ == "__main__":
    main()
