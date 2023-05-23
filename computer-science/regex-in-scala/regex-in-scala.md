<article class="first">
  <div class="title">
    <h1>RegEx in Scala</h1>
  </div>
</article>

---

[![made-with badge](https://img.shields.io/static/v1?label=Made%20with&message=Obsidian&color=7d5bed&logo=obsidian&labelColor=1a1a1a&style=flat)](https://obsidian.md/)

[![type](https://img.shields.io/static/v1?label=Type&message=deep-dive&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAi0lEQVRIS+2WMQ7AIAhF/UNXrtP7rz2OYxeqTWxMTBUSxQVXfnzyQQKC8YExL7zAGCNbgIkIsIKVhBw4vbR7unR6Gp0LvwxXd2v+EvkdDpxWXpWlRTyi9/pABRyBJHEHSlxSadxSlV0SsVsqcUml2W/pynWxnsXNisHMRxrCl8qvH3ECnQDuOmy+0zwB4WNxmUKgwwAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/deep-dives/) [![category](https://img.shields.io/static/v1?label=Category&message=computer-science&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAB9UlEQVRIS6VWMU7DQBDkDAQEdrAoCISCAomCL1DxC95Azy9oeQS/oOIHVFAgREFoCHGCRSzZzEU+63LZ9W6CO/vudmZ2d9Zn1pTPaDSqut2usduHw+FpFEUv7t1fk8LNAkiPDWj3+ADuTPjNvXMxWwGzLCuqqtqwh5MkiY0xEwfOAfrEKFAWUBO4DZQDXgCEqjuouvbZUanUrocpngMMVUkKtKC+WhFQUudAUd8r1PkepJ/w7Tysn4uzkNJlascF9WOASAki6w0xrn19b3Gpps5y3kRfJADPZgr9gJSP0EgDHDiQ/Mp50PfxAmDtuQhsZmb/z0OVhwSkmGrSGp5bGRDp3EFaJ5JaiahdZ2vYNj/JkWVMgW7sgNw2yOW+99gacp7TeFE72OcUrgo4Ho93+/3+D5T9QmGHm0BNSnHgMI7jj9Ai2tElZGCK9S3S+GA4BcNNydBaIuEstu/iLJWCa+pLDm+Nz+xQAsBenucnRVG8asFq0s/Yf9YoVAI21wyn3N4I7M1A8ijWHwB42XrFqIO9YfMRlVqqyXC5ukED3nIEVJcoBXv1lmWa5gIpeeQioyTWVj1uXf0DpgKUZbmfpunXKnVnU9rWDKiTHRSDNkDu36iqIQK/Q+mxU8sBYniL/1EVoJ9Wqwo/5x6Cf9YKv6Em1XbNH5bGfSwvuRe1AAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/categories/computer-science/) [![technologies](https://img.shields.io/static/v1?label=Technologies&message=Scala,%20RegEx,%20%20VS%20Code,%20PowerShell%207&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAACXBIWXMAAAsTAAALEwEAmpwYAAAA1klEQVR4nM2RMW7CUBBEnUikIQUIlBJxrrQgJG7ABRBnoUkaWhpoUgWJlgNYbvz/G1dUi1ayoy87rpOtVrszs6OdLPtXlef5UNJXjHHcCwohjMzsKZ3FGN+Bq/e+c0xHGfiWtEznkg6SNnW/dIxjs0YJ2AMnM3tJSFPgHkKY17gBcAQ+zOw5A3aSbsCkdW0NnNOZY2rstpcInJ3cS/SzwGdqtSzLmdusquqtIXWsehVF8QpcJK1qmxt/TMv6wjE/z0leP27i8Ag8inT/axxtAQ+9o/zn9QD3JOiyTjnQEQAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/technologies/) [![website article](https://img.shields.io/static/v1?label=Website&message=Post%20Link&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAACXBIWXMAAAsTAAALEwEAmpwYAAAB+ElEQVR4nO2VOYgUURCGR/BAI4MN1EwjI89EMDYQvNBNNNlcE0VBUdlUUSMjj2BF2UDRePDAwGzNF2GNPIYd8Hjv/6YnEHSf/FIDPTJiu4nJFBTd1Kv6/nrVBd1q/S8DJiU9AmaBm5LOSjoATPwDY0LSQUnnzDArmJOjkqclvQceSHohaR6oJC1JeiPprqT9pZSVg5pSyirH4sw5S1EzbwZwP5jTIwWBdj1meEppZ6/XOyXpCdCX9Am4Fv45Yo+Bk1VV7ag3FNz2kKC7yznvHiX4u3U6nXU55xPAW7vfHfvLmNtmW8NaFux67k0Ea03esTfJJQTj23bHgiNtPNK6jZem3Wpg46Wp23hp2q0GNl6axksjaRGYkXRF0mnHq6ra2HSk/X5/k6RDks6YEazFPwnuBS5KuirptqTnkj4CJZ4zwNFSytqBoP/2wDHgXi33A/BM0i2zzDR7SBC4LGlPr9fb5huVUlYMus45b5E0FYJfgQS8C8/Al7jJVEpp86DODLPMNDs0up7xXBQZVKLLb8CCpIfA+ZzzvpTS+lLKGuAI8DT8cClltc+c49yoWQjGL140ao25oW8QXW1IKe3KOR8Hbkh66ZtI+i7plaG+iR244JjP3HDkXnetGWbVp9XYopHtHgvwWtIPu9+BSx7bssBNDdhqX07xT/Jbz1SBBDGHAAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/deep-dives/regex-in-scala/)

Writing code can be as simple as importing the required libraries, declaring our variables, functions, and classes as required, including some docstrings here and there, some additional comments, executing, and we're done. While we're at it, let's skip the function & class part and drop everything as is. Even better, let's also save some lines by stripping our file from all comments.

In this Deep Dive, we'll

We'll be using Scala code which can be found in the [Deep Dive Repo](https://github.com/pabloagn/deep-dives/tree/master/computer-science/regex-in-scala).

---

# Table of Contents
- A brief introduction
	- RegEx
	- Scala
- What to expect
	- RegEx
	- Scala
	- Supporting technologies
- Setting up our environment
	- Creating a project
	- 
- An introduction to the scala.util.matching.Regex class
- Performing matches
- Capturing groups
- Advanced concepts
- Error handling with RegEx
- A practical example
	- A
	- B
	- C
- [Conclusions](#conclusions)
- [References](#references)
- [Copyright](#copyright)

---

# A brief introduction

## 1. RegEx


## 2. Scala

---

# What to expect
RegEx & Scala are not the most beginner-friendly languages out there. However, we'll make this as simple and clear as possible, so that, given that we already have a basic understanding of the both, we can glue them together, making an elegant combination of performance & safety with pure power.

## 1. RegEx
In this segment, we'll study a set of regular expressions which will help us illustrate examples; we will start with easier examples, and build our way up to a practical example involving more advanced concepts. Because of this, at least general knowledge of RegEx is recommended. If we're first approaching RegEx, we can check out [An Introduction to RegEx](https://pabloagn.com/blog/an-introduction-to-regex/), which provides a comprehensive introduction to regular expressions including the POSIX universal flavor as well as some Python hands-on examples.

## 2. Scala
Although we'll not be using advanced Scala features for this segment, at least a basic knowledge of Scala is recommended, since it will not be provided here. For that, we can check out [Scala 3 for Beginners](https://pabloagn.com/blog/scala-3-for-beginners/), which provides a comprehensive introduction to the language and its main features.

## 3. Supporting technologies
Additionally, we'll make use of two other technologies:
- PowerShell 7
- VS Code
- VS Code Extensions
- RegEx101

These will also not be covered in detail, since that's out of the scope of this segment. PowerShell 7 will really only be used to set up our project (*we'll not be executing RegEx here*). For the other ones (*VS Code, RegEx101*), if we're not yet familiar with either of these tools, we have two options:
- **Look for a quick introduction:** These are very simple tools that will boost our productivity whenever writing RegEx. Below are some resources for getting to know them more intimately:
	- **[Getting started with Visual Studio Code](https://code.visualstudio.com/docs/introvideos/basics):** Provides the basics for setting up the tool and understanding its main functionalities.
	- **[Regex101 - The Ultimate Tool for Regular Expressions, Federico Terzi](https://www.youtube.com/watch?v=79WVN-vGllU):** A great tutorial for getting started with RegEx101
- **Use alternative tools:** Of course, these are just two options (*one IDE and one debugger*), but we're free to use whatever works best.

---

# Setting up our environment

## 1. Setting up a RegEx101 session
There's no such thing as a "RegEx101 session"; what we're doing here is simply creating a new document that will serve as playground whenever we want to debug expressions quickly and safely, instead of doing it inside our IDE when we're writing the actual code.

## 2. Creating a Scala project
The next step is to create a new Scala project. For this, we'll follow the steps below:


We'll first create a new folder that will contain our project, as well as other materials such as input files:

##### **Code**
```PowerShell
New-Item -ItemType Directory -Path Test regex-in-scala
cd regex-in-scala
```

Next, we'll create our actual project using `sbt`:

##### **Code**
```PowerShell
sbt new scala/scala3.g8
```

With the name `regex-in-scala`.

We'll verify that our project was correctly generated:

##### **Code**
```PowerShell
cd regex-in-scala
dir
```

We should see something like this:

##### **Output**
```
Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d----          05/22/23     18:38                project
d----          05/22/23     18:38                src
-a---          05/22/23     18:38            342 .gitignore
-a---          05/22/23     18:38            271 build.sbt
-a---          05/22/23     18:38            346 README.md
```

Great! Now, we can open VS Code in the current (*`root`*) project directory, and import the sbt build when prompted:

D002A042_01.png

###### *Figure 1: Importing Main Build to Project*

The `sbt` template we used already includes a `Main.scala` file, which we'll use to write our simple application. However, we'll also create a new worksheet, which we'll use to test expressions on-the-fly:

##### **Code**
```PowerShell
New-Item -ItemType Directory -Path .\src\worksheets
New-Item -ItemType File -Path .\src\worksheets\regex_test.worksheet.sc
```

## 3. Including required dependencies
We'll only be using one dependency for our project called [Apache Commons CSV](https://commons.apache.org/proper/commons-csv/) for reading CSV files. To include the dependency, we can open our `build.sbt` file, and include the following:

##### **Code**
```Scala
libraryDependencies += "org.apache.commons" % "commons-csv" % "1.8"
```

So that our complete `build.sbt` file should look something like such:

##### **Code**
```Scala
val scala3Version = "3.2.2"

lazy val root = project
  .in(file("."))
  .settings(
    name := "regex-in-scala",
    version := "0.1.0-SNAPSHOT",

    scalaVersion := scala3Version,

    libraryDependencies += "org.scalameta" %% "munit" % "0.7.29" % Test,
    libraryDependencies += "org.apache.commons" % "commons-csv" % "1.10.0"
  )
```

The only thing that could change, are the versions of each dependency (*the latest version for `commons-csv` at the writing of this article was `1.10.0`*). We must ensure that we're using the latest version for increased compatibility; the latest versions can be consulted [here](https://commons.apache.org/proper/commons-csv/download_csv.cgi).

All the RegEx will be handled by an internal library called `scala.util.matching`, specifically the `RegEx` class provided by it.

---

# A practical example
We'll now create a very simple application that reads a csv file, and matches certain fields by using RegEx.

## 1. The raw data
For this project, we'll use three different CSV files:
- [`movies_shows.csv`](https://raw.githubusercontent.com/pabloagn/deep-dives/master/computer-science/regex-in-scala/regex-matching/utils/movies_shows.csv): A set of movies & tv shows including:
	- `Title`
	- `Type`
	- `Year`
	- `Rating`
	- `Duration`
	- `Country`
	- `Director`
- [`novels.csv`](https://raw.githubusercontent.com/pabloagn/deep-dives/master/computer-science/regex-in-scala/regex-matching/utils/novels.csv): A set of fiction novels containing:
	- `Title`
	- `Author`
	- `Year`
	- `Rating`
	- `Genre`
- [`characters.csv`](https://raw.githubusercontent.com/pabloagn/deep-dives/master/computer-science/regex-in-scala/regex-matching/utils/characters.csv): A set of characters belonging to movies, tv shows & fiction novels, containing:
	- `Name`
	- `LastName`
	- `Address`
	- `Profession`
	- `Age`
	- `EmailAddress`
	- `Phone`

Some files are more damaged than others, which is exactly what we'll investigate in this project; our task will be to find all the records that are incorrectly formatted or misspelled, by writing some regular expressions. 

## 1. Importing the required dependencies

When we created our project, a `Main.scala` file was also generated. We'll open it, and start by importing the required dependencies:

##### **Code**
```Scala
import org.apache.commons.csv._
import java.io.FileReader
import scala.util.matching.Regex
```

Where:
- A
- B
- C

## 2. Defining our main function

Then, we'll define a main function and call it `readCSV`; this function will read our target CSV file.



---


# Conclusions
We've reviewed 

---

# References
- [Introduction to Apache Commons CSV, Baeldung](https://www.baeldung.com/apache-commons-csv)
- 

---

# Copyright
Pablo Aguirre, Creative Commons Attribution 4.0 International, All Rights Reserved.