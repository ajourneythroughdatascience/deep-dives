<article class="first">
  <div class="title">
    <h1>Polars: A Lightning-Fast DataFrame Library for Python and Rust</h1>
  </div>
</article>

---

[![made-with badge](https://img.shields.io/static/v1?label=Made%20with&message=Obsidian&color=7d5bed&logo=obsidian&labelColor=1a1a1a&style=flat)](https://obsidian.md/)

[![type](https://img.shields.io/static/v1?label=Type&message=deep-dive&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAi0lEQVRIS+2WMQ7AIAhF/UNXrtP7rz2OYxeqTWxMTBUSxQVXfnzyQQKC8YExL7zAGCNbgIkIsIKVhBw4vbR7unR6Gp0LvwxXd2v+EvkdDpxWXpWlRTyi9/pABRyBJHEHSlxSadxSlV0SsVsqcUml2W/pynWxnsXNisHMRxrCl8qvH3ECnQDuOmy+0zwB4WNxmUKgwwAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/deep-dives/) [![category](https://img.shields.io/static/v1?label=Category&message=data-science&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAB9UlEQVRIS6VWMU7DQBDkDAQEdrAoCISCAomCL1DxC95Azy9oeQS/oOIHVFAgREFoCHGCRSzZzEU+63LZ9W6CO/vudmZ2d9Zn1pTPaDSqut2usduHw+FpFEUv7t1fk8LNAkiPDWj3+ADuTPjNvXMxWwGzLCuqqtqwh5MkiY0xEwfOAfrEKFAWUBO4DZQDXgCEqjuouvbZUanUrocpngMMVUkKtKC+WhFQUudAUd8r1PkepJ/w7Tysn4uzkNJlascF9WOASAki6w0xrn19b3Gpps5y3kRfJADPZgr9gJSP0EgDHDiQ/Mp50PfxAmDtuQhsZmb/z0OVhwSkmGrSGp5bGRDp3EFaJ5JaiahdZ2vYNj/JkWVMgW7sgNw2yOW+99gacp7TeFE72OcUrgo4Ho93+/3+D5T9QmGHm0BNSnHgMI7jj9Ai2tElZGCK9S3S+GA4BcNNydBaIuEstu/iLJWCa+pLDm+Nz+xQAsBenucnRVG8asFq0s/Yf9YoVAI21wyn3N4I7M1A8ijWHwB42XrFqIO9YfMRlVqqyXC5ukED3nIEVJcoBXv1lmWa5gIpeeQioyTWVj1uXf0DpgKUZbmfpunXKnVnU9rWDKiTHRSDNkDu36iqIQK/Q+mxU8sBYniL/1EVoJ9Wqwo/5x6Cf9YKv6Em1XbNH5bGfSwvuRe1AAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/categories/data-science/) [![technologies](https://img.shields.io/static/v1?label=Technologies&message=Python&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAACXBIWXMAAAsTAAALEwEAmpwYAAAA1klEQVR4nM2RMW7CUBBEnUikIQUIlBJxrrQgJG7ABRBnoUkaWhpoUgWJlgNYbvz/G1dUi1ayoy87rpOtVrszs6OdLPtXlef5UNJXjHHcCwohjMzsKZ3FGN+Bq/e+c0xHGfiWtEznkg6SNnW/dIxjs0YJ2AMnM3tJSFPgHkKY17gBcAQ+zOw5A3aSbsCkdW0NnNOZY2rstpcInJ3cS/SzwGdqtSzLmdusquqtIXWsehVF8QpcJK1qmxt/TMv6wjE/z0leP27i8Ag8inT/axxtAQ+9o/zn9QD3JOiyTjnQEQAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/technologies/) [![website article](https://img.shields.io/static/v1?label=Website&message=Post%20Link&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAACXBIWXMAAAsTAAALEwEAmpwYAAAB+ElEQVR4nO2VOYgUURCGR/BAI4MN1EwjI89EMDYQvNBNNNlcE0VBUdlUUSMjj2BF2UDRePDAwGzNF2GNPIYd8Hjv/6YnEHSf/FIDPTJiu4nJFBTd1Kv6/nrVBd1q/S8DJiU9AmaBm5LOSjoATPwDY0LSQUnnzDArmJOjkqclvQceSHohaR6oJC1JeiPprqT9pZSVg5pSyirH4sw5S1EzbwZwP5jTIwWBdj1meEppZ6/XOyXpCdCX9Am4Fv45Yo+Bk1VV7ag3FNz2kKC7yznvHiX4u3U6nXU55xPAW7vfHfvLmNtmW8NaFux67k0Ea03esTfJJQTj23bHgiNtPNK6jZem3Wpg46Wp23hp2q0GNl6axksjaRGYkXRF0mnHq6ra2HSk/X5/k6RDks6YEazFPwnuBS5KuirptqTnkj4CJZ4zwNFSytqBoP/2wDHgXi33A/BM0i2zzDR7SBC4LGlPr9fb5huVUlYMus45b5E0FYJfgQS8C8/Al7jJVEpp86DODLPMNDs0up7xXBQZVKLLb8CCpIfA+ZzzvpTS+lLKGuAI8DT8cClltc+c49yoWQjGL140ao25oW8QXW1IKe3KOR8Hbkh66ZtI+i7plaG+iR244JjP3HDkXnetGWbVp9XYopHtHgvwWtIPu9+BSx7bssBNDdhqX07xT/Jbz1SBBDGHAAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/deep-dives/polars-a-lightning-fast-dataframe-library-for-python-and-rust/)

Writing code can be as simple as importing the required libraries, declaring our variables, functions, and classes as required, including some docstrings here and there, some additional comments, executing, and we're done. While we're at it, let's skip the function & class part and drop everything as is. Even better, let's also save some lines by stripping our file from all comments.

In this Deep Dive, we'll

We'll be using Python scripts which can be found in the [Deep Dive Repo](https://github.com/pabloagn/blog/tree/master/computer-science/programming-best-practices-writing-better-code).

---

# Table of Contents
- [Legibility](#legibility)
	- [Authoring](#1-authoring)
	- [Comments](#2-comments)
- [Conclusions](#conclusions)
- [References](#references)
- [Copyright](#copyright)

---

# Preface
**Polars** is a DataFrame library/in-memory query engine written in [Rust](https://pabloagn.com/technologies/rust/). It's built upon the [safe Arrow2 implementation](https://github.com/jorgecarleitao/arrow2) of the [Apache Arrow specification](https://arrow.apache.org/docs/format/Columnar.html), enabling efficient resource use and processing performance. By doing so it also integrates seamlessly with other tools in the Arrow ecosystem.

Unlike tools such as `dask`, which tries to parallelize existing single-threaded libraries like `Numpy` and `Pandas`, `Polars` is designed for parallelization, resulting in extremely fast processing speeds by default.

A `groupby` task performed on a 5GB dataset, resulted in the following execution times:

| Method        | Version | Date Executed | Execution Time [s] |
| ------------- | ------- | ------------- | ------------------ |
| `DataFrames.jl` | 1.1.1   | May 15, 2021  | 9                  |
| `Polars`        | 0.8.8   | June 30, 2021 | 11                 |
| `cuDF`          | 0.19.2  | May 31, 2021  | 17                 |
| `Spark`         | 3.1.2   | May 31, 2021  | 34                 |
| `Pandas`        | 1.2.5   | June 30, 2021 | 70                 |
| `Arrow`         | 4.0.1   | May 31, 2021  | 212                |

###### *[Table 1. Groupby execution times on 5 GB data set, H2O AI](https://h2oai.github.io/db-benchmark/)*

A `join` task performed on a 5GB dataset, resulted in the following execution times:

| Method        | Version | Date Executed | Execution Time [s]  |
| ------------- | ------- | ------------- | ------------------- |
| `Polars`        | 0.8.8   | June 30, 2021 | 43                  |
| `Spark`         | 3.1.2   | May 31, 2021  | 332                 |
| `DataFrames.jl` | 1.1.1   | June 3, 2021  | 349                 |
| `Pandas`        | 1.2.5   | June 30, 2021 | 628                 |
| `cuDF`          | 0.19.2  | May 31, 2021  | internal error      |
| `Arrow`         | 4.0.1   | May 31, 2021  | not yet implemented |

###### *[Table 2. Join execution times on 5 GB data set, H2O AI](https://h2oai.github.io/db-benchmark/)*


We can see that...


The full benchmark can be consulted [here](https://h2oai.github.io/db-benchmark/).

`Polars` for Python exposes a complete Python API, including the full set of features to manipulate DataFrames using an expression language similar to `pandas`. It also has 2 different APIs:
- A lazy API
- An eager API

With eager execution, the code is run as soon as it's encountered; results are returned immediately. With lazy execution, the code is run until the result is required. 

---
# Preparing our environment
Polars is offered as a Python and a Rust package. In this segment, we'll only review the Python flavor; in a future iteration we might review its Rust counterpart.

We're going to use the `polars` package. More information about this package can be found in the [Polars Official Web Page](https://www.pola.rs/), in the [Polars GitHub Repo](https://github.com/pola-rs/polars), or in the [Polars Official Documentation for Python](https://pola-rs.github.io/polars/py-polars/html/reference/index.html).

If we don't yet have it, we can install it:

##### **Code**
```PowerShell
pip install polars
```

We will also install some additional libraries, which are not directly related to `Polars`, but will be useful for some bonus content.

##### **Code**
```PowerShell
pip install geopandas  
pip install geopy
pip install folium
```

The convention is to import `polars` using the `pl` alias, but we can select any alias we find more convenient. For our case, we'll be using the preferred alias. We'll also import some other modules which will come in handy:

##### **Code**
```Python
import polars as pl
import pandas as pd
import pyarrow
import os
import glob
from datetime import datetime

# Import bonus modules
import folium
from folium.plugins import FastMarkerCluster
```

As of the writing of this article, the `polars` version downloaded is the 0.16.9. We can confirm this by using the `__version__` method:

##### Code
```Python
print(pl.__version__)
```

We will also use the [Airbnb Prices in European Cities](https://www.kaggle.com/datasets/thedevastator/airbnb-prices-in-european-cities) data set by [The Devastator](https://www.kaggle.com/thedevastator). The complete set has 20 files, one for each European city.

We can first create a new folder `datasets` inside our project folder. We can then download the entire set as a `.zip` file, extract its contents, and move them to the newly created folder.

The `datasets` folder will contain 20 files, weighting a total of 10.2MB.

We can also create an outputs directory, where we will store our written files:

##### **Code**
```PowerShell
mkdir datasets, outputs
```

We will define both directories as variables inside our script:

##### **Code**
```Python
rDir = 'datasets/'
wDir = 'outputs/'
```

With everything ready, we can now proceed to load our data sets and perform some basic operations.

---

# Polars data structures
Similar to `pandas`, `polars` has two main data structures:

- `Series`: One-dimensional.
- `DataFrame` (With a `LazyFrame` variation for *lazy execution*): Can be one or two-dimensional.

We can define a `series` object by enclosing the values in square brackets `[]`:

##### **Code**
```Python
# Declare series
se = pl.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Check type
type(se)

# Print object
se
```

##### **Output**
```
polars.internals.series.series.Series

shape: (10,)
Series: '' [i64]
[
	1
	2
	3
	4
	5
	6
	7
	8
	9
	10
]
```

We can define a DataFrame object by enclosing our set of entries in curly brackets `{}`. Each dictionary key will correspond to a column name, and each value to the column entries.

##### **Code**
```Python
# Declare DataFrame
df = pl.DataFrame({'name' : ['Jack', 'Charles', 'Clarice'],
                   'surname' : ['Kerouac', 'Bukowski', 'Lispector'],
                   'birth' : [datetime(1922, 3, 12),
                              datetime(1920, 8, 16),
                              datetime(1920, 12, 10)]
                   })

# Print object
df
```

##### **Output**
```
shape: (3, 3)
+---------+-----------+---------------------+
| name    | surname   | birth               |
| ---     | ---       | ---                 |
| str     | str       | datetime[μs]        |
+===========================================+
| Jack    | Kerouac   | 1922-03-12 00:00:00 |
| Charles | Bukowski  | 1920-08-16 00:00:00 |
| Clarice | Lispector | 1920-12-10 00:00:00 |
+---------+-----------+---------------------+
```

---
# Eager execution
We will start by executing `polar` commands using *eager execution*. This is the default method, and will execute our code upon calling.

We can read one of our downloaded `.csv` files:

##### **Code**
```Python
df = pl.read_csv(os.path.join(rDir, 'berlin_weekends.csv'))
```

This method will read our file into a `polars.DataFrame` object:

##### **Code**
```Python
type(df)
```

##### **Output**
```
polars.internals.dataframe.frame.DataFrame
```

---
# Lazy execution
As we mentioned earlier, *lazy* operations don't execute until we call `collect`. This allows `polars` to optimize/reorder the query which may lead to faster queries or less type errors.

There are two main ways for *lazy-reading* a `.csv` file in `polars`:

- Using `pl.scan_csv()`
- Using `pl.read_csv().lazy()`

Both methods perform the same operation, the main difference between them being that the first one lazy-loads by default, while the second one includes the `.lazy()` method to specify that we're *lazy-loading*.

We can read a `.csv` file using either of the two methods:

##### **Code**
```Python
# Reading a csv file using pl.scan_csv()
df_s = pl.scan_csv(os.path.join(rDir, 'berlin_weekends.csv'))

# Reading a csv file using pl.read_csv().lazy()
df_l = pl.read_csv(os.path.join(rDir, 'berlin_weekends.csv')).lazy()
```

As opposed to *eager execution*, this method will read our file into a `polars.LazyFrame` object:

##### **Code**
```Python
type(df_s), type(df_l)
```

##### **Output**
```
(polars.internals.lazyframe.frame.LazyFrame,
 polars.internals.lazyframe.frame.LazyFrame)
```

If we try to get the head of our object, we will actually be presented with its memory location, and not the first records.

##### **Code**
```Python
df_s.head()
```

##### **Output**
```
<polars.LazyFrame object at 0x22F0CCFFF50>
```

We can display the object graph, which is a diagram of how the execution will take place upon calling `collect`.

##### **Code**
```Python
df_s.show_graph()
```

##### **Output**

SCREENSHOT_2

We can include additional transformation steps to our object:

##### **Code**
```Python
df_s_filtered = (df_s.filter(pl.col("bedrooms") >= 2).
                select(pl.col("metro_dist")).
                sort("metro_dist")
                )
```

And view its graph again:

##### **Code**
```Python
df_s_filtered.show_graph()
```

##### **Output**

SCREENSHOT_3

We can see that the additional steps were added, and are ready to be executed upon collecting our object.

We can also view this same information in text format:

##### **Code**
```Python
df_s_filtered.describe_optimized_plan()
```

##### **Output**
```
'SORT BY [col("metro_dist")]\n    FAST_PROJECT: [metro_dist]\n      CSV SCAN datasets/berlin_weekends.csv\n      PROJECT 2/20 COLUMNS\n      SELECTION: [(col("bedrooms")) >= (2i64)]\n'
```

Which is, of course, less neat than the previous graphical method.

We can finally call `collect()`:

##### **Code**
```Python
df_s_filtered.collect()
```

##### **Output**
```
shape: (124, 1)
┌────────────┐
│ metro_dist │
│ ---        │
│ f64        │
╞════════════╡
│ 0.088494   │
│ 0.110308   │
│ 0.12578    │
│ 0.131641   │
│ ...        │
│ 2.87661    │
│ 4.512803   │
│ 5.324563   │
│ 9.598773   │
└────────────┘
```

---

# Reading and writing multiple file formats

## 1. Writing
As with `pandas`, `polars` can write to multiple file formats, the most common ones being:

- `.avro`
- `.csv`
- `.ipc`
- `.json`
- `.parquet`

To illustrate some examples, we will read our entire `weekdays` data set into a DataFrame object, and then write to the file formats above:

##### **Code**
```Python
# Read the entire weekdays data set
weekdays_files = glob.glob(os.path.join(rDir, "*weekdays.csv"))

weekdays_list = []

for filename in weekdays_files:
    city = re.search('datasets\\\(.*)_weekdays.csv', filename).group(1)
    df_weekdays = (pl.read_csv(filename).
                   drop(['']).
                    with_columns(pl.lit(city).
                    alias('city'))
                    )
                   
    weekdays_list.append(df_weekdays)

df_weekdays = pl.concat(weekdays_list,
                        rechunk = True)

df_weekdays.shape

round(df_weekdays.estimated_size(unit='mb'), 4)
```

We should end up with a `polars` DataFrame object of shape `(25500, 20)`:

##### **Output**
```
(25500, 20)

3.7998
```

Let us explain in detail by writing the pseudocode for the steps performed:
- Declare a list of `weekday` data set paths by using the `glob.glob()` method.
- Create an empty DataFrame list `weekdays_list`.
- Iterate over the list.
- Extract the city using RegEx.
- Read each file using `pl.read_csv(filename)`.
- Drop the first column which represents the index.
- Assign a new column to each DataFrame object containing it's city name using `pl.lit(city).alias('city')`.
- Append each DataFrame to the DataFrame list `weekdays_list`.
- Concatenate all DataFrames in `weekdays_list`, passing `rechunk = True` as argument (*make sure that all data is in contiguous memory*).
- Get the object's shape.
- Get the object's estimated size in `mb` rounded to 4 decimal places.

Now, we can write our DataFrame to different file formats. The general syntax is `df.write_formatname(dir, args)`:

##### **Code**
```Python
# Write to csv
df_weekdays.write_csv(os.path.join(wDir, 'weekdays.csv'))

# Write to Parquet non-partitioned
df_weekdays.write_parquet(os.path.join(wDir, 'weekdays.parquet'))

# Write to Avro
df_weekdays.write_avro(os.path.join(wDir, 'weekdays.avro'))

# Write to JSON
df_weekdays.write_json(os.path.join(wDir, 'weekdays.json'))
```

## 2. Reading
Conversely, polars can read all the file formats we wrote earlier. We'll skip the `.csv` file format since we already reviewed it. For the other cases, we can use the `pl.read_formatname()` syntax:

##### **Code**
```Python
# Write to csv
df_weekdays_csv = pl.read_csv(os.path.join(wDir, 'weekdays.csv'))

# Write to Parquet non-partitioned
df_weekdays_parquet = pl.read_parquet(os.path.join(wDir, 'weekdays.parquet'))

# Write to Avro
df_weekdays_avro = pl.read_avro(os.path.join(wDir, 'weekdays.avro'))

# Write to JSON
df_weekdays_json = pl.read_json(os.path.join(wDir, 'weekdays.json'))
```

We can confirm that our files were read successfully by selecting a given column and getting each object's head:

##### **Code**
```Python
df_weekdays_csv['realSum'].head(10)
df_weekdays_parquet['realSum'].head(10)
df_weekdays_avro['realSum'].head(10)
df_weekdays_json['realSum'].head(10)
```

##### Output
```
shape: (10,)
Series: 'realSum' [f64]
[
	194.033698
	344.245776
	264.101422
	433.529398
	485.552926
	552.808567
	215.124317
	2771.307384
	1001.80442
	276.521454
]

shape: (10,)
Series: 'realSum' [f64]
[
	194.033698
	344.245776
	264.101422
	433.529398
	485.552926
	552.808567
	215.124317
	2771.307384
	1001.80442
	276.521454
]

shape: (10,)
Series: 'realSum' [f64]
[
	194.033698
	344.245776
	264.101422
	433.529398
	485.552926
	552.808567
	215.124317
	2771.307384
	1001.80442
	276.521454
]

shape: (10,)
Series: 'realSum' [f64]
[
	194.033698
	344.245776
	264.101422
	433.529398
	485.552926
	552.808567
	215.124317
	2771.307384
	1001.80442
	276.521454
]
```

---

# Basic operations

## 1. Exploratory methods
There are a wide range of exploratory methods we can use in order to take a first look at our data. We can display our DataFrame's shape, columns and first 10 entries for the `realSum` column:

##### **Code**
```Python
df.shape
df.columns
df['realSum'].head(10)
df['realSum'].tail(10)
```

##### **Output**
```
(1200, 20)

['',
 'realSum',
 'room_type',
 'room_shared',
 'room_private',
 'person_capacity',
 'host_is_superhost',
 'multi',
 'biz',
 'cleanliness_rating',
 'guest_satisfaction_overall',
 'bedrooms',
 'dist',
 'metro_dist',
 'attr_index',
 'attr_index_norm',
 'rest_index',
 'rest_index_norm',
 'lng',
 'lat']

shape: (10,)
Series: 'realSum' [f64]
[
	185.799757
	387.49182
	194.914462
	171.777134
	207.768533
	162.428718
	521.875292
	155.417407
	171.777134
	147.237543
]

shape: (10,)
Series: 'realSum' [f64]
[
	162.428718
	231.840703
	127.605871
	175.049079
	156.585959
	84.83687
	134.617182
	134.617182
	160.091614
	359.680284
]
```

We can notice some interesting details:
- The `df.columns` method returns a `list`, as opposed to `pandas` which returns a `pandas.core.indexes.base.Index` object.
- The `df.head()` method returns a `polars.internals.series.series.Series` object, similar to `pandas` which returns a `pandas.core.series.Series`. 
- The `df.head()` method also returns the column data type, which in the case of `realSum` is `float64`.

We can also perform a statistical description:

##### **Code**
```Python
df.describe()
```

##### **Output**
```
+------------+------------+-------------+
| describe   | column_0   | realSum     |
| ---        | ---        | ---         |
| str        | f64        | f64         |
+=======================================+
| count      | 1200.0     | 1200.0      |
| null_count | 0.0        | 0.0         |
| mean       | 599.5      | 249.252516  |
| std        | 346.554469 | 240.584178  |
| min        | 0.0        | 64.971487   |
| max        | 1199.0     | 5856.081144 |
| median     | 599.5      | 192.460503  |
+------------+------------+-------------+
...
```

If we want to take a random entry sample, we can do so:

##### **Code**
```Python
df.sample(5)
```

##### **Output**
```
+-----+------------+-----------------+
|     | realSum    | room_type       |
| --- | ---        | ---             |
| i64 | f64        | str             |
+====================================+
| 636 | 139.29139  | Private room    |
| 13  | 577.498364 | Entire home/apt |
| 240 | 291.203141 | Entire home/apt |
| 15  | 127.605871 | Private room    |
| 707 | 755.819389 | Private room    |
+-----+------------+-----------------+
```

## 2. Indexing, selecting and filtering
`Polars` offers two main ways of indexing or filtering a DataFrame:
- Using square brackets `[]`
- Using the `select` and `filter` methods
	- the `select` method is used to select columns
	- the `filter` method is used to select rows

The square brackets `[]` method works similar to `pandas`, but has limited usage in `polars`; it only works in eager mode, and operations on multiple columns are not parallelized.

This method is recommended on the following cases:
-   To extract a scalar value from a `DataFrame`
-   To convert a `DataFrame` column to a `Series`
-   For exploratory data analysis and to inspect some rows and/or columns

### 2.1 Select
We can select the `realSum` column:

##### **Code**
```Python
df.select(pl.col("realSum"))
```

##### **Output**
```
┌────────────┐
│ realSum    │
│ ---        │
│ f64        │
╞════════════╡
│ 185.799757 │
│ 387.49182  │
│ 194.914462 │
│ 171.777134 │
│ ...        │
│ 134.617182 │
│ 134.617182 │
│ 160.091614 │
│ 359.680284 │
└────────────┘
```

We can see that the `pl.col()` method was used; this method accepts one main parameter `name`, where we can directly specify the column name, or include a regular expression. Regular expressions should start with `^` and end with `$`.

We can use a regular expression to select all the columns containing `room`:

##### **Code**
```Python
df.select(pl.col("^room.*$"))
```

##### **Output**
```
┌─────────────────┬─────────────┬──────────────┐
│ room_type       ┆ room_shared ┆ room_private │
│ ---             ┆ ---         ┆ ---          │
│ str             ┆ bool        ┆ bool         │
╞═════════════════╪═════════════╪══════════════╡
│ Private room    ┆ false       ┆ true         │
│ Entire home/apt ┆ false       ┆ false        │
│ Private room    ┆ false       ┆ true         │
│ Private room    ┆ false       ┆ true         │
│ ...             ┆ ...         ┆ ...          │
│ Private room    ┆ false       ┆ true         │
│ Private room    ┆ false       ┆ true         │
│ Entire home/apt ┆ false       ┆ false        │
│ Entire home/apt ┆ false       ┆ false        │
└─────────────────┴─────────────┴──────────────┘
```

Three columns were returned, which coincides with the expected columns from our `df.columns` output.

To select every column or exclude a column, we can use the following:

##### **Code**
```Python
# Selecting all
df.select(pl.col("*"))

# Selecting all except
df.select(pl.exclude("realSum"))
```

To select based on the `dtype` of the columns:

##### **Code**
```Python
df.select(pl.col(pl.Int64))
```

##### **Output**
```
shape: (1200, 5)
+------+-----------------+-------+-----+----------+
|      | person_capacity | multi | biz | bedrooms |
| ---  | ---             | ---   | --- | ---      |
| i64  | i64             | i64   | i64 | i64      |
+=================================================+
| 0    | 2               | 0     | 0   | 1        |
| 1    | 6               | 0     | 1   | 2        |
| 2    | 5               | 0     | 1   | 1        |
| 3    | 2               | 0     | 0   | 1        |
| ...  | ...             | ...   | ... | ...      |
| 1196 | 4               | 1     | 0   | 1        |
| 1197 | 4               | 1     | 0   | 1        |
| 1198 | 3               | 0     | 0   | 1        |
| 1199 | 4               | 1     | 0   | 1        |
+------+-----------------+-------+-----+----------+
```

### 2.2 Filter
We can also filter by `bedrooms` using a boolean comparison, select the `metro_dist` column, sort it ascendingly and get the first 5 entries:

##### **Code**
```Python
(df.filter(pl.col("bedrooms") >= 2).
 select(pl.col("metro_dist")).
 sort("metro_dist").
 head(5)
)
```

##### **Output**
```
┌────────────┐
│ metro_dist │
│ ---        │
│ f64        │
╞════════════╡
│ 0.088494   │
│ 0.110308   │
│ 0.12578    │
│ 0.131641   │
│ 0.135447   │
└────────────┘
```

Similar to `pandas`, the execution order of a statement is top to bottom, meaning it will filter the `bedrooms` column first, and get the head of the resulting object last.

### 2.3 Filtering with multiple conditions

We want to look for a clean place hosting 2 people with a single bedroom. WE want to sort descending by `cleanliness_rating`. We want to be able to identify the place by its coordinates.

Let us filter rooms with `person_capacity` = 2, `bedrooms` = 1, and sorting descending by `cleanliness_rating`:

##### **Code**
```Python
berlin_places = (df.filter((pl.col("person_capacity") == 2) &
                           (pl.col("bedrooms")) == 1).
                 groupby(['lat', 'lng'], maintain_order=True).
                 agg(pl.col("cleanliness_rating").mean()).
                 sort('cleanliness_rating', descending = True)
                 )
```

##### **Output**
```
┌──────────┬──────────┬────────────────────┐
│ lat      ┆ lng      ┆ cleanliness_rating │
│ ---      ┆ ---      ┆ ---                │
│ f64      ┆ f64      ┆ f64                │
╞══════════╪══════════╪════════════════════╡
│ 52.4915  ┆ 13.42344 ┆ 10.0               │
│ 52.47842 ┆ 13.5244  ┆ 10.0               │
│ 52.51229 ┆ 13.45862 ┆ 10.0               │
│ 52.49265 ┆ 13.43842 ┆ 10.0               │
│ ...      ┆ ...      ┆ ...                │
│ 52.49937 ┆ 13.35408 ┆ 6.0                │
│ 52.573   ┆ 13.42254 ┆ 6.0                │
│ 52.49168 ┆ 13.30429 ┆ 5.0                │
│ 52.51526 ┆ 13.46914 ┆ 4.0                │
└──────────┴──────────┴────────────────────┘
```

As we move further, we can see a pattern in `polars` syntax; it's very similar to SQL syntax, while at the same time being closely related to `pandas`. Polars almost writes as a declarative language, each transformation step being very clear. Clarity increases if we separate each statement in a newline continuation.

Since we don't have the actual addresses for the places we would like to check, we will use the geolocation libraries we installed earlier to visualize these coordinates in a `folium` map:

##### **Code**
```Python
# Multiple filtering
berlin_places = (df.filter((pl.col("person_capacity") == 2) &
                           (pl.col("bedrooms")) == 1).
                 sort('cleanliness_rating', descending = True).
                 head(10)
                 )

# Creating a folium map, initializing view with first item
berlin_map = folium.Map(
    location=[berlin_places[0]['lat'][0], berlin_places[0]['lng'][0]],
    tiles='cartodbpositron',
    zoom_start=12,
)

# Adding remaining coordinates
FastMarkerCluster(data=list(zip(berlin_places['lat'], berlin_places['lng']))).add_to(berlin_map)

# Export map to HTML file and visualize using any browser
berlin_map.save(os.path.join(wDir, 'berlin_places.html'))
```

##### **Output**

SCREENSHOT_01

Looks like we we should be looking for places near the Neukölln and Friedrichshain-Kreuzberg boroughs.

### 2.4. Filtering with advanced operators
We can make use of more advanced filtering operators in order to narrow our search:

##### **Code**
```Python
# Filter between range
(df.filter(pl.col("bedrooms").is_between(2, 4)).
 select(pl.col(['bedrooms', 'room_type'])).
 head(5)
)

# Filter null values
(df.filter(pl.col("bedrooms").is_null()).
 select(pl.col(['bedrooms', 'room_type'])).
 head(5)
)


```

##### **Output**
```
shape: (5, 2)
+----------+-----------------+
| bedrooms | room_type       |
| ---      | ---             |
| i64      | str             |
+============================+
| 2        | Entire home/apt |
| 2        | Entire home/apt |
| 3        | Entire home/apt |
| 2        | Private room    |
| 2        | Entire home/apt |
+----------+-----------------+

shape: (0, 2)
+----------+-----------+
| bedrooms | room_type |
| ---      | ---       |
| i64      | str       |
+======================+
+----------+-----------+

```

## 3. Aggregations
Similar to `Pandas`, We can use the `groupby` method to group different columns and perform aggregations using different functions.

Let us group by `room_shared` and calculate the average `cleanliness_rating` for each case:

##### **Code**
```Python
(df.groupby(['room_shared'], maintain_order=True).
    agg(pl.col("cleanliness_rating").mean())
    )
```

##### **Output**
```
┌─────────────┬────────────────────┐
│ room_shared ┆ cleanliness_rating │
│ ---         ┆ ---                │
│ bool        ┆ f64                │
╞═════════════╪════════════════════╡
│ false       ┆ 9.462995           │
│ true        ┆ 8.973684           │
└─────────────┴────────────────────┘
```

It appears that shared rooms are slightly behind in terms of cleanliness.

It's important to note that the aggregation methods are `Polars` implementations; we're not using Python methods, meaning they're optimized for working with `Polars` DataFrame objects.

## 4. Joins
`Polars` supports several join strategies by specifying the `strategy` argument. The main strategies are:
-   `inner`: Produces a `DataFrame` that contains only the rows where the join key exists in both `DataFrames`.
-   `left`: Produces a `DataFrame` that contains all the rows from the left `DataFrame` and only the rows from the right `DataFrame` where the join key exists in the left `DataFrame`.
-   `outer`: Produces a `DataFrame` that contains all the rows from both `DataFrames`.
-   `cross`: Performs the cartesian product of the two `DataFrames`.

We can perform a join operation:

##### **Code**
```Python
# Declare dataframes
df_writers = pl.DataFrame(
        {
         'name' : ['Jack', 'Charles', 'Clarice'],
        'surname' : ['Kerouac', 'Bukowski', 'Lispector'],
        'birth' : [datetime(1922, 3, 12),
                   datetime(1920, 8, 16),
                   datetime(1920, 12, 10)]
        }
)

df_books = pl.DataFrame(
        {
         'name' : ['Jack', 'Charles', 'Clarice'],
        'surname' : ['Kerouac', 'Bukowski', 'Lispector'],
        'book' : ['On The Road',
                  'Ham On Rye',
                  'The Passion According to G.H.']
        }
)

# Join
df_writers = df_writers.join(df_books, on=['name', 'surname'], how="left")

# Print result
df_writers
```

##### **Output**
```
shape: (3, 4)
+---------+-----------+---------------------+-------------------------------+
| name    | surname   | birth               | book                          |
| ---     | ---       | ---                 | ---                           |
| str     | str       | datetime[μs]        | str                           |
+===========================================================================+
| Jack    | Kerouac   | 1922-03-12 00:00:00 | On The Road                   |
| Charles | Bukowski  | 1920-08-16 00:00:00 | Ham On Rye                    |
| Clarice | Lispector | 1920-12-10 00:00:00 | The Passion According to G.H. |
+---------+-----------+---------------------+-------------------------------+
```


---





---

# Conclusions
In this segment we've gone from zero to `Polars`; it's a lot to digest, but the important thing is that we covered the most relevant functionalities, and we can extend from here consulting external resources.

For those already familiar with `pandas`, there's this great [cheatsheet](https://www.rhosignal.com/posts/polars-pandas-cheatsheet/) which covers translations of the most relevant `polars` operations.

One disadvantage about `Polars`, is the lack of community discussing the library; `Pandas` is everywhere, all the time. Hopefully more people adopt `Polars` in the future.

---

# References
- [Polars Official Page, Home](https://www.pola.rs/)
- [Polars User Guide](https://pola-rs.github.io/polars-book/user-guide/)
- [Cheatsheet for Pandas to Polars](https://www.rhosignal.com/posts/polars-pandas-cheatsheet/)

---

# Copyright
Pablo Aguirre, Creative Commons Attribution 4.0 International, All Rights Reserved.