var title = "arrays";
document.getElementById("title").innerHTML =title;

// 1.
var numeros = [1,2,3,4,5];
console.log(numeros);

// 2. 
var estudiantes = [
    'carlos',
    'maria',
    'pedro',
]
console.log(estudiantes);

// 3. Ubicando por indice
console.log(estudiantes[2]);

// 4. Atributos y Metodos
    // length
console.log(estudiantes.length);
    // reverse()
console.log(estudiantes.reverse());
    // sort(): Ordena
console.log(estudiantes.sort());
    // push(): Pone al ultimo
console.log(estudiantes.push('luis'));
console.log(estudiantes);
    // shift():  Elimina el primer elemento
console.log(estudiantes.shift());
console.log(estudiantes);
    // pop(): Elimina el ultimo elemento
console.log(estudiantes.pop());
console.log(estudiantes);
    // indexOf()
console.log(estudiantes.indexOf('pedro'));
    // unshift(): Agrega al inicio!
console.log(estudiantes.unshift('sara'));
console.log(estudiantes);


// 4. 
var grupo_a = [1,2,3];
var grupo_b = [4,5,6];
var ans;
    ans = grupo_a.concat(grupo_b)
console.log(ans)