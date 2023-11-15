# Diccionario que contiene los productos musicales y sus precios
productos_musicales = {
    "guitarra": 299.99,
    "teclado": 199.50,
    "batería": 499.75,
    "micrófono": 79.99,
    "amplificador": 149.95
}

# Bienvenido a la tienda musical
print("Bienvenido a la Tienda Musical")
print("Productos Disponibles")
print("- Guitarra: $299.99")
print("- Teclado: $199.50")
print("- Batería: $499.75")
print("- Micrófono: $79.99")
print("- Amplificador: $149.95")

producto_seleccionado = input("Selecciona un producto musical: ")

# Verificar si el producto seleccionado existe en el diccionario
if producto_seleccionado in productos_musicales:
    cantidad = int(input(f"Ingrese la cantidad de {producto_seleccionado} que desea comprar: "))
    if cantidad > 0:
        precio_unitario = productos_musicales[producto_seleccionado]
        precio_total = precio_unitario * cantidad
        print(f"El precio total de {cantidad} {producto_seleccionado}(s) es: ${precio_total:.2f}")
    else:
        print("La cantidad debe ser mayor que cero")
else:
    print("Producto no encontrado en la tienda musical")
