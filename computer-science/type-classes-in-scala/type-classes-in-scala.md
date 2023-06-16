<article class="first">
  <div class="title">
    <h1>Type Classes in Scala</h1>
  </div>
</article>

---

[![made-with badge](https://img.shields.io/static/v1?label=Made%20with&message=Obsidian&color=7d5bed&logo=obsidian&labelColor=1a1a1a&style=flat)](https://obsidian.md/)

[![type](https://img.shields.io/static/v1?label=Type&message=deep-dive&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAi0lEQVRIS+2WMQ7AIAhF/UNXrtP7rz2OYxeqTWxMTBUSxQVXfnzyQQKC8YExL7zAGCNbgIkIsIKVhBw4vbR7unR6Gp0LvwxXd2v+EvkdDpxWXpWlRTyi9/pABRyBJHEHSlxSadxSlV0SsVsqcUml2W/pynWxnsXNisHMRxrCl8qvH3ECnQDuOmy+0zwB4WNxmUKgwwAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/deep-dives/) [![category](https://img.shields.io/static/v1?label=Category&message=computer-science&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAB9UlEQVRIS6VWMU7DQBDkDAQEdrAoCISCAomCL1DxC95Azy9oeQS/oOIHVFAgREFoCHGCRSzZzEU+63LZ9W6CO/vudmZ2d9Zn1pTPaDSqut2usduHw+FpFEUv7t1fk8LNAkiPDWj3+ADuTPjNvXMxWwGzLCuqqtqwh5MkiY0xEwfOAfrEKFAWUBO4DZQDXgCEqjuouvbZUanUrocpngMMVUkKtKC+WhFQUudAUd8r1PkepJ/w7Tysn4uzkNJlascF9WOASAki6w0xrn19b3Gpps5y3kRfJADPZgr9gJSP0EgDHDiQ/Mp50PfxAmDtuQhsZmb/z0OVhwSkmGrSGp5bGRDp3EFaJ5JaiahdZ2vYNj/JkWVMgW7sgNw2yOW+99gacp7TeFE72OcUrgo4Ho93+/3+D5T9QmGHm0BNSnHgMI7jj9Ai2tElZGCK9S3S+GA4BcNNydBaIuEstu/iLJWCa+pLDm+Nz+xQAsBenucnRVG8asFq0s/Yf9YoVAI21wyn3N4I7M1A8ijWHwB42XrFqIO9YfMRlVqqyXC5ukED3nIEVJcoBXv1lmWa5gIpeeQioyTWVj1uXf0DpgKUZbmfpunXKnVnU9rWDKiTHRSDNkDu36iqIQK/Q+mxU8sBYniL/1EVoJ9Wqwo/5x6Cf9YKv6Em1XbNH5bGfSwvuRe1AAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/categories/computer-science/) [![technologies](https://img.shields.io/static/v1?label=Technologies&message=Scala&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAACXBIWXMAAAsTAAALEwEAmpwYAAAA1klEQVR4nM2RMW7CUBBEnUikIQUIlBJxrrQgJG7ABRBnoUkaWhpoUgWJlgNYbvz/G1dUi1ayoy87rpOtVrszs6OdLPtXlef5UNJXjHHcCwohjMzsKZ3FGN+Bq/e+c0xHGfiWtEznkg6SNnW/dIxjs0YJ2AMnM3tJSFPgHkKY17gBcAQ+zOw5A3aSbsCkdW0NnNOZY2rstpcInJ3cS/SzwGdqtSzLmdusquqtIXWsehVF8QpcJK1qmxt/TMv6wjE/z0leP27i8Ag8inT/axxtAQ+9o/zn9QD3JOiyTjnQEQAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/technologies/) [![website article](https://img.shields.io/static/v1?label=Website&message=Post%20Link&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAACXBIWXMAAAsTAAALEwEAmpwYAAAB+ElEQVR4nO2VOYgUURCGR/BAI4MN1EwjI89EMDYQvNBNNNlcE0VBUdlUUSMjj2BF2UDRePDAwGzNF2GNPIYd8Hjv/6YnEHSf/FIDPTJiu4nJFBTd1Kv6/nrVBd1q/S8DJiU9AmaBm5LOSjoATPwDY0LSQUnnzDArmJOjkqclvQceSHohaR6oJC1JeiPprqT9pZSVg5pSyirH4sw5S1EzbwZwP5jTIwWBdj1meEppZ6/XOyXpCdCX9Am4Fv45Yo+Bk1VV7ag3FNz2kKC7yznvHiX4u3U6nXU55xPAW7vfHfvLmNtmW8NaFux67k0Ea03esTfJJQTj23bHgiNtPNK6jZem3Wpg46Wp23hp2q0GNl6axksjaRGYkXRF0mnHq6ra2HSk/X5/k6RDks6YEazFPwnuBS5KuirptqTnkj4CJZ4zwNFSytqBoP/2wDHgXi33A/BM0i2zzDR7SBC4LGlPr9fb5huVUlYMus45b5E0FYJfgQS8C8/Al7jJVEpp86DODLPMNDs0up7xXBQZVKLLb8CCpIfA+ZzzvpTS+lLKGuAI8DT8cClltc+c49yoWQjGL140ao25oW8QXW1IKe3KOR8Hbkh66ZtI+i7plaG+iR244JjP3HDkXnetGWbVp9XYopHtHgvwWtIPu9+BSx7bssBNDdhqX07xT/Jbz1SBBDGHAAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/deep-dives/type-classes-in-scala/)

Formally, a type class is a type system construct that supports ad hoc polymorphism. This is achieved by adding constraints to type variables in parametrically polymorphic types. In simpler terms, a type class is a construct that lets us add constraints to generic functions.

Type classes are useful when we have generic methods that may accept parameters of different types, and/or return results of different types, and would like to perform some kind of operation to our parameters without having to worry about explicitly defining the type-specific action ourselves. These constructs are widely used in type-drive programming, since they provide flexibility, while keeping our implementations safe.

In this Deep Dive, we'll discuss what type classes are, why are they useful, how are they implemented, and finally, go over some practical examples in order to solidify the theory discussed.

We'll be using Scala worksheets which can be found in the [Deep Dive Repo](https://github.com/pabloagn/blog/tree/master/computer-science/type-classes-in-scala).

---

# Table of Contents
- What are type classes?]()
- What are implicits?]()
- Type classes & implicits together]()
	- Defining a type class]()
	- Ad-hoc polymorphism]()
- Some practical examples]()
	- Requesting data from an external API]()
	- Aaa]()
- [Conclusions](#conclusions)
- [References](#references)
- [Copyright](#copyright)

---

# What are type classes?
It's easier to define type classes if we first define a problem we're trying to solve.

Let us imagine we have multiple integer lists, and would like to define a method that adds all the elements inside the list, and returns the result as an integer value:

##### **Code**
```Scala
// Defining a type-specific function
def addIntegers(xs: List[Int]): Int = {
    xs.reduceLeft(_ + _)
}

val myListIntegers: List[Int] = List(1, 2, 3, 4, 5, 6, 7, 8, 9)

addIntegers(myListIntegers)
```

##### **Output**
```
res0: Int = 45
```

This is a very straight-forward method, where, in one line, we define an operation that will add all the elements of our list, and return the required value.

The problem is that this is not a generic function, meaning this will only work with lists of integer values. We can confirm this by trying to perform the same operation with a list of strings:

##### **Code**
```Scala
val myListStrings: List[String] = List("1", "2", "3", "4", "5", "6", "7", "8", "9")

addIntegers(myListStrings)
```

And as expected, we get an incorrect type result:

##### **Output**
```
Found:    (MdocApp.this.myListStrings : List[String])
Required: List[Int]
```

We can solve this problem by declaring a generic method that expects a parameter of unknown type. This method would have a signature as such:

##### **Code**
```Scala
addGeneric[T](xs: List[T]): T
```

Where:
- The type `T` signifies any possible type under our "*definition*" of what can eb computed as a sum of elements.

But, wait a minute, how are we to implement this function? How can we tell the Scala compiler that, whenever we send a list of integers, it should compute the addition, but whenever we send a list of strings, it should concatenate the elements instead?

Well, here's where type classes come in handy, but first, we have to take a look at implicits.

---

# What are implicits?
Implicits are a very powerful concept in Scala; they let the compiler **infer** about certain value, based on its type. This concept is a little confusing, so let us explain it with yet another example.

Let us imagine we have a very powerful function that computes the square of a given number:

##### **Code**
```Scala
// Defining implicits
def myExplicitMethod(x: Int): Int = 
    x * x

myExplicitMethod(7)
```

As expected, we get the square of 7:

##### **Output**
```
res0: Int = 49
```

But what happens when we slightly change this function by adding the `implicit` keyword to one of our arguments?

##### **Code**
```Scala
def myInferringMethod(implicit x: Int): Int = 
    x * x
```

Now, when we call our function, Scala will try to find a parameter that matches the type of the input argument in our `myInferringMethod` function, given that we also define an `implicit` variable alongside.

##### **Code**
```Scala
def myInferringMethod(implicit x: Int): Int = 
    x * x

implicit val myInt1: Int = 7

myInferringMethod
```

##### **Output**
```
res1: Int = 49
```

So, we did not need to call our function with an argument explicitly; the compiler noticed that we declared an implicit variable matching the type of our argument's signature, and used that as input.

Of course, if we declare multiple implicit variables with the same type, Scala's compiler will complain, telling us that what we're doing is resulting in an ambiguous evaluation; the compiler doesn't know which value to use for the implicit call.

This is not super useful when dealing with simple functions and variables. However, we can hopefully start to see the confection between using type classes and implicits together.

---

# Type classes & implicits together
If we recall from our last examples, we have the following:
- A generic function that accepts a list of elements of type `T` as argument.
- The need to add those elements, depending on their type.
- The possibility to use the `implicit` keyword to let the compiler infer which value to use.

Let us start by defining a `trait` that includes all the possible operations that can be done with the types that we're looking to implement.

## 1. Defining a type class
Type classes are nothing more than traits that have one or more implicit method definitions inside. We want to define a `trait` that extends the functionality of our original sum function in a safe way, meaning we want to delimit the element types we can accept, and have ready a well-defined method for each case:

##### **Code**
```Scala
trait SumOfLists[T]:
    def sumElements(xs: List[T]): T

implicit object SumOfInts extends SumOfLists[Int]:
    override def sumElements(xs: List[Int]): Int = xs.reduceLeft(_ + _)

implicit object SumOfFloats extends SumOfLists[Double]:
    override def sumElements(xs: List[Double]): Double = xs.reduceLeft(_ + _)
implicit object SumOfStrings extends SumOfLists[String]:
    override def sumElements(xs: List[String]): String = xs.mkString("")
```

## 2. Ad-hoc polymorphism
Ad-hoc polymorphism is the fruit of type classes used in functions where we have implicit arguments. This might sound unintelligible, but it's actually not that hard once we include an example. Continuing from our sum function, we would now want to redesign it to accept the traits we just declared; this will finally create a truly generic function, but with proper defined methods for each type case. And the best of all, is that it will be dynamic, meaning the compiler will decide which method to use, depending on the type we throw as argument.

This is known as [ad-hoc polymorphism](https://en.wikipedia.org/wiki/Ad_hoc_polymorphism). Formally, we can define it as a programming concept used to describe functions with the same name that are executed differently, depending on the variable or argument type. It is also referred to as “*function overloading*” or “*method overloading*".

Once we have our trait, we can define a polymorphic generic function:

##### **Code**
```Scala
def addGeneric[T](xs: List[T])(implicit addElements: SumOfLists[T]): T = 
    addElements.sumElements(xs)
```

Note that we don't need to specify any type whatsoever, except for `T`; the compiler handles the type inference for us, so that when we call our function using lists with elements of different types, we get the result we expect:

##### **Code**
```Scala
val myListInts: List[Int] = List(1, 2, 3, 4, 5, 6)
val myListFloats: List[Double] = List(1.1, 2.2, 3.3, 4.4, 5.5, 6.6)
val myListStrings: List[String] = List("1", "2", "3", "4", "5", "6", "7", "8", "9")

addGeneric(myListInts)
addGeneric(myListFloats)
addGeneric(myListStrings)
```

##### **Output**
```
res3: Int = 21
res4: Double = 23.1
res5: String = 123456789
```

Also, note that this implementation is safe, since, if the compiler is not able to find an implicit matching the types of the elements inside the list, it will throw an error at compile time. In short, we have full control of what can and cannot be done inside our defined method:

##### **Code**
```Scala
addGeneric(List(true, true, false))
```

##### **Output**
```
No given instance of type MdocApp.this.SumOfLists[Boolean] was found for parameter addElements of method addGeneric in class MdocApp
```

This is horrible, right? So much work for a simple flexible function. Well, this is the price we have to pay when using strongly typed languages. The rules are rigorous, and make our code much more efficient in terms of execution and type safety, but we need to declare things in a different way that we would in other languages such as Python, JavaScript, etc.

---

# Some practical examples
Now that we have understood the very basics of type classes, we can proceed with some simple examples that will hopefully transmit why these constructs are extremely valuable when working with a strong statically-typed language like Scala.

## 1. Requesting data from an external API
Sometimes we're working with external APIs, and stumble upon poorly-documented ones, where we don't fully know the return type of the object requested. If we're working with strong statically-typed languages such as Scala, this is our worst nightmare, since one simple misalignment can complete break our program.

We can solve this by using a type class that acts according to the object type that we're getting. But first, we have to ask ourselves, how can our external data be structured? What data structures could be used to transfer the data through this mysterious API?

Well, below are some ideas:
- List
	- A list of values of the same type, but we can have multiple lists of multiple types.
- Array
	- Same as with lists
- Enum
	- Can have multiple different types. 
- Map
	- Can have keys associated with the values.

Great. So now we have an infinite amount of options to choose from, and this will take forever to write. The best approach here is to get at least some information of our object, and try to build from there.

For the sake of this example, let us imagine that the developers of this external API actually provided some hints of the output structure. They said it might be one of the following:
- A `Map` of key value pairs, where each key is of type `String`, and each value is an object of type `Array` with the following possible element types:
	- `Int`
	- `String`
	- `Double`
- A list of lists (*up to 2 levels of depth*), where each nested list can contain elements of the following type:
	- `Int`
	- `String`

So now our options are narrowed down; we know that we are expecting structures as such: 

##### **Code**
```Scala
// Example data structures
val exampleStructureOne = List(
    List(7, 14, 21, 28, 35),
    List(5, 1, 78, 43, 21)
    )

val exampleStructureTwo = List(
    List("Janusz", "Martha", "Emma"),
    List("Juarez", "Joan", "Dillon", "Leo")
)

val exampleStructureThree = Map(
    "Item 1" -> List(1, 2, 3, 4, 5),
    "Item 2" -> List(1, 2, 3, 4, 5),
    "Item 3" -> List(1, 2, 3, 4, 5),
    "Item 4" -> List(1, 2, 3, 4, 5),
    "Item 5" -> List(1, 2, 3, 4, 5)
)

val exampleStructureFour = Map(
    "Item 1" -> List("Virginia", "Woolf"),
    "Item 2" -> List("James", "Baldwin"),
    "Item 3" -> List("Thomas", "Hardy"),
    "Item 4" -> List("Clarice", "Lispector"),
    "Item 5" -> List("Edward", "Gibbon")
)
```

This sounds fairly reasonable. So, what we need to worry about is how are we destructuring these possibilities, and how are we letting the compiler know which possibility to expect?

Well, we can start with a type class for starters:

##### **Code**
```Scala
// Define a type class
trait parseData[T, S]:
    def extractData(obj: T): S

implicit object parseListInt extends parseData[List[List[Int]], List[Int]]:
    override def extractData(obj: List[List[Int]]): List[Int] = obj.flatten(x => x)

implicit object parseListString extends parseData[List[List[String]], List[String]]:
    override def extractData(obj: List[List[String]]): List[String] = obj.flatten(x => x)

implicit object parseMapInt extends parseData[Map[String, List[Int]], List[Int]]:
    override def extractData(obj: Map[String, List[Int]]): List[Int] = obj.values.flatMap(x => x).toList

implicit object parseMapString extends parseData[Map[String, List[String]], List[String]]:
    override def extractData(obj: Map[String, List[String]]): List[String] = obj.values.flatMap(x => x).toList
```

Here, we're covering four possibilities:
- `ListInt`
- `ListString`
- `MapInt`
- `MapString`

And we're flattening the structures so that we get a one-dimensional `List` object in return. So, the only thing left is to declare our extractor method: 

##### **Code**
```Scala
def getExtData[T, S](r: T)(implicit extractMethod: parseData[T, S]): S = 
    extractMethod.extractData(r)
```

And now, we call it with our example structures:

##### **Code**
```Scala
getExtData(exampleStructureOne)
getExtData(exampleStructureTwo)
getExtData(exampleStructureThree)
getExtData(exampleStructureFour)
```

##### **Output**
```
res6: List[Int] = List(7, 14, 21, 28, 35, 5, 1, 78, 43, 21)
res7: List[String] = List(Janusz, Martha, Emma, Juarez, Joan, Dillon, Leo)
res8: List[Int] = List(1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
res9: List[String] = List(Edward, Gibbon, Virginia, Woolf, Clarice, Lispector, Thomas, Hardy, James, Baldwin)
```

We can imagine that this precise signature (*that of the trait*) would probably not be the best approach if we're trying to extract data from an API return object, since we're effectively loosing any dimensionality or structuring that the API provider organized for us.

The ideal approach here, would be to build another Map, for example, containing all homogenized structures (*instead of a list of values*), but the point is made; this construct is extremely versatile and powerful, and most importantly, it's safe.

## 2. Aaa
Aaa

---

# References
- A
- A
- A
- A

---

# Copyright
Pablo Aguirre, Creative Commons Attribution 4.0 International, All Rights Reserved.