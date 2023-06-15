var title = "Funciones II";
document.getElementById("title").innerHTML =title;


// 1.
function area() {
    const PI = 3.14;
    var radio = document.getElementById("radio").value;
    var ans = PI * radio * radio;
    document.getElementById("resultado").value = ans;
}
area();


// 2. funciones reservadas
    // 2.1 eval
var a = 10;
var b = 20;
var x = eval('a + b');
var y = eval('3 + 4');
var z = eval('a + 8');
var ans = [x, y, z];
console.log(ans);

    // 2.2 parsefloat
var a = parseFloat(10);
var b = parseFloat('20curso');
var c = parseInt('10curso');
console.log(c);

    // 2.3 Date.parse
    // Fecha de inicio de javascript: 1 enero de 1970
var dato = 'january 1, 1970 1:30 PM';
var ans = Date.parse(dato);
console.log(ans);