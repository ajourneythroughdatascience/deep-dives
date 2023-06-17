<article class="first">
  <div class="title">
    <h1>Destructuring in JavaScript</h1>
  </div>
</article>

---

[![made-with badge](https://img.shields.io/static/v1?label=Made%20with&message=Obsidian&color=7d5bed&logo=obsidian&labelColor=1a1a1a&style=flat)](https://obsidian.md/)

[![type](https://img.shields.io/static/v1?label=Type&message=deep-dive&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAi0lEQVRIS+2WMQ7AIAhF/UNXrtP7rz2OYxeqTWxMTBUSxQVXfnzyQQKC8YExL7zAGCNbgIkIsIKVhBw4vbR7unR6Gp0LvwxXd2v+EvkdDpxWXpWlRTyi9/pABRyBJHEHSlxSadxSlV0SsVsqcUml2W/pynWxnsXNisHMRxrCl8qvH3ECnQDuOmy+0zwB4WNxmUKgwwAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/deep-dives/) [![category](https://img.shields.io/static/v1?label=Category&message=computer-science&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAB9UlEQVRIS6VWMU7DQBDkDAQEdrAoCISCAomCL1DxC95Azy9oeQS/oOIHVFAgREFoCHGCRSzZzEU+63LZ9W6CO/vudmZ2d9Zn1pTPaDSqut2usduHw+FpFEUv7t1fk8LNAkiPDWj3+ADuTPjNvXMxWwGzLCuqqtqwh5MkiY0xEwfOAfrEKFAWUBO4DZQDXgCEqjuouvbZUanUrocpngMMVUkKtKC+WhFQUudAUd8r1PkepJ/w7Tysn4uzkNJlascF9WOASAki6w0xrn19b3Gpps5y3kRfJADPZgr9gJSP0EgDHDiQ/Mp50PfxAmDtuQhsZmb/z0OVhwSkmGrSGp5bGRDp3EFaJ5JaiahdZ2vYNj/JkWVMgW7sgNw2yOW+99gacp7TeFE72OcUrgo4Ho93+/3+D5T9QmGHm0BNSnHgMI7jj9Ai2tElZGCK9S3S+GA4BcNNydBaIuEstu/iLJWCa+pLDm+Nz+xQAsBenucnRVG8asFq0s/Yf9YoVAI21wyn3N4I7M1A8ijWHwB42XrFqIO9YfMRlVqqyXC5ukED3nIEVJcoBXv1lmWa5gIpeeQioyTWVj1uXf0DpgKUZbmfpunXKnVnU9rWDKiTHRSDNkDu36iqIQK/Q+mxU8sBYniL/1EVoJ9Wqwo/5x6Cf9YKv6Em1XbNH5bGfSwvuRe1AAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/categories/computer-science/) [![technologies](https://img.shields.io/static/v1?label=Technologies&message=JavaScript,%20VS%20Code&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAACXBIWXMAAAsTAAALEwEAmpwYAAAA1klEQVR4nM2RMW7CUBBEnUikIQUIlBJxrrQgJG7ABRBnoUkaWhpoUgWJlgNYbvz/G1dUi1ayoy87rpOtVrszs6OdLPtXlef5UNJXjHHcCwohjMzsKZ3FGN+Bq/e+c0xHGfiWtEznkg6SNnW/dIxjs0YJ2AMnM3tJSFPgHkKY17gBcAQ+zOw5A3aSbsCkdW0NnNOZY2rstpcInJ3cS/SzwGdqtSzLmdusquqtIXWsehVF8QpcJK1qmxt/TMv6wjE/z0leP27i8Ag8inT/axxtAQ+9o/zn9QD3JOiyTjnQEQAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/technologies/) [![website article](https://img.shields.io/static/v1?label=Website&message=Post%20Link&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAACXBIWXMAAAsTAAALEwEAmpwYAAAB+ElEQVR4nO2VOYgUURCGR/BAI4MN1EwjI89EMDYQvNBNNNlcE0VBUdlUUSMjj2BF2UDRePDAwGzNF2GNPIYd8Hjv/6YnEHSf/FIDPTJiu4nJFBTd1Kv6/nrVBd1q/S8DJiU9AmaBm5LOSjoATPwDY0LSQUnnzDArmJOjkqclvQceSHohaR6oJC1JeiPprqT9pZSVg5pSyirH4sw5S1EzbwZwP5jTIwWBdj1meEppZ6/XOyXpCdCX9Am4Fv45Yo+Bk1VV7ag3FNz2kKC7yznvHiX4u3U6nXU55xPAW7vfHfvLmNtmW8NaFux67k0Ea03esTfJJQTj23bHgiNtPNK6jZem3Wpg46Wp23hp2q0GNl6axksjaRGYkXRF0mnHq6ra2HSk/X5/k6RDks6YEazFPwnuBS5KuirptqTnkj4CJZ4zwNFSytqBoP/2wDHgXi33A/BM0i2zzDR7SBC4LGlPr9fb5huVUlYMus45b5E0FYJfgQS8C8/Al7jJVEpp86DODLPMNDs0up7xXBQZVKLLb8CCpIfA+ZzzvpTS+lLKGuAI8DT8cClltc+c49yoWQjGL140ao25oW8QXW1IKe3KOR8Hbkh66ZtI+i7plaG+iR244JjP3HDkXnetGWbVp9XYopHtHgvwWtIPu9+BSx7bssBNDdhqX07xT/Jbz1SBBDGHAAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/deep-dives/destructuring-in-javascript/)

Destructuring is a very powerful & widely-used syntactic construct that allows us to decompose a given object or structure into smaller components. This is especially useful when we have, for example, objects with nested elements and would like to extract all or some of them and assign them to variables without having to write multiple lines of code to do so.

Destructuring can be used in various JavaScript structures, such as arrays, objects, function parameters, sets, maps, and even iterables. Each case offers a specific syntax. However, the overall process fairly is similar. 

In this Deep Dive, we'll discuss what destructuring is, how it can be applied to nested structures such as multi-dimensional arrays and objects, how it can be applied to function parameters, and some of its main use cases. Since the list is extensive, we'll not go into all the structures where destructuring can be used. We'll also introduce some examples that will hopefully help illustrate this concept better.

We'll be using JavaScript scripts which can be found in the [Deep Dive Repo](https://github.com/pabloagn/blog/tree/master/computer-science/destructuring-in-javascript).

---

# Table of Contents
- [What is destructuring?](#what-is-destructuring)
- [Why is it useful?](#why-is-it-useful)
	- [Working with APIs](#1-working-with-apis)
	- [Simplified code](#2-simplified-code)
	- [Power](#3-power)
- [General syntax](#general-syntax)
	- [Arrays](#1-arrays)
	- [Objects](#2-objects)
	- [Function parameters](#3-function-parameters)
- [Main features](#main-features)
	- [Skipping elements](#1-skipping-elements)
	- [Using starter values](#2-using-starter-values)
	- [Renaming variables](#3-renaming-variables)
- [Some practical examples](#some-practical-examples)
	- [Deeply nested objects](#1-deeply-nested-objects)
	- [Extracting intermittently from an unknown array](#2-extracting-intermittently-from-an-unknown-array)
	- [An object containing multiple argument groups](#3-an-object-containing-multiple-argument-groups)
- [Conclusions](#conclusions)
- [References](#references)
- [Copyright](#copyright)

---

# What is destructuring?
Simply put, destructuring, also called matching, is a syntactic construct introduced in [ES6 (*ECMAScript 2015*)](http://es6-features.org/#Constants) that lets us deconstruct structures, assigning the nested components to variables in one single line of code.

We can see destructuring as a two-step process:
1. Destructuring the structure
2. Assigning the resulting components to variables

This might sound simple, but it's an extremely powerful feature. Let us understand why.

Let us imagine we have an object with multiple key-value pairs, and some values are arrays. We want to take that object, go for some of the values with array structures, and assign a variable for each element inside these arrays.

Previous to ES6, this was possible by indexing:

##### **Code**
```JavaScript
const myObj = {
    fName: "Emma",
    lName: "Miller",
    interests: ["Reading", "Writing", "Sleeping"]
};

// Indexing method
const mainInterest = myObj.interests[0];
const secondaryInterest = myObj.interests[1];
const tertiaryInterest = myObj.interests[2];

console.log(mainInterest, secondaryInterest, tertiaryInterest);
```

##### **Output**
```
Reading Writing Sleeping
```

This is a complete waste of resources and space, since we're instancing our object on each line, and simply changing the index.

ES6 then introduces a new & more efficient way to handle these types of operations:

##### **Code**
```JavaScript
// Destructuring (ES6) method
const [Int1, Int2, Int3] = myObj.interests
console.log(Int1, Int2, Int3);
```

Which gives the exact same result:

##### **Output**
```
Reading Writing Sleeping
```

This was just an example using arrays, but destructuring can also be applied to objects and function parameters. We can see that the technique is extremely useful.

---

# Why is it useful?
Destructuring patterns, in general, is an extremely useful feature; many languages implement variations of this technique:
- **Scala** has the [pattern matching](https://docs.scala-lang.org/tour/pattern-matching.html) construct, where we can even deconstruct at the type level.
- **Python** also supports deconstruction through its unpacking syntax, which allows us to assign values from a sequence (*such as a list or tuple*) to multiple variables simultaneously
- **Ruby** has support for deconstruction assignment, commonly known as "*destructuring*" or "*parallel assignment*". It allows us to assign values from arrays or hashes to multiple variables.
- Rust, similar to Scala, provides a pattern-matching deconstruction feature, which allows us to extract and bind values from data structures, such as tuples or structs, to variables.

Fair, deconstructing is popular, but why is it so valuable? Simply put, it allows us to extract nested elements from sometimes complex structures without indexing and use considerably less code than if we were to index values in a loop or, even worst, one by one.

One of the main use cases for deconstruction, especially in JavaScript, is when we're working with APIs, but of course, that's not the only one.

## 1. Working with APIs
When working with external APIs, we have no guarantee that the structures returned will be simple, easy to understand, and well-documented. Deconstruction can facilitate interaction with APIs that return complex data structures by easily extracting and assigning the relevant values while keeping our code clean and readable.

## 2. Simplified code
When using deconstruction, we're effectively removing the intermediaries; we remove the use of any temporary variable. With deconstruction, we can directly assign values to variables, making the code more concise and easier to understand. 

Additionally, it's extremely flexible; if we're uncomfortable performing the full deconstruction in one line of code, we can separate our transformations into multiple lines by going one level at a time, similar to what we would do in a `for` loop. We are in control of the depth of deconstruction and can even stay at top levels if we don't need the full granularity.

## 3. Power
Some languages have more powerful features when talking about deconstruction constructs. For example, Scala, a strongly-typed language, lets us deconstruct at the type level, opening the possibilities for performing even the most granular operations while maintaining our code safe.

Even though JavaScript is a dynamically-typed language, and there's no need to think of use cases regarding types, it still provides very powerful use cases, for example, when we're trying to unpack complex structures containing multiple nested objects. Just imagine if we were to use a `for` loop to achieve this.

---

# General syntax
The destructuring syntax is analogous to the one we use to define the structures in the first place. For example, an array destructuring will involve square brackets `[]`, while an object destructuring will involve curly brackets `{}`. Let us look at the three in more detail.

## 1. Arrays
We can destructure an array by using the following syntax:

##### **Code**
```JavaScript
const myArr = [1, 2, 3]
const [val1, val2, val3] = myArr
console.log(val1, val2, val3);
```

##### **Output**
```
1 2 3
```

We can also destructure nested arrays using a similar approach:

##### **Code**
```JavaScript
const myNestedArr = [[1, 2], [3, 4], [5, 6], [7, 8]]
const [[val1,], [val2,], [val3,], [val4,]] = myNestedArr
console.log(val1, val2, val3, val4);
```

##### **Output**
```
1 3 5 7
```

In this example, we introduced skipping elements, which we'll review shortly. Still, the idea is that we can go as deep as we'd like in terms of structure nesting simply by mimicking the structure we're trying to deconstruct on the left side of the operation.

## 2. Objects
The mechanics are similar to objects. The main difference is that, with the latter, we're not working with an iterable object; an object does not store keys in an ordered structure. Instead, we purposefully provide a unique name for each value.

Thus, we cannot skip elements or use other names to assign our variables. Instead, we must use the actual object key's names:

##### **Code**
```JavaScript
const groundSupportPlane = {
    model: "A-10 Warthog",
    dimensions: { len: "53ft", wingspan: "57ft", height: "14ft" },
    power: { engines: "Twin General Electric TF34-GE-100 turbofans", thrust: "9,065 pounds (40.32 kilonewtons) of thrust per engine" },
    primaryWeapon: "GAU-8/A Avenger 30mm Gatling"
};

const { model, dimensions, power, primaryWeapon } = groundSupportPlane;
console.log(model, dimensions, power, primaryWeapon);
```

##### **Output**
```
A-10 Warthog { len: '53ft', wingspan: '57ft', height: '14ft' } {
  engines: 'Twin General Electric TF34-GE-100 turbofans',
  thrust: '9,065 pounds (40.32 kilonewtons) of thrust per engine'
} GAU-8/A Avenger 30mm Gatling
```

Once we have our variables assigned, we can rename them in the same expression. However, we'll leave this for later.

## 3. Function parameters
Another useful application consists of designing objects containing function parameters and then deconstructing them inside the actual function. This is called parameter packing/unpacking and can be useful whenever we have functions with many arguments.

We can declare a simple function and pass its parameters into an object by using the following syntax:

##### **Code**
```JavaScript
function getPlaneSpecs(args) {
    const { model, dimensions, power, primaryWeapon } = args
    console.log(`The ${model} is a ground support plane built by the US military.`);
    console.log(`Its dimensions are: ${dimensions.len} by ${dimensions.wingspan} by ${dimensions.height}.`);
    console.log(`The plane is equipped with a ${primaryWeapon} cannon, and is powered by two ${power.engines}.`);
}

// Declaring the function parameters object
const groundSupportPlane = {
    model: "A-10 Warthog",
    dimensions: { len: "53ft", wingspan: "57ft", height: "14ft" },
    power: { engines: "Twin General Electric TF34-GE-100 turbofans", thrust: "9,065 pounds (40.32 kilonewtons) of thrust per engine" },
    primaryWeapon: "GAU-8/A Avenger 30mm Gatling"
};

getPlaneSpecs(groundSupportPlane)
```

##### **Output**
```
The A-10 Warthog is a ground support plane built by the US military.
Its dimensions are: 53ft by 57ft by 14ft.
The plane is equipped with a GAU-8/A Avenger 30mm Gatling cannon, and is powered by two Twin General Electric TF34-GE-100 turbofans.
```

As we can see, we can leave out parameters that are not important to us, and not even extract them from the original object.

---

# Main features
Destructuring can be mainly applied to three different structures:
- Arrays
- Objects
- Function parameters

## 1. Skipping elements
Additionally, we can also skip elements, depending on if we're not interested in returning a given element. For example, following the `myObj` implementation we reviewed earlier, we can extract only the first and third interests by using the following syntax:

##### **Code**
```JavaScript
const [Int1, , Int3] = myObj.interests
console.log(Int1, Int3);
```

##### **Output**
```
Reading Sleeping
```

If we look closely, we skipped the middle element by simply not defining any variable in its place.

## 2. Using starter values
There are times when we don't know if an index position will be there (*in the structure we're working on*). In those cases, it's useful to have some kind of fallback value; otherwise, JavaScript will return `undefined`, which may lead to unexpected behavior and hard-to-debug errors if we don't handle these occurrences carefully.

Destructuring lets us set predefined values for a given variable. For example, we might not know that the array inside the object we're trying to access contains only three values:

##### **Code**
```JavaScript
const [val1 = "", val2 = "", val3 = "", val4 = ""] = myObj.interests
console.log(val1, val2, val3, val4);
```

##### **Output**
```
Reading Writing Sleeping
```

Otherwise, we would get the following:

##### **Code**
```JavaScript
const [val1, val2, val3, val4] = myObj.interests
console.log(val1, val2, val3, val4);
```

##### **Output**
```
Reading Writing Sleeping undefined
```

This also applies for objects and function parameters:

##### **Code**
```JavaScript
// Default values for objects
const { fName = "", lName = "", interests = "", favFood = "" } = myObj
console.log(fName, lName, interests, favFood);
```

##### **Output**
```
Emma Miller [ 'Reading', 'Writing', 'Sleeping' ] 
```

##### **Code**
```JavaScript
// Default values for function parameters
function myFun(params) {
    const { Country = "", City = "", Coords = "", Temp = "" } = params
    console.log(`Country : ${Country} \nCity: ${City} \nCoordinates: ${Coords} \nTemperature: ${Temp}`);
}

const funParams = {
    Country: "Austria",
    City: "Vienna",
    Coords: [48.2082, 16.3738]
}

myFun(funParams)
```

##### **Output**
```
Country : Austria 
City: Vienna 
Coordinates: 48.2082,16.3738 
Temperature:
```

## 3. Renaming variables
When destructuring objects, we mentioned that we needed to use the same variable names we declared when creating our object. For example, the destructuring pattern below would not work:

##### **Code**
```JavaScript
const myObj = {
    val1: "JavaScript",
    val2: "is",
    val3: "weird"
}

const { word1, word2, word3 } = myObj
console.log(word1, word2, word3);
```

##### **Output**
```
undefined undefined undefined
```

The only way to do this, would be by referencing the keys by their actual name:

##### **Code**
```JavaScript
const { val1, val2, val3 } = myObj
console.log(val1, val2, val3);
```

##### **Output**
```
JavaScript is weird
```

However, there is one trick we can use in order to reassign variable names:

##### **Code**
```JavaScript
const { val1: word1, val2: word2, val3: word3 } = myObj
console.log(word1, word2, word3);
```

##### **Output**
```
JavaScript is weird
```

Note that we still need to use the original variable names, but now, we simply reassign them to other variables, effectively changing the name in the same operation.

---

# Some practical examples

## 1. Deeply nested objects
Let us imagine we just got a database entry containing the information of a potential client we would like to contact to offer some of our services. The problem is that we have limited resources and want only to get the most relevant client fields.

The object has the following structure:

##### **Code**
```JavaScript
// Define an object
const clientInfo = {
    fName: "John Doe",
    age: 30,
    contact: {
        email: "johndoe@example.com",
        phone: {
            countryCode: "+1",
            number: "555-1234"
        },
        address: {
            street: "123 Main Street",
            city: "New York",
            state: "NY",
            zipCode: "10001"
        }
    },
    preferences: {
        language: "English",
        theme: "Dark",
        notifications: {
            email: true,
            sms: false
        }
    }
};
```

We can extract only the interesting fields, by extracting with the appropriate depth, and only selecting the required values:

##### **Code**
```JavaScript
// Deconstruct the object by extracting the most relevant information
const { fName, age, contact: { email: address }, contact: { phone: { number }, address: { state }, address: { city } }, preferences: { language }, preferences: { notifications: { email: emailContactPermission } } } = clientInfo

// Log the values
console.log(fName, age, address, number, state, city, language, emailContactPermission);
```

We can see that we had to access deeply nested objects by using the following strategy:

```
level_1 : { level_2: { level_3: level_3_renamed } }
```

We also had to rename one variable, since we had repeated nested elements (*`email`*). However, the effort is worth it since we now have a nice set of our client's most relevant fields:

##### **Output**
```
John Doe 30 johndoe@example.com 555-1234 NY New York English true
```

## 2. Extracting intermittently from an unknown array
Let us imagine a scenario where we have an array with two levels of depth and would like to extract the first, third, and fifth elements from the first level and all the elements except the first one from the second level. However, the number of elements in the second level is unknown to us (*we only know that there are at least two elements*).

The structure is something such as:

##### **Code**
```JavaScript
const myArr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
```

So the strategy would consist of the following:
- Get the required first-level elements using skipping.
- Get the required second-level elements using skipping, followed by a spread operator to include the remaining elements.

We have not yet reviewed the rest operator. However, it's fairly simple; it includes all the elements of a given array and is denoted by three dots `...`.

So, now that we have our strategy, we can define our destructuring pattern:

##### **Code**
```JavaScript
const [[, ...aa], , [, ...bb], , [, ...cc]] = myArr
console.log(aa, bb, cc);
```

##### **Output**
```
[ 2, 3 ] [ 8, 9 ] [ 'e', 'f' ]
```

## 3. An object containing multiple argument groups
Let us think of an example where we have a function that calculates a person's age by using their birth date and then prints out a set of useful values about the person in question.

We can first abstract a person by using an object:

##### **Code**
```JavaScript
// Define an object
const person = {
    fName: "Emma",
    lName: "Lovelace",
    birthDate: 1992,
    address: {
        street: "36, Obere Amtshausgasse",
        suburb: "Reinprechtsdorf",
        city: "Vienna",
        postCode: 1050, country: "Austria"
    },
    occupation: "Artist",
    family: {
        husband: "Peter",
        daughter: "Emma",
        son: "Christoph"
    }
}
```

We can then create a simple function for displaying basic data about this person and returning a new object with only the fields we would like to preserve:

##### **Code**
```JavaScript
// Defining a function
function introducePerson(args) {
    const currYear = new Date().getFullYear();

    // Since we do not want the person's address, we skip it
    const { fName, lName, birthDate, occupation, family: { husband } } = args;

    // Assign a new key-value pair including the person's calculated age
    const age = currYear - birthDate;
    person.age = age

    // Build a template literal
    const introduction = `Name: ${fName}\nLast Name: ${lName}\nAge: ${age}\nOccupation: ${occupation}\nHusband: ${husband}`
    console.log(introduction);

    // Build a new object with interesting fields
    const cleanPerson = {
        fName: fName,
        lName: lName,
        birthDate: birthDate,
        occupation: occupation,
        husband: husband
    }

    return cleanPerson
}

cleanPerson = introducePerson(person)
console.log(cleanPerson);
```

##### **Output**
```
Name: Emma
Last Name: Lovelace
Age: 31
Occupation: Artist
Husband: Peter

{
  fName: 'Emma',
  lName: 'Lovelace',
  birthDate: 1992,
  occupation: 'Artist',
  husband: 'Peter'
}
```

---

# Conclusions
In this segment, we discussed what deconstruction is in the context of JavaScript, why it is useful, how it can be applied, to which structures we can apply it, its main syntax depending on the structure we're trying to deconstruct, some of the main features of this construct, and its main advantages. We also reviewed some simple, practical examples to illustrate why this technique is so useful for some scenarios.

Deconstruction is a powerful construct that effortlessly lets us extract values from arrays, objects, and other data structures. It greatly enhances code readability and reduces the need for repetitive access. Additionally, it can be used for multiple scenarios: from simplifying function parameters and iterating through arrays to enabling a more intuitive approach to data manipulation and dynamic assignment.

---

# References
- [Destructuring assignment, MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)
- [Destructuring Function Parameters in JavaScript, Medium](https://javascript.plainenglish.io/destructuring-function-parameters-d110c59d7b8c)
- [A Brief Introduction to Array Destructuring in ES6, FreeCodeCamp](https://www.freecodecamp.org/news/array-destructuring-in-es6-30e398f21d10/)

---

# Copyright
Pablo Aguirre, Creative Commons Attribution 4.0 International, All Rights Reserved.