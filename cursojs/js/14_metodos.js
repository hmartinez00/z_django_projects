var title = "Metodos";
document.getElementById("title").innerHTML =title;


let array = [1,2,3,4,5,6,7];

// forEach
array.forEach(element => {
    console.log(element);
});

// some: verifica si alguno de los elementos cumple con la condicion especificada
console.log(
    array.some(element => {
        var ans = (element < 3);
        return ans;
    })
);

// every: Verifica si todos los elementos cumplen con la condicion especificada
console.log(
    array.every(
        element => {
            var ans = (element == 3);
            return ans;
        })
);


// map: permite aplicar operaciones sobre todos los elementos de un array y construye otro con esas operaciones.
let duplicar = array.map(
    element => {
        var ans = (element * 3);
        return ans;
    }
);
console.log(duplicar);


// filter: filtra los elementos que cumplen con la condicion especificada.
var new_array = array.filter(
    element => {
        var ans = (element > 3);
        return ans;
    }
    );
    console.log(new_array);
    
    
    // reduce
var new_ans = array.reduce(
    (sumar, dato) => sumar + dato, 0
);
console.log(new_ans);