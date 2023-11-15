class ProductoMusical:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Crear objetos de productos musicales
guitarra = ProductoMusical("guitarra", 299.99)
teclado = ProductoMusical("teclado", 199.50)
bateria = ProductoMusical("batería", 499.75)
microfono = ProductoMusical("micrófono", 79.99)
amplificador = ProductoMusical("amplificador", 149.95)

# Lista que contiene los objetos de productos musicales
productos_musicales = [guitarra, teclado, bateria, microfono, amplificador]

# Bienvenido a la tienda musical
print("Bienvenido a la Tienda Musical")
print("Productos Disponibles")

# Mostrar productos y precios usando bucle for
for producto in productos_musicales:
    print(f"- {producto.nombre}: ${producto.precio:.2f}")

producto_seleccionado = input("Selecciona un producto musical: ")

# Verificar si el producto seleccionado existe en la lista de objetos
producto_encontrado = next((producto for producto in productos_musicales if producto.nombre == producto_seleccionado), None)

if producto_encontrado:
    cantidad = int(input(f"Ingrese la cantidad de {producto_encontrado.nombre} que desea comprar: "))
    if cantidad > 0:
        precio_total = producto_encontrado.precio * cantidad
        print(f"El precio total de {cantidad} {producto_encontrado.nombre}(s) es: ${precio_total:.2f}")
    else:
        print("La cantidad debe ser mayor que cero")
else:
    print("Producto no encontrado en la tienda musical")
