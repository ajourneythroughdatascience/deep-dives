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
- A brief introduction]()
	- RegEx]()
	- Scala]()
- What to expect]()
	- RegEx]()
	- Scala]()
	- Supporting technologies]()
- Setting up our environment]()
	- Setting up a RegEx101 session]()
	- Creating a Scala project]()
	- Including required dependencies]()
- An introduction to the Scala Regex class]()
- Performing matches]()
- Capturing groups]()
- Advanced concepts]()
- Error handling with RegEx]()
- A practical example]()
	- Creating our regular expressions]()
		- Visualizing our data]()
		- Designing our expressions]()
	- Performing tests in a Scala worksheet]()
	- Writing our application]()
		- Importing the required dependencies]()
		- Defining our functions]()
			- The main function]()
			- The readCSV file function]()
			- The matchData function]()
			- The writeData function]()
	- Running our application]()
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

# An introduction to the Scala Regex class

## Performing matches


## Capturing groups


## Advanced concepts


## Error handling with RegEx


---

# A practical example
We'll now create a very simple application that reads a csv file, and matches certain fields by using RegEx.

## 1. The raw data
For this project, we'll use one CSV file:
- [`characters.csv`](https://raw.githubusercontent.com/pabloagn/deep-dives/master/computer-science/regex-in-scala/regex-matching/utils/characters.csv): A set of characters belonging to movies, tv shows & fiction novels, containing:
	- `Name`
	- `LastName`
	- `Address`
	- `Profession`
	- `Age`
	- `EmailAddress`
	- `Phone`

Our task will be to extract all usable information from this dataset in a readable and clear format.

## 2. Creating our regular expressions
For this section, we'll use [RegEx101](https://regex101.com/), a great tool used for writing, testing & debugging regular expressions on-the-fly. 

### 2.1 Visualizing our data
If we take a look at the head of our file, we can see the following structure:

```csv
Name,LastName,Address,Profession,Age,EmailAddress,Phone
Lucifer,Morningstar,Lux, Nightclub Owner, Immortal, lucifermorningstarlux.com,123-456-7890
Ray,Shoesmith,Sydney, Criminal, 40, ray.shoesmith@underworld.com.au,234-567-890
John,Tavner,Milwaukee, Intelligence Officer, 30, john.tavnermilwaukee.gov,345-678-9012
Doron,Kavillio,Israel, Commando, 50, doron.kavillio@israel.gov,456-789-0123
Wayne,McCullough,Brockton, Teenager, 16, wayne.mcculloughbrockton.net,567-890-1234
Edmond,Dantes,Château d'If, Sailor, 25, edmond.dantes@montecristo.com,678-901-2345
Rodion,Raskolnikov,Saint Petersburg, Ex-Student, 23, raskolnikov.rodionstpetersburg.ru,789-012-3456
Anna,Karenina,Moscow, Socialite, 30, anna.karenina@moscow.society.ru,890-123-456
Gania,Ivolgin,Saint Petersburg, Civil Servant, 27, gania.ivolgin@stpetersburg.ru,901-234-5678
Pierre,Bezukhov,Moscow, Count, 32, pierre.bezukhov@moscow.gov.ru,012-345-678
Clary,Desiree,Paris,Actress,20,desiree.clary@paris.fr,-222-333
Edmond,Alexandre,Marseilles,Sailor,30,alexandre.edmond@marseilles.fr,222-333-4444
Kitty,Shcherbatsky,Moscow,Socialite,20,kitty.shcherbatskymoscow.society.ru,333-444-555
Konstantin,Levin,Russian Countryside,Farmer,35,konstantin.levincountryside.ru,444-555-6666
```

So, it appears we have:
- A first name
- A surname
- An address
- A profession
- An age  as integer number
- An email address containing different possible domains.
- A phone number containing multiple possible formats:
	- Three segments: `999-1010-1111`
	- Four segments: `1-999-888-7777`

Our task is to match entries that have valid records, meaning:
- A valid name
- A valid surname
- An address of some kind
- A valid age
- A valid email address
- A valid phone number

### 2.2 Designing our expressions
Let us start with the first name:

##### **Code**
```RegEx
^(?<first_name>[A-z]+)\, ?
```

What we're doing:
- Start at the end of the line.
- Create a named capturing group.
- Include any alphabetical character, lower or upper-case.
- Include a comma `,` separator and an optional whitespace ` `.

Now, for the second name, we do a similar approach:

##### **Code**
```RegEx
(?<last_name>[A-z]+)\, ?
```

For the address, we'll do a simplified version, since many of our characters appear to be ancient or live in slightly unusual places, so we'll have to sacrifice a little and generalize:

##### **Code**
```RegEx
(?<address>[A-zÀ-úÀ-ÿÀ-ÖØ-öø-ÿ ']+)\, ?
```

We include accented & special characters, since some of our characters may live in non-US provinces where these characters are common.

The profession is fairly simple:

##### **Code**
```RegEx
(?<profession>[A-z ]+)\, ?
```

The only thing to consider, is that we must include all alphabetic characters, but also white spaces, since the profession might be a collection of 2 or more words (*e.g., Civil Servant, Army Officer, etc.*).

Now, we can go for the age, whose only condition will be that is must be composed of an integer or be immortal. We'll also include an age limit, since we don't want people with 1000+ years of age in our database without them explicitly stating that they're immortal (*luckily for us, the immortal guys included are specified as immortal*).

##### **Code**
```RegEx
(?<age>\d+|Immortal)\, ?
```

Once we have the ages, we'll go for the email addresses. This one is a little bit trickier, since we appear to have domains of all kinds, so the only conditions will be as follows:
- Start with alphanumeric characters, including special characters (*`.`, `-`, `_`, etc.*)
- Continue with an `@` symbol.
- Continue with alphanumeric characters (domain name)
- Close with at least one dot character followed by alphabetical characters (*top-level domain*)

##### **Code**
```RegEx
(?<email_address>[a-zA-Z0-9_.+-]+\@[a-zA-Z0-9-.]{1,})\, ?
```

The phone number is also slightly trickier, since we have two possible combinations we can accept:
- `8-222-111-0000`
- `456-789-0123`

So, in essence, the first segment is optional, while the other 3 are required:

##### **Code**
```RegEx
(?<phone_number>(\d{1,2}\-)?\d{3}\-\d{3}\-\d{4})$
```

We also make sure to include an end-of-line metacharacter using the dollar sign `$`.

If we join all the pieces together, we should end up with something like the expression below:

##### **Code**
```RegEx
^(?<first_name>[A-z]+)\, ?(?<last_name>[A-z]+)\, ?(?<address>[A-zÀ-úÀ-ÿÀ-ÖØ-öø-ÿ ']+)\, ?(?<profession>[A-z ]+)\, ?(?<age>\d+|Immortal)\, ?(?<email_address>[a-zA-Z0-9_.+-]+\@[a-zA-Z0-9-.]{1,})\, ?(?<phone_number>(\d{1,2}\-)?\d{3}\-\d{3}\-\d{4})$
```

If we transfer this expression to a RegEx visualizer tool, we can see in this [link](https://regex-vis.com/?r=%5E%28%3F%3Cfirst_name%3E%5BA-z%5D%2B%29%5C%2C+%3F%28%3F%3Clast_name%3E%5BA-z%5D%2B%29%5C%2C+%3F%28%3F%3Caddress%3E%5BA-z%C3%80-%C3%BA%C3%80-%C3%BF%C3%80-%C3%96%C3%98-%C3%B6%C3%B8-%C3%BF+%27%5D%2B%29%5C%2C+%3F%28%3F%3Cprofession%3E%5B%5Cw+%5D%2B%29%5C%2C+%3F%28%3F%3Cage%3E%5Cd%2B%29%5C%2C+%3F%28%3F%3Cemail_address%3E%5Ba-zA-Z0-9_.%2B-%5D%2B%5C%40%5Ba-zA-Z0-9-.%5D%7B1%2C%7D%29%5C%2C+%3F%28%3F%3Cphone_number%3E%28%5Cd%7B1%2C2%7D%5C-%29%3F%5Cd%7B3%7D%5C-%5Cd%7B3%7D%5C-%5Cd%7B4%7D%29%24+) that we end up with a complete structure.

Now it's time to transfer this expression to our application.

## 3. Performing tests in a Scala worksheet
Earlier in this module, we created a worksheet; the advantage with working with these files, is that we can immediately see the result of our evaluations, without having to compile and run. The main downside to this, is that we are limited in terms of reading and writing files (*these will not work properly*). So, what we'll do, is emulate csv entries using a string containing some records:

##### **Code**
```Scala
import scala.util.matching.Regex

val myText: String =
"""
Lucifer,Morningstar,Lux, Nightclub Owner, Immortal, lucifermorningstarlux.com,123-456-7890
Ray,Shoesmith,Sydney, Criminal, 40, ray.shoesmith@underworld.com.au,234-567-890
John,Tavner,Milwaukee, Intelligence Officer, 30, john.tavnermilwaukee.gov,345-678-9012
Doron,Kavillio,Israel, Commando, 50, doron.kavillio@israel.gov,456-789-0123
Wayne,McCullough,Brockton, Teenager, 16, wayne.mcculloughbrockton.net,567-890-1234
Edmond,Dantes,Château d'If, Sailor, 25, edmond.dantes@montecristo.com,678-901-2345
Rodion,Raskolnikov,Saint Petersburg, Ex-Student, 23, raskolnikov.rodionstpetersburg.ru,789-012-3456
"""
```

Now, we include our translated RegEx; it's important to mention that Scala does not yet support named captured groups, so we'll have to work with unnamed groups for this example. Also, unfortunately Scala is extremely picky when it comes to declaring RegEx using newline characters. Because of this, and to increase clarity, we'll declare one `String` variable per group of our expression, then concatenate all, and finally convert to a regular expression:

##### **Code**
```Scala
val namePattern: String = """([A-Za-z]+), ?"""
val surnamePattern: String = """([A-Za-z]+), ?"""
val addressPattern: String = """([A-Za-zÀ-úÀ-ÿÀ-ÖØ-öø-ÿ ']+), ?"""
val professionPattern: String = """([A-Za-z ]+), ?"""
val agePattern: String = """(\d+|Immortal), ?"""
val emailPattern: String = """([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+), ?"""
val phonePattern: String = """((\d{1,2}-)?\d{3}-\d{3}-\d{4})"""

val completePattern: String = namePattern + surnamePattern + addressPattern + professionPattern + agePattern + emailPattern + phonePattern
val regexPattern: Regex = completePattern.r
```

So that in the end, we're left with something like such:

##### **Output**
```
regexPattern: Regex = ([A-Za-z]+), ?([A-Za-z]+), ?([A-Za-zÀ-úÀ-ÿÀ-ÖØ-öø-ÿ ']+), ?([A-Za-z ]+), ?(\d+|Immortal), ?([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+), ?((\d{1,2}-)?\d{3}-\d{3}-\d{4})
```

We could also have done it in a single line, but it would decrease readability:

##### **Code**
```Scala
val regexPattern: Regex = """([A-Za-z]+), ?([A-Za-z]+), ?([A-Za-zÀ-úÀ-ÿÀ-ÖØ-öø-ÿ ']+), ?([A-Za-z ]+), ?(\d+|Immortal), ?([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+), ?((\d{1,2}-)?\d{3}-\d{3}-\d{4})""".r
```

The matches variable is an iterator object, so now, the only thing we need to do is to include a `foreach` statement that goes through every record (*newline*) and performs a pattern matching of the records that comply with out expression:

##### **Code**
```Scala
matches.foreach { m =>
    println(s"First name: ${m.group(1)}")
    println(s"Last name: ${m.group(2)}")
    println(s"Address: ${m.group(3)}")
    println(s"Profession: ${m.group(4)}")
    println(s"Age: ${m.group(5)}")
    println(s"Email address: ${m.group(6)}")
    println(s"Phone number: ${m.group(7)}")
    println("-----")
}
```

##### **Output**
```
// First name: Doron
// Last name: Kavillio
// Address: Israel
// Profession: Commando
// Age: 50
// Email address: doron.kavillio@israel.gov
// Phone number: 456-789-0123
// -----
// First name: Edmond
// Last name: Dantes
// Address: Château d'If
// Profession: Sailor
// Age: 25
// Email address: edmond.dantes@montecristo.com
// Phone number: 678-901-2345
// -----
```

It appears that there are just 2 records from this subset that comply with our requirements. We can verify this by going to RegEx101, and inserting the same set of entries we just used, along with the expression employed:

D002A042_02.png

Now that we have positive results using our worksheet, it's time to get more serious and import our entire set using a proper `.scala` file.

## 4. Writing our application

### 4.1 Importing the required dependencies
When we created our project, a `Main.scala` file was also generated. We'll open it, and start by importing the required dependencies:

##### **Code**
```Scala
import java.io.{File, FileWriter}
import org.apache.commons.csv.{CSVFormat, CSVParser, CSVPrinter}
import scala.util.matching.Regex
import scala.collection.JavaConverters._
```

Where:
- `java.io.FileReader`: Is used for for reading streams of characters.
- `org.apache.commons.csv._`: Is used to read and write files in variations of the Comma Separated Value (*CSV*) format.
- `scala.util.matching.Regex`: provides the `Regex` class used to perform regex matching in bodies of text.
- `scala.collection.JavaConverters._`: Provides a variety of decorators that enable converting between Scala and Java collections using extension methods.

### 4.2. Defining our functions
Once we have our dependencies ready, we'll define some functions that will help us modularize our small application:
- A main function called `runMatcher`: Will call the `writeData` function.
- A reader function called `readCsvFile`: Will read a `.csv` file containing our data.
- A matching function called `matchData`: Will match our entries using a predefined regular expression.
- A writing function called `writeData`: Will write a new `.csv` file containing only matched records.

#### 4.2.1 The main function
The main function will simply call the other functions, in this case, the writing function which will be at the last part of our application. 

##### **Code**
```Scala
// Define main function
@main def runMatcher: Unit = {
  // Define directories
  val rDir: String = "utils/characters.csv"
  val wDir: String = "utils/characters_processed.csv"

  // Define RegEx groups
  val namePattern: String = """([A-Za-z]+), ?"""
  val surnamePattern: String = """([A-Za-z]+), ?"""
  val addressPattern: String = """([A-Za-zÀ-úÀ-ÿÀ-ÖØ-öø-ÿ ']+), ?"""
  val professionPattern: String = """([A-Za-z ]+), ?"""
  val agePattern: String = """(\d+|Immortal), ?"""
  val emailPattern: String = """([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+), ?"""
  val phonePattern: String = """((\d{1,2}-)?\d{3}-\d{3}-\d{4})"""

  writeData(rDir, wDir, regexPattern)
}
```

Here, we're simply:
- Declaring two variables holding our directory paths.
- Declaring out RegEx pattern that we'll use later for pattern matching.
- Calling our not-yet-implemented `writeData` function.

#### 4.2.2 The readCSV file function
This function will help us read our target file, which is in a `.csv` file format, to a Scala `List` of `CSVRecord` objects.

##### **Code**
```Scala
// Defining our reading function
def readCsvFile(readPath: String): List[String] = {
  val file = new File(readPath)
  val parser = CSVParser.parse(file, java.nio.charset.StandardCharsets.UTF_8, CSVFormat.DEFAULT)
  val records = parser.getRecords.asScala.toList
  parser.close()
  records.map(_.toString)
}
```

What we're doing is:
1. We first declare our function with a single argument, the target path, and an expected return type of `List[String]`.
2. We then create a new `java.io.File` object containing our path.
3. Next, we declare a CSV parser handle.
	1. This new object will take the `File` object, the encoding (*in this case `UTF_8`*), and the CSV format we're expecting, in this case, `DEFAULT`.
4. We then ask the parser for our records, and convert them to a `List`. This `List` contains a set of `CSVRecord` objects with all of its values.
5. Finally, we close the parser handler and map each CSV record to its string representation using the `toString` method.

#### 4.2.3 The matchData function
This function will be in charge of matching our data using a predefined RegEx pattern:

##### **Code**
```Scala
def matchData(readDir: String, regexPattern: Regex): List[String] = {
  val csvData = readCsvFile(readDir)
  val matchedData = csvData.flatMap { row =>
    regexPattern.findFirstMatchIn(row).map { m =>
      s"""
      |First name: ${m.group(1)}
      |Last name: ${m.group(2)}
      |Address: ${m.group(3)}
      |Profession: ${m.group(4)}
      |Age: ${m.group(5)}
      |Email address: ${m.group(6)}
      |Phone number: ${m.group(7)}
      |-----""".stripMargin
    }
  }
  matchedData
}
```

What we're doing is:
1. We fist call our `csvData` function and assign its return value to a new variable called `csvData`. The type of this variable will be a `List` of `String` values.
2. We then create a new variable called `matchedData`, that will perform our RegEx matching. This expression is slightly more elaborate, so lets detail it more:
	1. We take the `csvData` variable of type `List[String]`.
	2. We then use the `flatMap` higher-order method. This method applies (*`Map`*) a given function to all elements inside our list, and then flattens (*`flat`*) the remaining object. The level of granularity is row level, as denoted in `csvData.flatMap { row => ... }`.
	3. The function in this case is `regexPattern.findFirstMatchIn(row)`: It searches for the first match of the regular expression pattern (`regexPattern`) within the current `row` string. The result is an `Option` that either contains the match or is `None`.
	4. `.map { m => ... }`: If a match is found in the previous step, it maps the match (*`m`*) to a new value.
	5. We then take `m`, and see if it matches any of the groups by using string interpolation `s"""${var}"""`.
	6. Finally, we apply the `stripMargin` method to our string output, which removes the leading `|` characters and any preceding whitespace on each line, resulting in properly formatted output.
3. We finally call the `matchedData` variable. This is required because it triggers the evaluation of the transformation operations defined earlier in the code. In Scala, certain operations like `flatMap` and `map` are lazily evaluated, meaning they are not executed immediately when they are defined. Instead, they are executed when the result is actually needed or when a strict operation is applied to them.

#### 4.2.4 The writeData function
This is our last function, and involves paying attention to how the output from the previous function is being formatted. If we take a look at our previous output, it should look something like such:

##### **Output**
```
List(
First name: Edmond
Last name: Alexandre
Address: Marseilles
Profession: Sailor
Age: 30
Email address: alexandre.edmond@marseilles.fr
Phone number: 222-333-4444
-----,
First name: Alyosha
Last name: Karamazov
Address: Saint Petersburg
Profession: Monk
Age: 20
Email address: alyosha.karamazov@stpetersburg.ru
Phone number: 555-666-7777
...
```

So, we need to translate this list into something that is writeable to a `.txt` file. This is easily done by using a `foreach` method:

##### **Code**
```Scala
def writeData(readPath: String, writePath: String, regexPattern: Regex): Unit = {
  val data: List[String] = matchData(readPath, regexPattern)
  val fileWriter = new FileWriter(writePath)
  data.foreach(record => fileWriter.write(record + "\n"))
  fileWriter.close()
}
```

What we're doing is:
1. We first define our function, accepting both reading & writing paths, as well as our RegEx pattern.
2. The output type of this function is `Unit`, since we're not returning anything to the user, we're simply writing a file.
3. We then call our our `matchData` function and assign it to a new variable.
4. Next, we create a new `FileWriter` object.
5. Next, we iterate over all records inside our list, and write them by including the contents and a newline character in the end, so the records are properly separated.
6. Finally, we close the `fileWriter` handler object.

## 5. Running our application
Now that we have everything we need, we can compile & run our application using `sbt`. For this, we can head to our root directory, open a new PowerShell instance, and execute the following:

##### **Code**
```PowerShell
sbt run
```

Which should yield the following:

##### **Output**
```
[info] welcome to sbt 1.8.2 (Oracle Corporation Java 11)
[info] loading settings for project regex-matching-build-build from metals.sbt ...
[info] loading project definition from \project\project
[info] loading settings for project regex-matching-build from metals.sbt ...
[info] loading project definition from \project
[success] Generated .bloop\regex-matching-build.json
[success] Total time: 0 s, completed May 23, 2023, 5:20:30 PM
[info] loading settings for project root from build.sbt ...
[info] set current project to regex-matching (in build file:regex-in-scala)
[info] compiling 1 Scala source to \regex-in-scala\target\scala-3.2.2\classes ...
[warn] there was 1 deprecation warning; re-run with -deprecation for details
[warn] one warning found
[info] running runMatcher
```

If we take a look at our `.txt` file, we can see that it correctly matched the expected records, and wrote them in a really nice format:

##### **Output**
```
First name: Edmond
Last name: Alexandre
Address: Marseilles
Profession: Sailor
Age: 30
Email address: alexandre.edmond@marseilles.fr
Phone number: 222-333-4444
-----

First name: Alyosha
Last name: Karamazov
Address: Saint Petersburg
Profession: Monk
Age: 20
Email address: alyosha.karamazov@stpetersburg.ru
Phone number: 555-666-7777
-----

First name: Ivan
Last name: Karamazov
Address: Saint Petersburg
Profession: Intellectual
Age: 24
Email address: ivan.karamazov@stpetersburg.ru
Phone number: 666-777-8888
-----

First name: Dewitt
Last name: Booker
Address: Columbia
Profession: Detective
Age: 38
Email address: booker.dewitt@columbia.com
Phone number: 888-999-1010
-----

First name: Konstantin
Last name: Levin
Address: Russian Countryside
Profession:  
Age: 35
Email address: levin.konstantin@countryside.ru
Phone number: 3-777-666-5555
-----
...
```

---

# Conclusions
In this segment, we briefly discussed what Scala & RegEx are, what are the use-cases of both, and how can we use RegEx inside Scala to perform simple validations by using the built-in `scala.util.matching.Regex` class. We also went over a simple real-life example, where we were presented with a messy CSV file that we had to process by using regular expressions. Finally, we wrote the new file containing the clean records in a readable format what we can present to anyone, and it'll be understood.

Scala is not the most beginner-friendly language for performing RegEx matching; there are other languages such as Python providing easy-to-use implementations that can be more flexible in some instances. However, Scala is still extremely powerful, and provides excellent capabilities; similar to Python, we can use unnamed capturing groups to treat our fields as variables. We can also go over large bodies of text without sacrificing performance if we use the right modules & methods.

So sure, if we're in a hurry and would like to simply perform a RegEx analysis on some text, even RegEx101 is a better option for this; the real power of Scala surfaces when we're aiming to develop a streamlined process that can handle terabytes of records while staying performant.

---

# References
- [Introduction to Apache Commons CSV, Baeldung](https://www.baeldung.com/apache-commons-csv)
- 

---

# Copyright
Pablo Aguirre, Creative Commons Attribution 4.0 International, All Rights Reserved.