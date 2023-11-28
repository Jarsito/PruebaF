const productosMusicales={
    1:{
        name: 'guitarra',
        price: 299.99,
        stock:5,
    },
    2:{
        name: 'teclado',
        price: 199.5,
        stock:7,
    },
    3:{
        name: 'bateria',
        price: 499.75,
        stock:2,
    },
};
for(const[key, value] of Object.entries(productosMusicales)) {
    console.log(`${key}: ${value.name} - ${value.price} - ${value.stock}`)
}