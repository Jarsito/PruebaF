# Listas que contienen los productos y sus precios
productos_musicales = ["guitarra", "teclado", "batería", "micrófono", "amplificador"]
precios_musicales = [299.99, 199.50, 499.75, 79.99, 149.95]

# Bienvenido a la tienda musical
print("Bienvenido a la Tienda Musical")
print("Productos Disponibles")

# Mostrar productos y precios usando bucle for
for i in range(len(productos_musicales)):
    print(f"- {productos_musicales[i]}: ${precios_musicales[i]:.2f}")

producto_seleccionado = input("Selecciona un producto musical: ")

# Verificar si el producto seleccionado existe en la lista
if producto_seleccionado in productos_musicales:
    cantidad = int(input(f"Ingrese la cantidad de {producto_seleccionado} que desea comprar: "))
    if cantidad > 0:
        indice_producto = productos_musicales.index(producto_seleccionado)
        precio_unitario = precios_musicales[indice_producto]
        precio_total = precio_unitario * cantidad
        print(f"El precio total de {cantidad} {producto_seleccionado}(s) es: ${precio_total:.2f}")
    else:
        print("La cantidad debe ser mayor que cero")
else:
    print("Producto no encontrado en la tienda musical")
