class ProductoMusical:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

# Crear objetos de productos musicales usando el diccionario
productos_musicales = {
    1: ProductoMusical('guitarra', 299.99, 5),
    2: ProductoMusical('teclado', 199.5, 7),
    3: ProductoMusical('bateria', 499.75, 2),
}

# Bienvenido a la tienda musical
print("Bienvenido a la Tienda Musical")
print("Productos Disponibles")

# Mostrar productos y precios usando bucle for
for key, producto in productos_musicales.items():
    print(f"{key}: {producto.nombre} - ${producto.precio:.2f} - Stock: {producto.stock}")

producto_seleccionado = int(input("Selecciona un producto musical por número: "))

# Verificar si el producto seleccionado existe en el diccionario
if producto_seleccionado in productos_musicales:
    cantidad = int(input(f"Ingrese la cantidad de {productos_musicales[producto_seleccionado].nombre} que desea comprar: "))
    if cantidad > 0 and cantidad <= productos_musicales[producto_seleccionado].stock:
        precio_unitario = productos_musicales[producto_seleccionado].precio
        precio_total = precio_unitario * cantidad
        print(f"El precio total de {cantidad} {productos_musicales[producto_seleccionado].nombre}(s) es: ${precio_total:.2f}")
    elif cantidad <= 0:
        print("La cantidad debe ser mayor que cero")
    else:
        print("No hay suficiente stock para la cantidad solicitada.")
else:
    print("Producto no encontrado en la tienda musical")
