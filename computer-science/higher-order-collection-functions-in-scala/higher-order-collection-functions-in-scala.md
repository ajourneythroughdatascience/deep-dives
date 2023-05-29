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
	- Creating a generic higher-order collection function
	- Chaining functions
		- mapReduce
		- A
		- A
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

The generic function signature for `filter` is the following:

##### **Code**
```Scala
def filter[A](list: List[A])(predicate: A => Boolean): List[A]
```

Where:
- `(list: List[A])` is the function that takes a parameter named `list`, which is of type `List[A]`.
- `(predicate: A => Boolean)` is the function takes another parameter named `predicate`, which is a function that takes an element of type `A` and returns a Boolean value.
- `: List[A]` denotes the return type of the function.

Let us declare a simple list of integer values, and apply a recursive function that verifies if a given element is even:

##### **Code**
```Scala
// Declare a recursive function that filters even numbers
def checkEven(xs: List[Int]): List[Int] = xs match
    case Nil => Nil
    case y :: ys => if (y % 2 == 0) y :: checkEven(ys) else checkEven(ys)

val myList7: List[Int] = List(1, 2, 3, 4, 5, 6, 7, 8, 9)
checkEven(myList7)
```

##### **Output**
```
res7: List[Int] = List(2, 4, 6, 8)
```

Now, let us perform the exact same operation using `filter`:

##### **Code**
```Scala
// Filter even numbers using filter
myList7.filter(x => x % 2 == 0)
```

##### **Output**
```
res8: List[Int] = List(2, 4, 6, 8)
```

We can also use filter to compare a given condition using the same list elements as reference. For example, we can compare if the entire list is less than the head of the list (*the first element*):

##### **Code**
```Scala
// Filter a list of strings
val myList8: List[String] = List("d", "b", "e", "a", "t", "b", "y", "z")

myList8.filter(x => x < myList8.head)
```

##### **Output**
```
res9: List[String] = List(b, a, b)
```

If we change this for less than or equal to, the first element will also be included in the resulting collection (*it will filter itself*):

##### **Code**
```Scala
myList8.filter(x => x <= myList8.head)
```

##### **Output**
```
res10: List[String] = List(d, b, a, b)
```

## 4. foldLeft
`foldLeft` belongs to a greater classification called `fold`. What `foldLeft` does, is reduce a list from right to left by applying some predefined operation. For example, a fold on `List(1, 2, 3, 4, 5)` will go from right to left, taking each element, and applying the operation we provide.

The `fold` methods require what's called an accumulator as a given parameter; this is a value that keeps count of the result of the operation, and returns it as the result.

We'll see that the `reduce` methods perform practically the same operation than `fold`, and do not require an explicit accumulator declaration. However, it can sometimes be advantageous to use an accumulator different than the first element in our collection.

The generic function signature for `foldLeft` is the following:

##### **Code**
```Scala
def foldLeft[A, B](list: List[A])(initialValue: B)(accumulator: (B, A) => B): B
```

Where:
- `foldLeft` is the name of the function.
- `[A, B]` are type parameter declarations. The letter `A` represents the type of elements in the list, and `B` represents the type of the accumulated result.
- `(list: List[A])` is the function takes a parameter named `list`, which is of type `List[A]`. It represents the input list that will be folded over.
- `(initialValue: B)` is the function takes another parameter named `initialValue`, which represents the initial value of the accumulator.
- `(accumulator: (B, A) => B)` is the function takes a third parameter named `accumulator`, which is a function that takes the current accumulated value of type `B` and an element of type `A`, and returns the updated accumulated value of type `B`.
- `: B` denotes the return type of the function. It specifies that the function will return the final accumulated value of type `B`.

Let us provide a simple example where we have a list of lists, and we want to reduce the nested lists by performing a product operation. We can do this using a recursive definition first:

##### **Code**
```Scala
// Define a recursive function calculating the product of items and returning a list of integer values
def foldListsLeft(xs: List[List[Int]], f: List[Int] => Int): List[Int] = xs match
    case Nil => Nil
    case y :: ys => f(y) :: foldListsLeft(ys, f)

// Define the product helper function
def productsInt(xs: List[Int]): Int = 
    def prodAccumulate(xs: List[Int], acc: Int): Int = 
        if (xs.isEmpty) acc
        else xs.head * prodAccumulate(xs.tail, acc)
    prodAccumulate(xs, 1)

val myList9: List[List[Int]] = List(List(1, 2, 3), List(4, 5, 6), List(7, 8, 9))

foldListsLeft(myList9, productsInt)
```

What we're doing is:
- Declaring a recursive function that will go over all nested lists inside the main list.
- Apply a product operation using a helper function `productsInt`
- Calling the recursive function with a list of lists.

##### **Output**
```
res11: List[Int] = List(6, 120, 504)
```

The `reduceLeft` method does this, but in three lines:

##### **Code**
```Scala
// Calculate sum of products using foldLeft
def foldListsLeft2(xs: List[List[Int]]): List[Int] = xs match
    case Nil => Nil
    case y :: ys => y.foldLeft(1)(_ * _) :: foldListsLeft2(ys)

foldListsLeft2(myList9)
```

##### **Output**
```
res12: List[Int] = List(6, 120, 504)
```

What `foldLeft` is doing, is:
- Taking the first element of a list of lists (*a list of type `List[Int]`*)
- Folding left by calculating the product of each element with the second one. This is achieved via the deconstruction of `List[Int]` using `_*_`.
- Calling the function recursively by constructing a new list using the `::` operator.

## 5. foldRight
`foldRight` works the same as foldLeft, the only difference being that the order of operations goes from left to right. This does not matter when we're performing operations such as product or addition, but starts to matter when we have less direct operations; even with a subtraction operation, the order starts to matter.

The generic function signature for `foldRight` is the following:

##### **Code**
```Scala
def foldRight[A, B](list: List[A])(initialValue: B)(accumulator: (A, B) => B): B
```

Where:
- `foldRight` is the name of the function.
- `[A, B]` are type parameter declarations. The letter `A` represents the type of elements in the list, and `B` represents the type of the accumulated result.
- `(list: List[A])` is the parameter named `list`, which is of type `List[A]`. It represents the input list that will be folded over.
- `(initialValue: B)` is the function that takes another parameter named `initialValue`, which represents the initial value of the accumulator.
- `(accumulator: (A, B) => B)` is the parameter named `accumulator`, which is a function that takes an element of type `A` and the current accumulated value of type `B`, and returns the updated accumulated value of type `B`.
- `: B` denotes the return type of the function. It specifies that the function will return the final accumulated value of type `B`.

Let us define a a list of integer values that we want to reduce by subtracting all elements. We'll do it both ways: left to right, and right to left:

##### **Code**
```Scala
// Define a list of integer values
val myList10: List[Int] = List(1, 2, 3, 4)

// Compare between both foldLeft & foldRight
myList10.foldLeft(0)(_ - _)
myList10.foldRight(0)(_ - _)
```

##### **Output**
```
res13: Int = -10
res14: Int = -2
```

Here we can see that the order indeed matters since we're dealing with a subtraction operator. This is just a simple use case, but there are more complex cases we can explore. However, we'll leave that to the equivalent `reduce` methods.

## 6. reduceLeft
As mentioned, reduceLeft works practically the same as foldLeft, the main difference being than the `reduce` methods do not require an initial parameter to be explicitly declared.

The generic function signature for `reduceLeft` is the following:

##### **Code**
```Scala
def reduceLeft[A](list: List[A])(accumulator: (A, A) => A): A
```

Where:
- `reduceLeft` is a higher-order function in Scala.
- It takes a list of elements of type `A` and an accumulator function.
- The accumulator function combines two elements of type `A` and returns a result of type `A`.
- `reduceLeft` applies the accumulator function successively to the elements of the list from left to right, using the first element as the starting point.
- It returns the final result, which is of type `A`.

Let us define a list of characters that we want to concatenate into a single string. We'll first do it by defining a recursive method:

##### **Code**
```Scala
def concatList(xs: List[Char]): String = xs match
    case Nil => ""
    case y :: ys => y.toString + concatList(ys)

val myList11: List[Char] = List('S', 'c', 'a', 'l', 'a')

concatList(myList11)
```

##### **Output**
```
res15: String = Scala
```

We can start seeing a common pattern here: When we define a recursive method using pattern matching like we've been defining in this segment, we need to declare at least two cases:
- **Case 1:** When list is empty (*`Nil`*), return the most basic unit of the return type we're trying to produce.
	- In the case of an `Int` when calculating sums, we need to provide a 0.
	- In the case of an `Int` when calculating products, we need to provide a 1.
	- In the case of a `String` when performing concatenations, we need to provide an empty string.
	- In the case of a `Char`, the same applies.
- **Case 2:** When the list is not empty, and follows the pattern `y :: ys`, we recursively call our function while performing the desired operation.

We can now perform a similar operation using `reduceLeft`. With `reduceLeft`, it's a little trickier, since we cannot directly provide recursively a value of a different type while performing the transformation; we could do that with our recursive declaration, since we explicitly defined the function signature to be `concatList(xs: List[Char]): String`.

Because of this, we'll need to use another higher-order function to first change types, and then reduce to a string:

##### **Code**
```Scala
myList11.map(a => a.toString).reduceLeft(_ + _)
```

## 7. reduceRight
`reduceRight` works exactly the same, only that the direction of the reduction is inverted.

The generic function signature for `reduceLeft` is the following:

##### **Code**
```Scala
def reduceRight[A](list: List[A])(accumulator: (A, A) => A): A
```

Where:
- `reduceRight` is a higher-order function in Scala.
- It takes a list of elements of type `A` and an accumulator function.
- The accumulator function combines two elements of type `A` and returns a result of type `A`.
- `reduceRight` applies the accumulator function successively to the elements of the list from right to left, using the last element as the starting point.
- It returns the final result, which is of type `A`.

Contrary to common sense, a reduceRight will not invert our list; instead, it will concatenate in the same order, but starting from the inverse direction.

For example, the reduceRight version of our previous implementation would yield exactly the same:

##### **Code**
```Scala
myList11.map(a => a.toString).reduceRight(_ + _)
```

##### **Output**
```
res17: String = Scala
```

If we want to reverse our list using `reduceRight`, we can exchange each item recursively:

##### **Code**
```Scala
val myList12: List[Char] = List('a', 'l', 'a', 'c', 'S')
myList12.map(a => a.toString).reduceRight((a, b) => b + a)
```

##### **Output**
```
res18: String = Scala
```

## 8. scanLeft
scanLeft is similar to fold & reduce, but instead of returning an accumulator with the total value computed by a given operation, it introduces a collection of intermediate cumulative results using a start value.

The generic function signature for `scanLeft` is the following:

##### **Code**
```Scala
def scanLeft[A, B](list: List[A])(initialValue: B)(accumulator: (B, A) => B): List[B]
```

This is a little confusing, so let's explain it with an example. Let us declare a simple list of integer values, and apply a `scanLeft` method using the addition operator:

##### **Code**
```Scala
val myList13: List[Int] = List(2, 2, 2, 2, 2, 2, 2)

myList13.scanLeft(2)(_ * _)
```

##### **Output**
```
res19: List[Int] = List(2, 4, 8, 16, 32, 64, 128, 256)
```

This operation actually returns the power sequence of 2. Interesting. So in general terms, the `scanLeft` function is going over each element in our list, and starting from a predefined accumulator, computing the product operation between a pair of elements, and returning a collection with the accumulated results on each step.

We can visualize each step of the `reduceLeft` method in this diagram:

```
2 = 2
2 * 2 = 4
2 * 4 = 8
2 * 8*
...
```

Where the first element is our initial accumulator parameter.

If we modify our initial accumulator to 1, the behavior is the same, with the difference of the first element:

##### **Code**
```Scala
myList13.scanLeft(1)(_ * _)
```

##### **Output**
```
res20: List[Int] = List(1, 2, 4, 8, 16, 32, 64, 128)
```

So the accumulator simply serves to mark the first entry, and from there, each accumulation is inserted in our new sequence in a recursive fashion.

## 9. scanRight
scanRight is the scanLeft equivalent in inverse direction, meaning the order of items in the resulting collection will be inverse of that of `reduceLeft`.

The generic function signature for `scanRight` is the following:

##### **Code**
```Scala
def scanRight[A, B](list: List[A])(initialValue: B)(accumulator: (A, B) => B): List[B]
```

Where:
- `scanRight` is a higher-order function in Scala.
- It takes a list of elements of type `A`, an initial value of type `B`, and an accumulator function.
- The accumulator function combines an element of type `A` with the accumulated value of type `B` and returns an updated value of type `B`.
- `scanRight` applies the accumulator function successively to the elements of the list from right to left, starting with the initial value.
- It returns a new list of accumulated values, where each element represents the result of applying the accumulator function up to that point. The type of the elements in the resulting list is `B`.

We can use `reduceRight` to calculate the power of a given integer number:

##### **Code**
```Scala
def computePower(x: Int, y: Int): Int =
    val myCollection: List[Int] = List.fill(y)(x)
    myCollection.scanRight(1)(_ * _).head

computePower(2, 3)
```

What `computePower` is doing, is:
- It accepts the integer number `x` elevated to the power of `y`.
- It then creates a list containing `x` elements `y` times.
- Finally, it uses `scanRight` with the initial accumulator defined as `1`, and a product operation throughout the entire collection.
- It returns the head of the collection, which will be the actual power of the number elevated to `y`.

##### **Output**
```
res21: Int = 8
```

## 10. zip
We might have heard of the `zip` function from a Python context, for example, whenever we're trying to create dictionaries.

The `zip` method in Scala is used to merge a collection to a current collection resulting in a new collection of pair of tuple elements from both collections.

Essentially, we're packing two collections into one, creating combinations of collection A & collection B.

The generic function signature for `scanRight` is the following:

##### **Code**
```Scala
def zip[A, B](list1: List[A], list2: List[B]): List[(A, B)]
```

Where:
- `zip` is a function in Scala that takes two lists, `list1` of type `List[A]` and `list2` of type `List[B]`.
- It combines the corresponding elements from both lists and returns a new list where each element is a tuple `(A, B)` representing the pairs of elements from the original lists.
- The resulting list will have a length equal to the shorter of the two input lists.
- The type of elements in the resulting list is `(A, B)`, a tuple where the first element comes from `list1` and the second element comes from `list2`.

Let us start by declaring a recursive method to accomplish a `zip` operation:

##### **Code**
```Scala
def zipCollections(xs: List[Int], ys: List[Int]): List[List[Int]] = (xs, ys) match
    case (Nil, Nil) => Nil
    case (Nil, z :: zs) => Nil
    case (z :: zs, Nil) => Nil
    case (z :: zs, d :: ds) => List(z, d) :: zipCollections(zs, ds)

val myList14: List[Int] = List(1, 2, 3, 4)
val myList15: List[Int] = List(4, 3, 2, 1)

zipCollections(myList14, myList15)
```

##### **Output**
```
res22: List[List[Int]] = List(List(1, 4), List(2, 3), List(3, 2), List(4, 1))
```

What we're doing here, is covering for all possible cases that can occur in a pair of list of integers by matching our two lists simultaneously. This can be done because we're packing our pair of lists in a tuple; we then deconstruct this tuple into element `xs` and `ys` in the cases below.

This ensures that if a list `A` has different length than a list `B`, the resulting pair will be `Nil`:

##### **Code**
```Scala
val myList14: List[Int] = List(1, 2, 3, 4)
val myList15: List[Int] = List(4, 3, 2)
```

##### **Output**
```
res22: List[List[Int]] = List(List(1, 4), List(2, 3), List(3, 2))
```

We can do the same in a single line by using the `zip` method:

##### **Code**
```Scala
myList14.zip(myList15)
```

##### **Output**
```
res23: List[Tuple2[Int, Int]] = List((1,4), (2,3), (3,2), (4,1))
```

## 11. zipWithIndex
`zipWithIndex` is similar to `zip`, the difference being that instead of combining elements from two separate lists, we include an index to the first element of a list `A`.

The generic function signature for `zipWithIndex` is the following:

##### **Code**
```Scala
def zipWithIndex[A](list: List[A]): List[(A, Int)]
```

Where:
- `zipWithIndex` is a function in Scala that takes a list of elements of type `A`.
- It pairs each element of the list with its corresponding index.
- The resulting list will contain tuples `(A, Int)`, where the first element is an element from the original list, and the second element is its corresponding index.
- The index starts from 0 for the first element and increments by 1 for each subsequent element.

Let us declare a list of strings containing random names, and apply the `zipWithIndex` function to see what it does:

##### **Code**
```Scala
val myList16: List[String] = List("Carolina", "Emma", "Diego", "Will", "Charles")
myList16.zipWithIndex(0)
```

##### **Output**
```
res24: Tuple2[String, Int] = (Carolina,0)
```

So, the index we specify is applied to the first element of the list. This is not that useful for one single element, but we can iterate over the entire collection and assign an incremental index to our whole collection. There are two main easy methods we can use to approach this:
- By using the `foreach` iterator.
- By using `map`

##### **Code**
```Scala
// Using map
myList16.zipWithIndex.map(x => x)

// Using foreach
myList16.zipWithIndex.foreach(x => println(x))
```

##### **Output**
```
res25: List[Tuple2[String, Int]] = List((Carolina,0), (Emma,1), (Diego,2), (Will,3), (Charles,4))

// (Carolina,0)  
// (Emma,1)  
// (Diego,2)  
// (Will,3)  
// (Charles,4)
```

The results will be of different type, since on the first one, we're actually applying the function, whose return value can be assigned to a new variable, while on the second one, the return type of `foreach` will always be `Unit`; in short, if we want to create a new collection with indexed elements, we use `map` or `flatMap`.  

## 12. forall
`forall` is used to evaluate if all elements in a given collection comply with a specified predicate. As we have seen, a predicate is a function that accepts a "*test*", and returns a `Boolean` value depending on the outcome of the test.

As we will see, forall is similar to filter in this way, but the difference is that the first one returns a `Boolean` value if the entire collection complies, while the second one returns the element that complied with the predicate. 

The generic function signature for `forall` is the following:

##### **Code**
```Scala
def forall[A](list: List[A])(predicate: A => Boolean): Boolean
```

Where:
- `forall` is a higher-order function in Scala.
- It takes a list of elements of type `A` and a predicate function `predicate`.
- The predicate function takes an element of type `A` and returns a Boolean value.
- `forall` applies the predicate function to each element in the list and checks if the predicate holds true for all elements.
- It returns a `Boolean` value indicating whether the predicate holds true for all elements in the list.
- The return type is `Boolean`. It will be `true` if the predicate holds true for all elements, and `false` otherwise.

We can check if a list contains exclusively even integers:

##### **Code**
```Scala
val myList17: List[Int] = List(1, 2, 3, 4, 5)
val myList18: List[Int] = List(2, 4, 6, 8)

myList17.forall(x => x % 2 == 0)
myList18.forall(x => x % 2 == 0)
```

##### **Output**
```
res27: Boolean = false
res28: Boolean = true
```

We can implement a similar definition by using a recursive declaration, leveraging the logical operator `&`:

##### **Code**
```Scala
// Implementing forall using a recursive function
def compliesAll(xs: List[Int]): Boolean = xs match
    case Nil => throw Error("Nothing")
    case y :: Nil => (y % 2 == 0)
    case y :: ys => (y % 2 == 0) & compliesAll(ys)

compliesAll(List(2, 2, 1, 3))
compliesAll(List(2, 2, 4, 6))
compliesAll(List(1, 2, 2))
compliesAll(List(1))
compliesAll(List(0))
compliesAll(List())
```

##### **Output**
```
res29: Boolean = false
res30: Boolean = true
res31: Boolean = false
res32: Boolean = false
res33: Boolean = true
java.lang.Error: Nothing
```

What we're doing here, is the following:
- We first check if the list is empty, and return `Nil` if it is.
- We then check if the list has one non-empty element `y` followed by an empty element `Nil`. In that case, we only check the truth of the element `y`.
- Finally, we check for the list with at least two non-empty elements `y :: ys`. We must note that `ys` is not necessarily a non-empty element. In fact, it can be non-empty, but the condition above checks for that specific case; if we remove the pattern `y :: Nil`, the evaluation will always result in `Error("Nothing")`, since, in the end, an empty list is guaranteed to always be returned as the last argument in our evaluation.

In this implementation, we're leveraging the use of the logical operator `&` (*if there is any `Boolean` value that evaluates to `false`, the resulting value will be false, no matter what*)

We can also perform this same implementation by using a non-recursive option, where we combine `map` & `flatten`; the idea about functional programming, is that there are always many different ways to tackle a problem; it's up to us to decide which implementation is the most efficient, less resource-intensive, and more clean in terms of syntaxis.

## 13. exists
The `exists` method is the `OR` version of the above; it evaluates all elements, and returns `true` if at least one element complies with the provided predicate.

In fact, if we look at the function signature, it's exactly the same as `forall`. The generic function signature for `exists` is the following:

##### **Code**
```Scala
def exists[A](list: List[A])(predicate: A => Boolean): Boolean
```

Where:
- `exists` is a higher-order function in Scala.
- It takes a list of elements of type `A` and a predicate function `predicate`.
- The predicate function takes an element of type `A` and returns a Boolean value.
- `exists` applies the predicate function to each element in the list and checks if the predicate holds true for at least one element.
- It returns a `Boolean` value indicating whether the predicate holds true for at least one element in the list.
- The return type is `Boolean`. It will be `true` if the predicate holds true for at least one element, and `false` if the predicate holds false for all elements.

Now that we have the recursive implementation for `forall`, it's fairly straightforward to define one for `exists`:

##### **Code**
```Scala
// Implementing exists using a recursive function
def compliesOne(xs: List[Int]): Boolean = xs match
    case Nil => throw Error("Nothing")
    case y :: Nil => (y % 2 == 0)
    case y :: ys => (y % 2 == 0) | compliesOne(ys)

compliesOne(List(1, 3, 5, 7, 9))
compliesOne(List(2, 2, 4, 6))
compliesOne(List(1, 2, 2))
compliesOne(List(1))
compliesOne(List(0))
compliesOne(List())
```

##### **Output**
```
res35: Boolean = false
res36: Boolean = true
res37: Boolean = true
res38: Boolean = false
res39: Boolean = true
java.lang.Error: Nothing
```

We can see that the only modification is the logical operator; we change `&` for `|`.

Similar to the example above, we can check if a list contains at least one even integer:

##### **Code**
```Scala
val myList20: List[Int] = List(1, 3, 5, 7, 9)
val myList21: List[Int] = List(2, 4, 6, 8)

myList20.exists(x => x % 2 == 0)
myList21.exists(x => x % 2 == 0)
``` 

##### **Output**
```
res40: Boolean = false
res41: Boolean = true
```

## 14. groupBy
The `groupBy` method partitions a collection into a `HashMap` according to some discriminator function. This function can, for example, evaluate if a given subset of the list contains an even number, and group by different columns depending on the truth of the evaluation.

The generic function signature for `groupBy` is the following:

##### **Code**
```Scala
def groupBy[A, B](list: List[A])(keyFunction: A => B): Map[B, List[A]]
```

Where:
- `groupBy` is a higher-order function in Scala.
- It takes a list of elements of type `A` and a key function `keyFunction`.
- The key function maps each element of type `A` to a key of type `B`.
- `groupBy` groups the elements of the list based on the keys obtained from the key function.
- It returns a `Map` where the keys are of type `B`, and the values are lists of elements of type `A` that have the same key.
- The return type is `Map[B, List[A]]`, representing a mapping from keys of type `B` to lists of elements of type `A`.

This one might seem slightly more confusing; we can illustrate how it works with a simple use case:

Let us define a list that contains odd & even numbers. We want to group our list into two different mappings: the first one will contain the even numbers, and the second one the odd ones:

##### **Code**
```Scala
// Define a discriminator function
def groupNumbers(x: Int): Int =
    if (x % 2 == 0) 1
    else 2

val myList22: List[Int] = List(1, 2, 3, 4, 5, 6, 7, 8, 9)

// Group by using discriminator function
myList22.groupBy(groupNumbers)
```

##### **Output**
```
res42: Map[Int, List[Int]] = HashMap(1 -> List(2, 4, 6, 8), 2 -> List(1, 3, 5, 7, 9))
```

As we can see, the result is a HashMap structure that maps each key with its corresponding subset, based on the discriminator function `groupNumbers`.

As we can imagine, this method is extremely powerful, since it lets us compose infinitely complex discriminators, while returning the very fast `HashMap` data structure as result.

Of course, keys can be of different types than the grouped subsets:

##### **Code**
```Scala
// Define a discriminator function now returning a string as key
def groupNumbersStringKey(x: Int): String =
    if (x % 2 == 0) "Even"
    else "Odd"

// Group by using discriminator function
myList22.groupBy(groupNumbersStringKey)
```

##### **Output**
```
res43: Map[String, List[Int]] = HashMap(Odd -> List(1, 3, 5, 7, 9), Even -> List(2, 4, 6, 8))
```

If we want to assign our `groupBy` result to a variable, and then index our `HashMap` structure to return a given subset, we can do so:

##### **Code**
```Scala
// Group by using discriminator function
val groupedInts = myList22.groupBy(groupNumbersStringKey)
groupedInts("Odd")
```

##### **Output**
```
res43: List[Int] = List(1, 3, 5, 7, 9)
```

## 15. sort

The generic function signature for `scanRight` is the following:

##### **Code**
```Scala
def scanRight[A, B](list: List[A])(initialValue: B)(accumulator: (A, B) => B): List[B]
```

Where:

## 16. sortBy


The generic function signature for `scanRight` is the following:

##### **Code**
```Scala
def scanRight[A, B](list: List[A])(initialValue: B)(accumulator: (A, B) => B): List[B]
```

Where:

## 17. sortWith


The generic function signature for `scanRight` is the following:

##### **Code**
```Scala
def scanRight[A, B](list: List[A])(initialValue: B)(accumulator: (A, B) => B): List[B]
```

Where:

## 18. minBy


The generic function signature for `scanRight` is the following:

##### **Code**
```Scala
def scanRight[A, B](list: List[A])(initialValue: B)(accumulator: (A, B) => B): List[B]
```

Where:

## 19. maxBy


The generic function signature for `scanRight` is the following:

##### **Code**
```Scala
def scanRight[A, B](list: List[A])(initialValue: B)(accumulator: (A, B) => B): List[B]
```

Where:

---

# Creating a generic higher-order collection function
Up until now, we've worked with fixed types in our recursive function declarations, meaning the function expects, for example, a list of integer values, a list of chars, or a list of strings, etc.

The power of defining our own methods is that we can abstract a specific type function to a generic type. This is achieved via the `T` parameter declaration.

Let us explore a case where we have a list of unknown type, and we'd like to perform the same operation, without having to explicitly declare our list as `List[Int]`, for example:

##### **Code**
```Scala
def genericMap[T](xs: List[T], f: T => T): List[T] = xs match
    case Nil => Nil
    case y :: ys => f(y) :: genericMap(ys, f)

val myListInts: List[Int] = List(1, 2, 3, 4)
val myListStrings: List[String] = List("1", "2", "3", "4")
val myListDoubles: List[Double] = List(1.0, 2.0, 3.0, 4.0)

genericMap(myListInts, x => x * 2)
genericMap(myListStrings, x => x * 2)
genericMap(myListDoubles, x => x * 2)
```

##### **Output**
```
res24: List[Int] = List(2, 4, 6, 8)
res25: List[String] = List(11, 22, 33, 44)
res26: List[Double] = List(2.0, 4.0, 6.0, 8.0)
```

What we're doing, is specifying our function in terms of a type parameter or type variable denoted by `T`. This parameter acts as a placeholder for a specific type that will be determined when the function is invoked or the generic class is instantiated, and is what lets us declare generic functions that work with different types.

However, there's a tradeoff; we need to make sure that the `map` function we're defining, in this case `x * 2`, is compatible with the types we're specifying. If this is not the case, we'll need to define separate methods depending on the type used; this can be achieved via additional pattern matching, for example.

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