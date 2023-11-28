class ProductoMusical:
    def __init__(self, nombre, marcas_precios_stock):
        self.nombre = nombre
        self.marcas_precios_stock = marcas_precios_stock

    def log(self):
        print(f"{self.nombre.capitalize()}:")
        for marca, precio, stock in self.marcas_precios_stock:
            print(f"  - Marca: {marca.capitalize()} - Precio: ${precio:.2f} - Stock: {stock}")

# Definir instrumentos y marcas con arrays
INSTRUMENTOS = ['GUITARRA', 'TECLADO', 'BATERIA', 'MICROFONO', 'AMPLIFICADOR', 'PIANO', 'VIOLIN', 'FLAUTA']

MARCAS = {
    'GUITARRA': {'fender': 1200, 'gibson': 1500, 'ibanez': 1000},
    'TECLADO': {'roland': 1000, 'yamaha': 1200, 'korg': 900},
    'BATERIA': {'pearl': 1800, 'sabian': 1600, 'stagg': 1400},
    'MICROFONO': {'shure': 150, 'akg': 120, 'sennheiser': 180},
    'AMPLIFICADOR': {'marshall': 700, 'orange': 750, 'fender': 650},
    'PIANO': {'steinway': 3000, 'kawai': 2800, 'casio': 2500},
    'VIOLIN': {'stentor': 400, 'yamaha': 380, 'ibanez': 350},
    'FLAUTA': {'yamaha': 200, 'pearl': 180, 'gemeinhardt': 220},
}

PRODUCTOS = {
    instrumento: ProductoMusical(instrumento, [(marca, precio, 10) for marca, precio in MARCAS[instrumento].items()])
    for instrumento in INSTRUMENTOS
}

class CarritoItem:
    def __init__(self, producto, marca, cantidad):
        self.producto = producto
        self.marca = marca
        self.cantidad = cantidad

    def calcular_precio_total(self):
        return self.producto.marcas_precios_stock[self.marca][1] * self.cantidad

# Base de datos de usuarios
usuarios = {"usuario1": "contrasena1", "usuario2": "contrasena2"}

def mostrar_inventario():
    print("\nProductos Disponibles en LIMA MUSIC:")
    for producto in PRODUCTOS.values():
        producto.log()

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

    # Verificar la sesión del usuario
    if not iniciar_sesion():
        return

    carrito = []

    while True:
        mostrar_inventario()
        producto_seleccionado = input("Seleccione un producto musical (o '0' para salir): ").upper()
        if producto_seleccionado == '0':
            break

        producto = PRODUCTOS.get(producto_seleccionado)
        if producto:
            producto.log()
            
            marcas_disponibles = producto.marcas_precios_stock.keys()
            print("Marcas Disponibles:", marcas_disponibles)

            marca_seleccionada = input("Seleccione una marca: ").lower()

            if marca_seleccionada in marcas_disponibles:
                cantidad = int(input(f"Ingrese la cantidad de {marca_seleccionada} {producto_seleccionado} que desea comprar: "))
                stock = producto.marcas_precios_stock[marca_seleccionada][2]

                if 0 < cantidad <= stock:
                    carrito.append(CarritoItem(producto, marca_seleccionada, cantidad))
                    producto.marcas_precios_stock[marca_seleccionada] = (
                        producto.marcas_precios_stock[marca_seleccionada][0],
                        producto.marcas_precios_stock[marca_seleccionada][1],
                        stock - cantidad
                    )
                    print(f"Se han agregado {cantidad} {marca_seleccionada} {producto_seleccionado}(s) al carrito.")
                else:
                    print("Cantidad no válida o no hay suficiente stock.")
            else:
                print(f"Marca no válida para {producto_seleccionado.capitalize()}.")
        else:
            print("Producto no encontrado en LIMA MUSIC.")
        
        seguir_comprando = input("¿Desea seguir comprando? (si/no): ").lower()
        if seguir_comprando != "si":
            break

    if carrito:
        print("\nRecibo de Compra:")
        total_por_marca = {}
        for item in carrito:
            precio_total = item.calcular_precio_total()
            if item.marca not in total_por_marca:
                total_por_marca[item.marca] = precio_total
            else:
                total_por_marca[item.marca] += precio_total
            print(f"{item.producto.nombre.capitalize()} - Marca: {item.marca.capitalize()} - Cantidad: {item.cantidad} - Precio total: ${precio_total:.2f}")

        total_compra = sum(total_por_marca.values())
        print("\nTotal de la compra por marca:")
        for marca, total in total_por_marca.items():
            print(f"Marca: {marca.capitalize()} - Total: ${total:.2f}")

        print(f"\nTotal de la compra: ${total_compra:.2f}")
        print("¡Gracias por comprar en LIMA MUSIC!")

if __name__ == "__main__":
    main()
