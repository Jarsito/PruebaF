import os
from colorama import Fore, Back, Style, init

# Inicializar colorama
init(autoreset=True)

class ProductoMusical:
    def __init__(self, nombre, marcas_precios_stock):
        self.nombre = nombre
        self.marcas_precios_stock = marcas_precios_stock

    def mostrar_inventario(self):
        print(f"\n{'='*60}")
        print(f"{Fore.CYAN}{self.nombre.capitalize()} - Productos Disponibles en LIMA MUSIC:{Style.RESET_ALL}")
        print(f"{'='*60}")
        print("{:<20} {:<20} {:<15} {:<15}".format("Marca", "Precio (USD)", "Stock", "Total"))
        print("-" * 60)
        for marca, (precio, stock) in self.marcas_precios_stock.items():
            print("{:<20} {:<20.2f} {:<15} {:<15.2f}".format(marca.capitalize(), precio, stock, precio * stock))
        print("="*60)

class CarritoItem:
    def __init__(self, producto, marca, cantidad):
        self.producto = producto
        self.marca = marca
        self.cantidad = cantidad

    def calcular_precio_total(self):
        return self.producto.marcas_precios_stock[self.marca][0] * self.cantidad

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Base de datos de productos
PRODUCTOS = {
    'GUITARRA': ProductoMusical('GUITARRA', {'fender': (1200, 10), 'gibson': (1500, 10), 'ibanez': (1000, 10)}),
    'TECLADO': ProductoMusical('TECLADO', {'roland': (1000, 10), 'yamaha': (1200, 10), 'korg': (900, 10)}),
    'BATERIA': ProductoMusical('BATERIA', {'pearl': (1800, 10), 'sabian': (1600, 10), 'stagg': (1400, 10)}),
    'MICROFONO': ProductoMusical('MICROFONO', {'shure': (150, 10), 'akg': (120, 10), 'sennheiser': (180, 10)}),
    'AMPLIFICADOR': ProductoMusical('AMPLIFICADOR', {'marshall': (700, 10), 'orange': (750, 10), 'fender': (650, 10)}),
    'PIANO': ProductoMusical('PIANO', {'steinway': (3000, 10), 'kawai': (2800, 10), 'casio': (2500, 10)}),
    'VIOLIN': ProductoMusical('VIOLIN', {'stentor': (400, 10), 'yamaha': (380, 10), 'ibanez': (350, 10)}),
    'FLAUTA': ProductoMusical('FLAUTA', {'yamaha': (200, 10), 'pearl': (180, 10), 'gemeinhardt': (220, 10)}),
}

def iniciar_sesion(usuarios):
    while True:
        opcion = input("¿Desea iniciar sesión (S) o crear un nuevo usuario (C)? ").lower()

        if opcion == "s":
            usuario = input("Ingrese su nombre de usuario: ")
            contrasena = input("Ingrese su contraseña: ")

            if usuarios.get(usuario) == contrasena:
                print(f"Bienvenido, {Fore.GREEN}{usuario}!{Style.RESET_ALL}")
                return True
            else:
                print(f"{Fore.RED}Nombre de usuario o contraseña incorrectos. Intente nuevamente.{Style.RESET_ALL}")
        elif opcion == "c":
            nuevo_usuario = input("Cree un nuevo nombre de usuario: ")
            nueva_contrasena = input("Cree una nueva contraseña: ")
            usuarios[nuevo_usuario] = nueva_contrasena
            print(f"{Fore.GREEN}Usuario creado exitosamente. Ahora puede iniciar sesión.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Opción no válida. Intente nuevamente.{Style.RESET_ALL}")

def mostrar_marcas(producto):
    # Limpiar la consola antes de mostrar las marcas
    clear_console()

    producto.mostrar_inventario()

    marcas_disponibles = list(producto.marcas_precios_stock.keys())
    print(f"{Fore.CYAN}Marcas Disponibles:{Style.RESET_ALL}", ', '.join(marcas_disponibles))

    marca_seleccionada = input(f"{Fore.YELLOW}Seleccione una marca:{Style.RESET_ALL} ").lower()

    return marca_seleccionada

def imprimir_linea_separadora():
    print("=" * 60)

def main():
    print(f"{Fore.MAGENTA}Bienvenido a LIMA MUSIC{Style.RESET_ALL}")

    # Base de datos de usuarios
    usuarios = {"usuario1": "contrasena1", "usuario2": "contrasena2"}

    # Verificar la sesión del usuario
    if not iniciar_sesion(usuarios):
        return

    carrito = []

    while True:
        # Limpiar la consola al seleccionar un producto
        clear_console()

        for producto in PRODUCTOS.values():
            producto.mostrar_inventario()

        producto_seleccionado = input(f"{Fore.YELLOW}Seleccione un producto musical (o '0' para salir):{Style.RESET_ALL} ").upper()
        if producto_seleccionado == '0':
            break

        producto = PRODUCTOS.get(producto_seleccionado)
        if producto:
            # Mostrar marcas después de seleccionar un producto
            marca_seleccionada = mostrar_marcas(producto)

            if marca_seleccionada in producto.marcas_precios_stock:
                cantidad = int(input(f"{Fore.YELLOW}Ingrese la cantidad de {marca_seleccionada} {producto_seleccionado} que desea comprar:{Style.RESET_ALL} "))
                precio, stock = producto.marcas_precios_stock[marca_seleccionada]
                if 0 < cantidad <= stock:
                    carrito.append(CarritoItem(producto, marca_seleccionada, cantidad))
                    producto.marcas_precios_stock[marca_seleccionada] = (precio, stock - cantidad)
                    print(f"{Fore.GREEN}Se han agregado {cantidad} {marca_seleccionada} {producto_seleccionado}(s) al carrito.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Cantidad no válida o no hay suficiente stock.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Marca no válida para {producto_seleccionado.capitalize()}.{Style.RESET_ALL}")

            input(f"{Fore.YELLOW}Presione Enter para continuar...{Style.RESET_ALL}")  # Esperar a que el usuario presione Enter

        else:
            print(f"{Fore.RED}Producto no encontrado en LIMA MUSIC.{Style.RESET_ALL}")

        seguir_comprando = input(f"{Fore.YELLOW}¿Desea seguir comprando? (si/no):{Style.RESET_ALL} ").lower()
        if seguir_comprando != "si":
            break

    if carrito:
        # Limpiar la consola antes de imprimir la boleta de compras
        clear_console()

        print(f"\n{Fore.MAGENTA}Recibo de Compra:{Style.RESET_ALL}")
        imprimir_linea_separadora()
        for item in carrito:
            precio_total = item.calcular_precio_total()
            print(f"{item.producto.nombre.capitalize()} - Marca: {item.marca.capitalize()} - Cantidad: {item.cantidad} - Precio total: ${precio_total:.2f}")

        total_por_marca = {}
        for item in carrito:
            precio_total = item.calcular_precio_total()
            total_por_marca[item.marca] = total_por_marca.get(item.marca, 0) + precio_total

        total_compra = sum(total_por_marca.values())

        imprimir_linea_separadora()
        print(f"\n{Fore.MAGENTA}Total de la compra por marca:{Style.RESET_ALL}")
        for marca, total in total_por_marca.items():
            print(f"{Fore.CYAN}Marca:{Style.RESET_ALL} {marca.capitalize()} - {Fore.CYAN}Total:{Style.RESET_ALL} ${total:.2f}")

        imprimir_linea_separadora()
        print(f"\n{Fore.MAGENTA}Total de la compra:{Style.RESET_ALL} ${total_compra:.2f}")
        imprimir_linea_separadora()
        print(f"{Fore.GREEN}¡Gracias por comprar en LIMA MUSIC!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
