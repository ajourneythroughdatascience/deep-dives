// ---------------------
// Map
// ---------------------

// A simple function
val myList1: List[Int] = List(1, 2, 3, 4, 5)
myList1.map(x => x * x)

// A more elaborate function
def applyFun(x: Int): Int =
    if (x % 2 == 0) x * x
    else x

myList1.map(applyFun)

// A generic method
def genericMethod[T](x: T) = x match
    case x:Int => x * x
    case x:String => s"${x} * ${x}"

val myList2 = List(1, 2, "3")

myList2.map(genericMethod)

// A method matching a list of lists
def matchMultiple(xs: List[Int]): Int = xs match
    case Nil => 0
    case y :: ys => y + matchMultiple(ys)

val myList3: List[List[Int]] = List(List(1, 2, 3), List(4, 5, 6), List(7, 8, 9))

myList3.map(matchMultiple)

// ---------------------
// flatMap
// ---------------------

// Calculate square of nested elements using a recursive function
def squaredSum(xs: List[List[Int]]): List[Int] = xs match
    case Nil => Nil
    case y :: ys => y.map(x => x * x) ++ squaredSum(ys)

val myList4: List[List[Int]] = List(List(1, 2, 3), List(4, 5, 6))

squaredSum(myList4)

// Calculate square of nested elements using flatMap & map
myList4.flatMap(x => x.map(x => x * x))

// Return the collection without any operation
myList4.flatMap(x => x)


// ---------------------
// Chaining functions
// ---------------------

// map reduce
def mapReduce(xs: List[List[Int]]): List[Int] = xs match
    case Nil => Nil
    case y :: ys => y.map(x => x * x).reduce(_ + _) :: mapReduce(ys)

val myList5: List[List[Int]] = List(List(1, 2, 3), List(4, 5, 6), List(7, 8, 9))

mapReduce(myList5)

// flat map reduce
def flatMapReduce(xs: List[List[Int]]): List[Int] = xs match
    case Nil => Nil
    case y :: ys => (y.map(x => x * x).reduce(_ + _) :: mapReduce(ys))

val myList6: List[List[Int]] = List(List(1, 2, 3), List(4, 5, 6), List(7, 8, 9))

flatMapReduce(myList5)