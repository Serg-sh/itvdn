"use strickt";

// let salaries = {
//     John: 100,
//     Ann: 160,
//     Pete: 130
// };

// let salaries2 = {
//     John: 100,
//     Ann:  160,
//     Pete: 130,
//     Serg: 200

// };

// let sum;
// function sum_obj(obj){
//     let sum = 0;
//     for(let k in obj){
//         sum += obj[k];
//     };
//     return sum
// };
// sum = sum_obj(salaries);
// console.log(sum);
// console.log(sum_obj(salaries2));


let menu = {
    width: 200,
    height: 300,
    title: 'Мое меню'
};

function multiply(obj) {
    for (let key in obj) {
        if (typeof obj[key] == 'number') {
            obj[key] *= 2;
        }

    }
}

console.log(menu);
multiply(menu);
console.log(menu);