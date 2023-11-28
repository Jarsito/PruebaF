class ProductoMusical {
    constructor(nombre, precio, stock, marca){
        this.nombre = nombre;
        this.precio = precio;
        this.stock = stock;
        this.marca = marca;
    }

    log() {
       console.log(`${nombre}- ${precio}- ${stock}- ${marca}`); 
    }
}
const PRODUCTOS ={
    GUITARRA: 'guitarra',
    TECLADO: 'teclado',
    BATERIA: 'bateria',
    MICROFONO: 'microfono',
    AMPLIFICADOR:'amplificador',
    PIANO: 'piano',
    VIOLIN: 'violin',
    FLAUTA: 'flauta',
}

const MARCAS={
    GIBSON: 'gibson',
    FENDER: 'fender',
    IBANEZ: 'ibanez',
    ROLAND: 'roland',
}

const productos_musicales ={
    1: ProductoMusical(PRODUCTOS.GUITARRA, 1000, 10, MARCAS.FENDER),
    2: ProductoMusical(PRODUCTOS.GUITARRA, 1000, 10, MARCAS.GIBSON),
    3: ProductoMusical(PRODUCTOS.GUITARRA, 1000, 10, MARCAS.IBANEZ),
}