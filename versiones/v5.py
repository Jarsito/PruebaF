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

# Bienvenido a la tienda musical
print("Bienvenido a la Tienda Musical")
print("Productos Disponibles")

# Mostrar productos y precios
for key, producto in productos_musicales.items():
    print(f"{key}: {producto}")

producto_seleccionado = int(input("Selecciona un producto musical por número: "))

# Verificar si el producto seleccionado existe en el diccionario
if producto_seleccionado in productos_musicales:
    producto = productos_musicales[producto_seleccionado]
    cantidad = int(input(f"Ingrese la cantidad de {producto.nombre} que desea comprar: "))
    
    if cantidad > 0 and cantidad <= producto.stock:
        precio_total = producto.precio * cantidad
        print(f"El precio total de {cantidad} {producto.nombre}(s) es: ${precio_total:.2f}")
        producto.stock -= cantidad  # Actualizar el stock
    elif cantidad <= 0:
        print("La cantidad debe ser mayor que cero")
    else:
        print("No hay suficiente stock para la cantidad solicitada.")
else:
    print("Producto no encontrado en la tienda musical")