// 1) Write a function that given a list of countries, returns the country(s) that occur the least/min times
// Example:- ["Argentina", "Cuba", "Chile", "Argentina"]
// Result:-
// ["Cuba", "Chile"]
let country = ['Argentina', 'Cuba', 'Chile', 'Argentina'];
let marker = 0;
for (let i = 1; i < country.length; i++) {
  if (country[marker] === country[i]) {
    country.pop(marker);
    country.pop(i);
    marker++;
  }
}
console.log(country);

// 2) Find the 2nd largest and 2nd smallest number in two arrays of numbers combined
// Example:- [10,5,7,2,4,1,24] & [8,23,29,25,40,0,24]
// Result:-
// 2nd Largest: 29 && 2nd Smallest: 1
const array1 = [10, 5, 7, 2, 4, 1, 24];
const array2 = [8, 23, 29, 25, 40, 0, 24];
let newArr = array1.concat(array2);
newArr.sort();
console.log(newArr[1], newArr[newArr.length - 1]);

// 3) Write a function to represent a Triangle, given input is the number of rows of the triangle
// Example - if the number of rows are 3
// Result:-
// 1
// 2 3
// 4 5 6

const triangleFunction = (rows) => {
  let marker = 0;
  let marker2 = 0;
  let arr = [];
  for (let i = 0; i < rows; i++) {
    marker2 += marker;
    marker = marker + 1;
    marker2 += marker;
  }
  for (let j = 0; j < marker; j++) {
    arr.push(j);
  }
  console.log(arr);
};
