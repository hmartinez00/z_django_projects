var title = "Condicionales";
document.getElementById("title").innerHTML =title;

// 1. IF - ELSE
var a = 20;
var b = 20;
if (a > b) {
    console.log(`${a}   es mayor que  ${b}`);
}
else if (a == b) {
    console.log(`${a}   es igual a    ${b}`);
} 
else{
    console.log(`${a}   es menor que  ${b}`);
}

// 2. Operadores logicos
var x = true
var y = false
    // AND
// condition = x && y
    // OR
condition = x || y
console.log(condition)
