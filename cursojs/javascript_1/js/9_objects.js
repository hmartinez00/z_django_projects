var title = "objects";
document.getElementById("title").innerHTML =title;

// 1. Definiendo objetos
const auto = {
    // Definiendo atributos
    marca   : 'Toyota',
    modelo  : 2018,
    color   : 'Azul',
    accesorios   : [
        'motor',
        'llantas',
        'luces',
    ],
}

console.log(auto)
console.log(auto.color)
console.log(auto.accesorios)