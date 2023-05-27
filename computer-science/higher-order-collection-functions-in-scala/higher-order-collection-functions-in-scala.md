<article class="first">
  <div class="title">
    <h1>Higher-Order Collection Functions in Scala</h1>
  </div>
</article>

---

[![made-with badge](https://img.shields.io/static/v1?label=Made%20with&message=Obsidian&color=7d5bed&logo=obsidian&labelColor=1a1a1a&style=flat)](https://obsidian.md/)

[![type](https://img.shields.io/static/v1?label=Type&message=deep-dive&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAi0lEQVRIS+2WMQ7AIAhF/UNXrtP7rz2OYxeqTWxMTBUSxQVXfnzyQQKC8YExL7zAGCNbgIkIsIKVhBw4vbR7unR6Gp0LvwxXd2v+EvkdDpxWXpWlRTyi9/pABRyBJHEHSlxSadxSlV0SsVsqcUml2W/pynWxnsXNisHMRxrCl8qvH3ECnQDuOmy+0zwB4WNxmUKgwwAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/deep-dives/) [![category](https://img.shields.io/static/v1?label=Category&message=computer-science&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAB9UlEQVRIS6VWMU7DQBDkDAQEdrAoCISCAomCL1DxC95Azy9oeQS/oOIHVFAgREFoCHGCRSzZzEU+63LZ9W6CO/vudmZ2d9Zn1pTPaDSqut2usduHw+FpFEUv7t1fk8LNAkiPDWj3+ADuTPjNvXMxWwGzLCuqqtqwh5MkiY0xEwfOAfrEKFAWUBO4DZQDXgCEqjuouvbZUanUrocpngMMVUkKtKC+WhFQUudAUd8r1PkepJ/w7Tysn4uzkNJlascF9WOASAki6w0xrn19b3Gpps5y3kRfJADPZgr9gJSP0EgDHDiQ/Mp50PfxAmDtuQhsZmb/z0OVhwSkmGrSGp5bGRDp3EFaJ5JaiahdZ2vYNj/JkWVMgW7sgNw2yOW+99gacp7TeFE72OcUrgo4Ho93+/3+D5T9QmGHm0BNSnHgMI7jj9Ai2tElZGCK9S3S+GA4BcNNydBaIuEstu/iLJWCa+pLDm+Nz+xQAsBenucnRVG8asFq0s/Yf9YoVAI21wyn3N4I7M1A8ijWHwB42XrFqIO9YfMRlVqqyXC5ukED3nIEVJcoBXv1lmWa5gIpeeQioyTWVj1uXf0DpgKUZbmfpunXKnVnU9rWDKiTHRSDNkDu36iqIQK/Q+mxU8sBYniL/1EVoJ9Wqwo/5x6Cf9YKv6Em1XbNH5bGfSwvuRe1AAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/categories/computer-science/) [![technologies](https://img.shields.io/static/v1?label=Technologies&message=Scala,%20PowerShell%207,%20VS%20Code&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAACXBIWXMAAAsTAAALEwEAmpwYAAAA1klEQVR4nM2RMW7CUBBEnUikIQUIlBJxrrQgJG7ABRBnoUkaWhpoUgWJlgNYbvz/G1dUi1ayoy87rpOtVrszs6OdLPtXlef5UNJXjHHcCwohjMzsKZ3FGN+Bq/e+c0xHGfiWtEznkg6SNnW/dIxjs0YJ2AMnM3tJSFPgHkKY17gBcAQ+zOw5A3aSbsCkdW0NnNOZY2rstpcInJ3cS/SzwGdqtSzLmdusquqtIXWsehVF8QpcJK1qmxt/TMv6wjE/z0leP27i8Ag8inT/axxtAQ+9o/zn9QD3JOiyTjnQEQAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/technologies/) [![website article](https://img.shields.io/static/v1?label=Website&message=Post%20Link&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAACXBIWXMAAAsTAAALEwEAmpwYAAAB+ElEQVR4nO2VOYgUURCGR/BAI4MN1EwjI89EMDYQvNBNNNlcE0VBUdlUUSMjj2BF2UDRePDAwGzNF2GNPIYd8Hjv/6YnEHSf/FIDPTJiu4nJFBTd1Kv6/nrVBd1q/S8DJiU9AmaBm5LOSjoATPwDY0LSQUnnzDArmJOjkqclvQceSHohaR6oJC1JeiPprqT9pZSVg5pSyirH4sw5S1EzbwZwP5jTIwWBdj1meEppZ6/XOyXpCdCX9Am4Fv45Yo+Bk1VV7ag3FNz2kKC7yznvHiX4u3U6nXU55xPAW7vfHfvLmNtmW8NaFux67k0Ea03esTfJJQTj23bHgiNtPNK6jZem3Wpg46Wp23hp2q0GNl6axksjaRGYkXRF0mnHq6ra2HSk/X5/k6RDks6YEazFPwnuBS5KuirptqTnkj4CJZ4zwNFSytqBoP/2wDHgXi33A/BM0i2zzDR7SBC4LGlPr9fb5huVUlYMus45b5E0FYJfgQS8C8/Al7jJVEpp86DODLPMNDs0up7xXBQZVKLLb8CCpIfA+ZzzvpTS+lLKGuAI8DT8cClltc+c49yoWQjGL140ao25oW8QXW1IKe3KOR8Hbkh66ZtI+i7plaG+iR244JjP3HDkXnetGWbVp9XYopHtHgvwWtIPu9+BSx7bssBNDdhqX07xT/Jbz1SBBDGHAAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/deep-dives/higher-order-collection-functions-in-scala/)

Higher-order functions are functions that take other functions as arguments, and/or return other functions as result. These are powerful abstractions that allow us to perform very complex computations with the benefit of reduced verbosity and declaration. Scala has a strong functional component embedded in its architecture; it then makes sense that Scala provides a wide variety of powerful higher-order functions, specifically for collections such as lists, tuples, arrays, vectors, and more. 

In this Deep Dive, we'll discuss the main higher-order functions available in Scala, specifically for lists. However, we'll also discuss other collections. We'll go over each one of them by explaining in detail why they're for, how to use them, and providing various examples, ranging from simpler ones to more complex ones.

We'll be using Scala worksheets which can be found in the [Deep Dive Repo](https://github.com/pabloagn/deep-dives/tree/master/computer-science/higher-order-collection-functions-in-scala).

---

# Table of Contents
- Preparing our environment
- An introduction to higher-order functions
- An introduction to collections in Scala
- Higher-order list functions
	- map
	- flatMap
	- filter
	- foldLeft
	- foldRight
	- reduceLeft
	- reduceRight
	- scanLeft
	- scanRight
	- zip
	- zipWithIndex
	- forall
	- exists
	- groupBy
	- sort
	- sortBy
	- sortWith
	- minBy
	- maxBy
- [Conclusions](#conclusions)
- [References](#references)
- [Copyright](#copyright)

---

# Preparing our environment
As per usual, we'll prepare a new environment by using [`sbt`](https://www.scala-sbt.org/), [VS Code](https://code.visualstudio.com/download) & [Metals extension for VS Code](https://marketplace.visualstudio.com/items?itemName=scalameta.metals).

We'll start by creating a new folder called `higher-order-collection-functions-in-scala`:

##### **Code**
```PowerShell
New-Item -ItemType Directory -Path higher-order-collection-functions-in-scala
cd higher-order-collection-functions-in-scala
```

We'll then create a new Scala project using `sbt`:

##### **Code**
```PowerShell
sbt new sbt new scala/scala3.g8
```

And name it `higher-order-collection-functions`.

We'll open VS Code in our project's root directory, import the current build, and create a new folder & worksheet, so that our directory structure looks something as such:

```
├───.bloop
├───.metals
├───.vscode
├───project
├───src
│   ├───main
│   │   └───scala
│   ├───test
│   │   └───scala
│   └───worksheets
|       └───higher-order-list-functions.worksheet.sc
└───target
```

We'll open our `higher-order-list-functions.worksheet.sc` and start exploring. 

---

# Higher-order list functions

## 1. map
`map` is a function used to apply a given function to a collection item-wise, meaning each item in our collection is affected by the operation. The return type of `map` is the same as the input type; a new collection with the modified items.

The generic function signature for `map` is the following:

##### **Code**
```Scala
def map[A, B](list: List[A])(f: A => B): List[B]
```

Where:
- `A` represents the type of elements in the input list.
- `B` represents the type of elements in the resulting list.
- `list` is the input list on which the `map` operation is performed.
- `f` is the transformation function that maps each element of type `A` to an element of type `B`.
- `List[B]` is the returning list after transformation.

Let us declare a simple list of integer values, and apply a square function:

##### **Code**
```Scala
val myList1: List[Int] = List(1, 2, 3, 4, 5)
myList1.map(x => x * x)
```

Here, we're first declaring our list, and then deconstructing it by using the `x => x * x` pattern. This pattern tells Scala that we're expecting an element `x`, that is, the element to which we're applying the operation, and we're transforming it to be `x` * `x`.

##### **Output**
```
res0: List[Int] = List(1, 4, 9, 16, 25)
```

We can also define a more complex function that can be applied to our list, for example, for applying a square operation only for even numbers:

##### **Code**
```Scala
// A more elaborate function
def applyFun(x: Int): Int =
    if (x % 2 == 0) x * x
    else x

myList1.map(applyFun)
```

##### **Output**
```
res1: List[Int] = List(1, 4, 3, 16, 5)
```

Also, we can apply a method for generic `List` types, meaning we're not constrained to the `List[Int]` type:

##### **Code**
```Scala
// A generic method
def genericMethod[T](x: T) = x match
    case x:Int => x * x
    case x:String => s"${x} * ${x}"

val myList2 = List(1, 2, "3")

myList2.map(genericMethod)
```

##### **Output**
```
res2: List[Matchable] = List(1, 4, 3 * 3)
```

However, lists of varying types are not recommended; there are other collections more suited for this effect.

What if we have a list of lists, and we want to sum all the elements inside each nested list?

Well, there are several ways to do so, one being with `map`:

##### **Code**
```Scala
// A method matching a list of lists
def matchMultiple(xs: List[Int]): Int = xs match
    case Nil => 0
    case y :: ys => y + matchMultiple(ys)

val myList3: List[List[Int]] = List(List(1, 2, 3), List(4, 5, 6), List(7, 8, 9))

myList3.map(matchMultiple)
```

##### **Output**
```
res3: List[Int] = List(6, 15, 24)
```

What we're doing here is:
- If the list `xs` is `Nil`, meaning an empty list, return 0.
- If the list `xs` follows the deconstructed pattern `y :: ys`, meaning an item `y` of type `Int` followed by the tail of the list denoted by `ys`, add the item `y` to a recursive call of `matchMultiple` using the tail `ys`.

The map function works here, because we're effectively applying a function to each item of the main list `myList3`; in this case, each item is a list itself.

## 2. flatMap
`flatMap` is similar to `flatten`, in that it flattens the collection. We can think of flattening as reducing dimensions of a given collection. For example, a list of nested lists will be flattened and produce a single list, including all elements inside each nested list.

The generic function signature for `flatMap` is the following:

##### **Code**
```Scala
def flatMap[A, B](list: List[A])(f: A => List[B]): List[B]
```

Where:
- `A` represents the type of elements in the input list.
- `B` represents the type of elements in the resulting list.
- `list` is the input list on which the `flatMap` operation is performed.
- `f` is the transformation function that maps each element of type `A` to a list of elements of type `B`.

Let us declare a simple list of lists, and apply a recursive function that squares all the nested elements returns a flattened version of the collection:

##### **Code**
```Scala
/ Calculate square of nested elements using a recursive function
def squaredSum(xs: List[List[Int]]): List[Int] = xs match
    case Nil => Nil
    case y :: ys => y.map(x => x * x) ++ squaredSum(ys)

val myList4: List[List[Int]] = List(List(1, 2, 3), List(4, 5, 6))

squaredSum(myList4)
```

##### **Output**
```
res4: List[Int] = List(1, 4, 9, 16, 25, 36)
```

Let us now perform the same operation using `flatMap`:

##### **Code**
```Scala
// Calculate square of nested elements using flatMap & map
myList4.flatMap(x => x.map(x => x * x))
```

##### **Output**
```
res5: List[Int] = List(1, 4, 9, 16, 25, 36)
```

We can also simply flatten the collection without any operation:

##### **Code**
```Scala
// Return the collection without any operation
myList4.flatMap(x => x)
```

##### **Output**
```
res6: List[Int] = List(1, 2, 3, 4, 5, 6)
```

## 3. filter
`filter` does exactly what it sounds like: It filters elements in a collection by using what's called a predicate. A predicate is a function that evaluates to a Boolean value, depending if the condition is met or not.

The `filter` method is extremely useful since it can take extremely complex predicate functions, and can also be combined (*chained*) with other functions to achieve more complex operations.



## 4. foldLeft


## 5. foldRight


## 6. reduceLeft


## 7. reduceRight


## 8. scanLeft


## 9. scanRight


## 10. zip


## 11. zipWithIndex


## 12. forall


## 13. exists


## 14. groupBy


## 15. sort


## 16. sortBy


## 17. sortWith


## 18. minBy


## 19. maxBy


---

# Chaining functions
Functional programming encourages what's called chaining of operations. This means that we can apply one function after another using a single line, without requiring separate variable definitions for each step. Chaining works because the evaluation of a given function A is taken as argument of the subsequent function B, and so on.

This might sound similar to what SQL does, and that's because they use the same underlying concept called "*fluent API*" or "*method chaining*".

Fluent API is a design pattern that enables code to be written in a way that resembles natural language or a domain-specific language (*DSL*). It allows for chaining multiple operations or method calls together in a concise and readable manner.

Both Scala and SQL share this characteristic because they have adopted the fluent API pattern in their respective designs.

While method chaining is extremely powerful, it must be used with care, since its whole objective is to simplify syntax & improve readability; overusing this feature might result in illegible code.

## 1. mapReduce
Let us start with a simple example, where we want to apply two functions on a list of lists:
- First, calculate the square of all the elements contained in the nested lists
- Then, perform a sum operation for all the nested elements.

##### **Code**
```Scala
// map reduce
def mapReduce(xs: List[List[Int]]): List[Int] = xs match
    case Nil => Nil
    case y :: ys => y.map(x => x * x).reduce(_ + _) :: mapReduce(ys)

val myList5: List[List[Int]] = List(List(1, 2, 3), List(4, 5, 6), List(7, 8, 9))

mapReduce(myList5)
```

##### **Output**
```
res7: List[Int] = List(14, 77, 194)
```

Here, we're chaining two functions: `map` & `reduce`, where:
- `map` applies a square operation to each element contained in the nested lists.
- `reduce` reduces all elements on each nested list to a single number, by performing a sum operation.

## 1. flatMap
We already saw this implementation, which consists of two chained functions:
- `flatten` or `flatMap`
- `map`

Let us declare a function that calculates the 

##### **Code**
```Scala

```

---

# Conclusions
We've reviewed multiple yet simple mechanisms we can employ to make our code cleaner, more elegant, modular, usable, scalable and safer. These measures can not only help us become better programmers but better collaborators. It will make reading code a pleasure instead of an agonizing process and instantly boost our credibility.

---

# References
- [Python Documentation, Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [Python Documentation, Errors & Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Towards Data Science, What happens when you import a Python module?](https://towardsdatascience.com/what-happens-when-you-import-a-python-module-ad6c0efd2640)
- [Towards Data Science, 3 data structures for faster Python Lists](https://towardsdatascience.com/3-data-structures-for-faster-python-lists-f29a7e9c2f92)

---

# Copyright
Pablo Aguirre, Creative Commons Attribution 4.0 International, All Rights Reserved.