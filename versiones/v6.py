class ProductoMusical:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} - Stock: {self.stock}"

# Crear objetos de productos musicales usando un diccionario
productos_musicales = {
    1: ProductoMusical('guitarra', 299.99, 5),
    2: ProductoMusical('teclado', 199.5, 7),
    3: ProductoMusical('batería', 499.75, 2),
}

def mostrar_inventario():
    print("\nProductos Disponibles:")
    for key, producto in productos_musicales.items():
        print(f"{key}: {producto}")

def main():
    print("Bienvenido a la Tienda Musical")
    carrito = []
    continuar_comprando = True

    while continuar_comprando:
        mostrar_inventario()
        producto_seleccionado = int(input("Selecciona un producto musical por número: "))

        if producto_seleccionado in productos_musicales:
            producto = productos_musicales[producto_seleccionado]
            cantidad = int(input(f"Ingrese la cantidad de {producto.nombre} que desea comprar: "))

            if cantidad > 0 and cantidad <= producto.stock:
                precio_total = producto.precio * cantidad
                carrito.append((producto, cantidad))
                producto.stock -= cantidad
                print(f"Se han agregado {cantidad} {producto.nombre}(s) al carrito.")
            elif cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
            else:
                print("No hay suficiente stock para la cantidad solicitada.")
        else:
            print("Producto no encontrado en la tienda musical.")

        respuesta = input("¿Desea continuar comprando? (si/no): ")
        continuar_comprando = respuesta.lower() == "si"

    # Mostrar el recibo
    if carrito:
        print("\nRecibo:")
        total_compra = 0
        for producto, cantidad in carrito:
            precio_total = producto.precio * cantidad
            total_compra += precio_total
            print(f"{producto.nombre} - Cantidad: {cantidad} - Precio unitario: ${producto.precio:.2f} - Precio total: ${precio_total:.2f}")
        print(f"Total de la compra: ${total_compra:.2f}")
    else:
        print("No se ha realizado ninguna compra.")

if __name__ == "__main__":
    main()