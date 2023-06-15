var title = "strings";
document.getElementById("title").innerHTML =title;

// 1. Caracter de escape \n
// let color = 'rojo\nverde';
// console.log(color);

// 2. Metodos de cadenas
// 2.1 length: longitud
// let fruta = 'manzana';
// console.log(fruta.length);
// 2.2 toUpperCase: mayusculas
// console.log(fruta.toUpperCase());
// 2.3 toLowerCase: minusculas
// console.log(fruta.toLowerCase());
// 2.4 indexOf: Busca la primera conincidencia contando desde cero!
// console.log(fruta.indexOf('z'));
// 2.5 slice: Imprime des del caracter de inicio de hasta el caracer final especificados.
// console.log(fruta.slice(2,5));
// 2.5 replace: reemplaza la primera coincidencia.
// console.log(fruta.replace('an', 'erg'));
// 2.5 split: 
// console.log(fruta.split(''));

// 3. Conversion o casteo
var numero_uno = '2';
var numero_dos = '3';
var suma = Number(numero_uno) + Number(numero_dos);
console.log(suma);