var title = "Bucles";
document.getElementById("title").innerHTML =title;

// 1. for
var array = [0,1,2,3,4];
for (let i = 0; i < array.length; i++) {
    const element = array[i];
    console.log(element)
}

// 2. while
let i = 0;
while (i < 8) {
    console.log(i);
    i++;
}

// 3. do while
let j = 0;
do {
    j++;
    console.log(j)
} while (j < 10);