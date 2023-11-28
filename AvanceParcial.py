class ProductoMusical:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} - Stock: {self.stock}"

productos_musicales = {
    1: ProductoMusical('guitarra', 299.99, 5),
    2: ProductoMusical('teclado', 199.5, 7),
    3: ProductoMusical('batería', 499.75, 2),
}

def mostrar_inventario():
    print("\nProductos Disponibles en LIMA MUSIC:")
    for key, producto in productos_musicales.items():
        print(f"{key}: {producto}")

def main():
    print("Bienvenido a LIMA MUSIC")
    carrito = []

    while True:
        mostrar_inventario()
        producto_seleccionado = int(input("Selecciona un producto musical por número (0 para salir): "))
        if producto_seleccionado == 0:
            break

        producto = productos_musicales.get(producto_seleccionado)
        if producto:
            cantidad = int(input(f"Ingrese la cantidad de {producto.nombre} que desea comprar: "))
            if 0 < cantidad <= producto.stock:
                carrito.append((producto, cantidad))
                producto.stock -= cantidad
                print(f"Se han agregado {cantidad} {producto.nombre}(s) al carrito.")
            else:
                print("Cantidad no válida o no hay suficiente stock.")
        else:
            print("Producto no encontrado en LIMA MUSIC.")
        
        seguir_comprando = input("¿Desea seguir comprando? (si/no): ").lower()
        if seguir_comprando != "si":
            break

    if carrito:
        print("\nRecibo de Compra:")
        total_compra = sum(producto.precio * cantidad for producto, cantidad in carrito)
        for producto, cantidad in carrito:
            print(f"{producto.nombre} - Cantidad: {cantidad} - Precio unitario: ${producto.precio:.2f} - Precio total: ${producto.precio * cantidad:.2f}")
        print(f"Total de la compra: ${total_compra:.2f}")
        print("¡Gracias por comprar en LIMA MUSIC!")

if __name__ == "__main__":
    main()
