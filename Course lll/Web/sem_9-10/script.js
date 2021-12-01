function task(n) {
    console.log("=".repeat(20), `\n\n     Задание ${n}\n`);
    console.log("=".repeat(20));
}
// Task 1
// Напишите цикл, который треугольник:

task(1);
var str = "#";
while (str.length <= 7) {
    console.log(str + "\n");
    str += "#"
}

/**
 * Task 2
 * Напишите программу, которая выводит через console.log все числа от 1 до 100, с двумя исключениями.
 * Для чисел, нацело делящихся на 3, она должна выводить ‘Fizz’, а для чисел, делящихся на 5 (но не на 3) – ‘Buzz’.
 * Когда сумеете – исправьте её так, чтобы она выводила «FizzBuzz» для всех чисел, которые делятся и на 3 и на 5.
 */

// первый вариант
task(2);
for (let i = 1; i < 100; i++) {
    if (i % 3 == 0) {
        console.log(i, 'Fizz');
    } else if (i % 5 == 0) {
        console.log(i, "Buzz");
    }
}

console.log("Задание 2 которые делятся и на 3 и на 5");
for (let i = 1; i < 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
        console.log('FizzBuzz');
    } else {
        console.log(i);
    }
}

/**
 * Task 3
 * Шахматная доска
 */

task(3);
var size = 8;
for (let i = 0; i < size; i++) {
    if (i % 2 == 0) {
        console.log("# ".repeat(size / 2));
    } else {
        console.log(" #".repeat(size / 2));
    }
}

/**
 * Task 4
 * Минимум. 
 * Напишите функцию min, принимающую два аргумента, и возвращающую минимальный из них.
 */
function minOfTwo(a1, a2) {
    return a1 < a2 ? a1 : a2;
}

task(4);
var arr = [15, -30];
console.log("Минимальное:", minOfTwo(arr[0], arr[1]));

/**
 * Task 5
 * Считаем бобы
 * Напишите функцию countBs, которая принимает строку в качестве аргумента, и возвращает количество символов “B”,
 * содержащихся в строке. Затем напишите функцию countChar, которая работает примерно как countBs, 
 * только принимает второй параметр — символ, который мы будем искать в строке (вместо того, чтобы просто считать количество символов “B”).
 * Для этого переделайте функцию countBs.
 */

function countBs(justString) {
    let total = 0;
    for (let i = 0; i < justString.length; i++) {
        total++;
    }
    console.log(total)
}

function countChar(justString, char) {
    let total = 0;
    for (let i = 0; i < justString.length; i++) {
        if (justString.charAt(i) == char) {
            total++;
        }
    }
    console.log(total)
}

task(5);
var text = "Считаем бобы. Символ номер N строки можно получить, добавив к ней .charAt(N) ( “строчка”.charAt(5) ) – схожим образом с получением длины строки при помощи .length. Возвращаемое значение будет строковым, состоящим из одного символа (к примеру, “к”). У первого символа строки позиция 0, что означает, что у последнего символа позиция будет string.length – 1. Другими словами, у строки из двух символов длина 2, а позиции её символов будут 0 и 1.Напишите функцию countBs, которая принимает строку в качестве аргумента, и возвращает количество символов “B”, содержащихся в строке.Затем напишите функцию countChar, которая работает примерно как countBs, только принимает второй параметр — символ, который мы будем искать в строке (вместо того, чтобы просто считать количество символов “B”). Для этого переделайте функцию countBs."
countBs(text)
countChar(text, "С")

/**
 * Task 6
 * Сумма диапазона
 * Напишите функцию range, принимающую два аргумента, начало и конец диапазона, и возвращающую массив,
 * который содержит все числа из него, включая начальное и конечное.Затем напишите функцию sum,
 * принимающую массив чисел и возвращающую их сумму. Запустите указанную выше инструкцию и убедитесь, что она возвращает 55.
 * В качестве бонуса дополните функцию range, чтобы она могла принимать необязательный третий аргумент – шаг для построения массива.
 * Если он не задан, шаг равен единице. Вызов функции range(1, 10, 2) должен будет вернуть [1, 3, 5, 7, 9].
 * Убедитесь, что она работает с отрицательным шагом так, что вызов range(5, 2, -1) возвращает [5, 4, 3, 2].
 */

var range = function(start, end, step) {
    var range = [];
    var typeofStart = typeof start;
    var typeofEnd = typeof end;

    if (step === 0) {
        throw TypeError("Step cannot be zero.");
    }

    if (typeofStart == "undefined" || typeofEnd == "undefined") {
        throw TypeError("Must pass start and end arguments.");
    } else if (typeofStart != typeofEnd) {
        throw TypeError("Start and end arguments must be of same type.");
    }

    typeof step == "undefined" && (step = 1);

    // if (end < start) {
    //     step = -step; // Отрицательный шаг
    // }

    while (step > 0 ? end >= start : end <= start) {
        range.push(start); // аналог append в python
        start += step;
    }

    return range;

}

function sum(array) {
    let sum = 0;
    for (let i = 0; i < array.length; i++) {
        sum += array[i];
    }
    console.log("sum:", sum);
}

function sum2(array) {
    return array.reduce((total, curr) => total + curr);
};

task(6);
console.log(range(5, 2, 1));
sum(range(1, 10));
console.log(`sum2: ${sum2(range(1, 10))}`);

/**
 * Task 7
 * Напишите две функции, reverseArray и reverseArrayInPlace.
 */
function reverseArray(array) {
    let result = [];
    for (let i = array.length - 1; i >= 0; i--)
        result.push(array[i]);
    return result;
}

function reverseArrayInPlace(array) {
    for (let i = 0; i < Math.floor(array.length / 2); i++) {
        let old = array[i];
        let len = array.length - 1 - i;
        array[i] = array[len];
        array[len] = old;
    }
    return array;
}


task(7);
console.log(reverseArray(["10", "20", "30", "35", "40"]));
var arr = ['40', '35', '32', '22', '11'];
reverseArrayInPlace(arr);
console.log(arr);

/**
 * Task 8
 */

function arrayToList(arr) {

    var list = { value: arr[0], rest: null }
    let res = list;

    for (i = 0; i < arr.length; i++) {
        list.rest = {};
        list.rest.value = arr[i];
        list.rest.rest = null;
        list = list.rest;
    }

    return res;

}

function listToArray(list) {
    var arr = [];

    while (list.rest != null) {
        list = list.rest;
        arr.push(list.value);
    }

    return arr;
}

/**
 * Также напишите вспомогательную функцию prepend, которая получает элемент и создаёт новый список,
 * где этот элемент добавлен спереди к первоначальному списку
 */

function prepend(list, elem) {
    return { value: elem, rest: list };
}

/**
 * функция которая в качестве аргументов принимает список и число, а возвращает элемент на заданной позиции в списке,
 * или же undefined в случае отсутствия такого элемента.

 */
function nth(list, index, current = 0) {

    if (index == current) {
        return list.value;
    } else {
        if (list != null) {
            return nth(list.rest, index, current + 1);
        } else {
            return undefined;
        }
    }
}
task(8);
l = arrayToList([1, 21, 34, 4]);
console.log(l);
console.log(listToArray(l));
console.log(prepend(l, 555))
console.log(nth(l, 2));


/**
 * Task 9
 * 
 */

function deepEqual(a, b) {
    if (a === b) {
        return true;
    }

    if (a == null || typeof(a) != "object" ||
        b == null || typeof(b) != "object") {
        return false;
    }

    for (var i in a) {
        if (!(i in b) || !deepEqual(a[i], b[i])) {
            return false;
        }
    }
    return true;
}


task(9);
var obj = { here: { is: "an" }, object: 2 };
console.log(deepEqual(obj, obj));
console.log(deepEqual(obj, { here: 1, object: 2 }));
console.log(deepEqual(obj, { here: { is: "an" }, object: 2 }));

/**
 * Task 10
 * 
 */

task(10);
var arr_task10 = [
    ["Baranov"],
    [1, 2, 3],
    [5, 5],
    [6, 7],
    ["Aleksandr"]
];
arr_task10 = arr_task10.reduce((a, b) => {
    return a.concat(b);
});
console.log(arr_task10);


/**
 * Task 11
 * 
 */
const data = JSON.stringify([
    { "name": "Carolus Haverbeke", "sex": "m", "born": 1832, "died": 1905, "father": "Carel Haverbeke", "mother": "Maria van Brussel" },
    { "name": "Emma de Milliano", "sex": "f", "born": 1876, "died": 1956, "father": "Petrus de Milliano", "mother": "Sophia van Damme" },
    { "name": "Maria de Rycke", "sex": "f", "born": 1683, "died": 1724, "father": "Frederik de Rycke", "mother": "Laurentia van Vlaenderen" },
    { "name": "Jan van Brussel", "sex": "m", "born": 1714, "died": 1748, "father": "Jacobus van Brussel", "mother": "Joanna van Rooten" },
    { "name": "Philibert Haverbeke", "sex": "m", "born": 1907, "died": 1997, "father": "Emile Haverbeke", "mother": "Emma de Milliano" },
    { "name": "Jan Frans van Brussel", "sex": "m", "born": 1761, "died": 1833, "father": "Jacobus Bernardus van Brussel", "mother": null },
    { "name": "Pauwels van Haverbeke", "sex": "m", "born": 1535, "died": 1582, "father": "N. van Haverbeke", "mother": null },
    { "name": "Clara Aernoudts", "sex": "f", "born": 1918, "died": 2012, "father": "Henry Aernoudts", "mother": "Sidonie Coene" },
    { "name": "Emile Haverbeke", "sex": "m", "born": 1877, "died": 1968, "father": "Carolus Haverbeke", "mother": "Maria Sturm" },
    { "name": "Lieven de Causmaecker", "sex": "m", "born": 1696, "died": 1724, "father": "Carel de Causmaecker", "mother": "Joanna Claes" },
    { "name": "Pieter Haverbeke", "sex": "m", "born": 1602, "died": 1642, "father": "Lieven van Haverbeke", "mother": null },
    { "name": "Livina Haverbeke", "sex": "f", "born": 1692, "died": 1743, "father": "Daniel Haverbeke", "mother": "Joanna de Pape" },
    { "name": "Pieter Bernard Haverbeke", "sex": "m", "born": 1695, "died": 1762, "father": "Willem Haverbeke", "mother": "Petronella Wauters" },
    { "name": "Lieven van Haverbeke", "sex": "m", "born": 1570, "died": 1636, "father": "Pauwels van Haverbeke", "mother": "Lievijne Jans" },
    { "name": "Joanna de Causmaecker", "sex": "f", "born": 1762, "died": 1807, "father": "Bernardus de Causmaecker", "mother": null },
    { "name": "Willem Haverbeke", "sex": "m", "born": 1668, "died": 1731, "father": "Lieven Haverbeke", "mother": "Elisabeth Hercke" },
    { "name": "Pieter Antone Haverbeke", "sex": "m", "born": 1753, "died": 1798, "father": "Jan Francies Haverbeke", "mother": "Petronella de Decker" },
    { "name": "Maria van Brussel", "sex": "f", "born": 1801, "died": 1834, "father": "Jan Frans van Brussel", "mother": "Joanna de Causmaecker" },
    { "name": "Angela Haverbeke", "sex": "f", "born": 1728, "died": 1734, "father": "Pieter Bernard Haverbeke", "mother": "Livina de Vrieze" },
    { "name": "Elisabeth Haverbeke", "sex": "f", "born": 1711, "died": 1754, "father": "Jan Haverbeke", "mother": "Maria de Rycke" },
    { "name": "Lievijne Jans", "sex": "f", "born": 1542, "died": 1582, "father": null, "mother": null },
    { "name": "Bernardus de Causmaecker", "sex": "m", "born": 1721, "died": 1789, "father": "Lieven de Causmaecker", "mother": "Livina Haverbeke" },
    { "name": "Jacoba Lammens", "sex": "f", "born": 1699, "died": 1740, "father": "Lieven Lammens", "mother": "Livina de Vrieze" },
    { "name": "Pieter de Decker", "sex": "m", "born": 1705, "died": 1780, "father": "Joos de Decker", "mother": "Petronella van de Steene" },
    { "name": "Joanna de Pape", "sex": "f", "born": 1654, "died": 1723, "father": "Vincent de Pape", "mother": "Petronella Wauters" },
    { "name": "Daniel Haverbeke", "sex": "m", "born": 1652, "died": 1723, "father": "Lieven Haverbeke", "mother": "Elisabeth Hercke" },
    { "name": "Lieven Haverbeke", "sex": "m", "born": 1631, "died": 1676, "father": "Pieter Haverbeke", "mother": "Anna van Hecke" },
    { "name": "Martina de Pape", "sex": "f", "born": 1666, "died": 1727, "father": "Vincent de Pape", "mother": "Petronella Wauters" },
    { "name": "Jan Francies Haverbeke", "sex": "m", "born": 1725, "died": 1779, "father": "Pieter Bernard Haverbeke", "mother": "Livina de Vrieze" },
    { "name": "Maria Haverbeke", "sex": "m", "born": 1905, "died": 1997, "father": "Emile Haverbeke", "mother": "Emma de Milliano" },
    { "name": "Petronella de Decker", "sex": "f", "born": 1731, "died": 1781, "father": "Pieter de Decker", "mother": "Livina Haverbeke" },
    { "name": "Livina Sierens", "sex": "f", "born": 1761, "died": 1826, "father": "Jan Sierens", "mother": "Maria van Waes" },
    { "name": "Laurentia Haverbeke", "sex": "f", "born": 1710, "died": 1786, "father": "Jan Haverbeke", "mother": "Maria de Rycke" },
    { "name": "Carel Haverbeke", "sex": "m", "born": 1796, "died": 1837, "father": "Pieter Antone Haverbeke", "mother": "Livina Sierens" },
    { "name": "Elisabeth Hercke", "sex": "f", "born": 1632, "died": 1674, "father": "Willem Hercke", "mother": "Margriet de Brabander" },
    { "name": "Jan Haverbeke", "sex": "m", "born": 1671, "died": 1731, "father": "Lieven Haverbeke", "mother": "Elisabeth Hercke" },
    { "name": "Anna van Hecke", "sex": "f", "born": 1607, "died": 1670, "father": "Paschasius van Hecke", "mother": "Martijntken Beelaert" },
    { "name": "Maria Sturm", "sex": "f", "born": 1835, "died": 1917, "father": "Charles Sturm", "mother": "Seraphina Spelier" },
    { "name": "Jacobus Bernardus van Brussel", "sex": "m", "born": 1736, "died": 1809, "father": "Jan van Brussel", "mother": "Elisabeth Haverbeke" }
])

function average(array) {
    return array.reduce((a, b) => a + b) / array.length;
}


var ancestry = JSON.parse(data);
var byName = {};

ancestry.forEach(function(person) {
    byName[person.name] = person;
});

var diffs = ancestry.filter(function(person) {
    return byName[person.mother] != null;
}).map(function(person) {
    return person.born - byName[person.mother].born;
});

task(11);
console.log(`Средняя разница: ${Math.round(average(diffs)*10)/10}`);


/**
 * Task 12
 */

var byCenturies = {}

function getCenturyArray(arr) {
    var obj = {};
    arr.forEach(function(p) {
        var id = Math.ceil(p.died / 100);;
        if (obj[id] === undefined) { obj[id] = []; }
        obj[id].push(p)
    });
    return obj;
}

task(12);
var centuries = getCenturyArray(ancestry);
for (century in centuries) {
    centuries[century] = average(centuries[century].map((p) => p.died - p.born));
    console.log(century + ": " + Math.round(centuries[century] * 10) / 10);
}


/**
 * Task 13
 */

function every(array) {
    for (var i = 0; i < array.length; i++) {
        if (!isNaN(array[i]))
            return false;
    }
    return true;
}


function some(array) {
    for (var i = 0; i < array.length; i++) {
        if (isNaN(array[i]))
            return true;
    }
    return false;
}

task(13);
console.log(every([NaN, NaN, NaN]));
console.log(every([NaN, NaN, 4]));
console.log(some([NaN, 3, 4]));
console.log(some([2, 3, 4]));