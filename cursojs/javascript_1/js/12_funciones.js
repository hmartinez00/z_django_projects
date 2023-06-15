var title = "Funciones";
document.getElementById("title").innerHTML =title;

// 0. 
    // Definiendo
function suma(a,b) {
    var sum = a+b;
    console.log(sum);
}
    // Llamando a la funcion
suma(12,3);


// 1. funciones con retorno
function dato_trabajador(salario) {
    var salario = salario;
    return salario;
}
var obrero = dato_trabajador(2550);
console.log(`Su salario es: ${obrero}`);


// 2. funciones con flechas o anonimas
    // Primera forma
var resta = function (a,b) {
    var ans = a-b;
    return ans;
}
console.log(resta(2,3));
    // Segunda forma
var resta = (a,b) => a-b;
console.log(resta(2,3));


// 3. funciones anidadas
function operacion(radio) {
    const PI = 3.14;
    function area(radio) {
        var area = PI * radio * radio;
        console.log(`El area es: ${area}`);
    }
    return area(radio)
}
var radio = 4;
operacion(radio);
