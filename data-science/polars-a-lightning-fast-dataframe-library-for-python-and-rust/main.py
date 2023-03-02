# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:38:05 2023

@author: pablo

GitHub: https://github.com/pabloagn
Website: https://pabloagn.com
Contact: https://pabloagn.com/contact

Part of Deep Dive: polars-a-lightning-fast-dataframe-library-for-python-and-rust
"""

# Import modules
import polars as pl
import pandas as pd
import numpy as np
import pyarrow
import os
import re
import glob
from datetime import datetime

# Import bonus modules
import folium
from folium.plugins import FastMarkerCluster

rDir = 'datasets/'
wDir = 'outputs/'

# Printing polars version
print(pl.__version__)

# Polars data structures
# --------------------------

# Declare series
se = pl.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Check type
type(se)

se

# Declare DataFrame
df = pl.DataFrame({'name' : ['Jack', 'Charles', 'Clarice'],
                   'surname' : ['Kerouac', 'Bukowski', 'Lispector'],
                   'birth' : [datetime(1922, 3, 12),
                              datetime(1920, 8, 16),
                              datetime(1920, 12, 10)]
                   })

# Print object
df

# Eager Execution
# --------------------------

# Reading a csv file
df = pl.read_csv(os.path.join(rDir, 'berlin_weekends.csv'))

# Exploring our DataFrame type
type(df)


# Lazy Execution
# --------------------------

# Reading a csv file using pl.scan_csv()
df_s = pl.scan_csv(os.path.join(rDir, 'berlin_weekends.csv'))

# Reading a csv file using pl.read_csv().lazy()
df_l = pl.read_csv(os.path.join(rDir, 'berlin_weekends.csv')).lazy()

# Check types
type(df_s), type(df_l)

# Check head
df_s.head()

# View graph
df_s.show_graph()

# Perform additional operations to lazy object
df_s_filtered = (df_s.filter(pl.col("bedrooms") >= 2).
                select(pl.col("metro_dist")).
                sort("metro_dist")
                )

# Show graph again
df_s_filtered.show_graph()

# Show optimized plan in text format
df_s_filtered.describe_optimized_plan()

# Collect the object
df_s_filtered.collect()

# Reading and writing multiple file formats
# --------------------------

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


# Write
# --------------------------

# # Write to csv
# df_weekdays.write_csv(os.path.join(wDir, 'weekdays.csv'))

# # Write to Parquet non-partitioned
# df_weekdays.write_parquet(os.path.join(wDir, 'weekdays.parquet'))

# # Write to Avro
# df_weekdays.write_avro(os.path.join(wDir, 'weekdays.avro'))

# # Write to JSON
# df_weekdays.write_json(os.path.join(wDir, 'weekdays.json'))


# Read
# --------------------------

# Write to csv
df_weekdays_csv = pl.read_csv(os.path.join(wDir, 'weekdays.csv'))

# Write to Parquet non-partitioned
df_weekdays_parquet = pl.read_parquet(os.path.join(wDir, 'weekdays.parquet'))

# Write to Avro
df_weekdays_avro = pl.read_avro(os.path.join(wDir, 'weekdays.avro'))

# Write to JSON
df_weekdays_json = pl.read_json(os.path.join(wDir, 'weekdays.json'))


# Confirm reading
# --------------------------

df_weekdays_csv['realSum'].head(10)
df_weekdays_parquet['realSum'].head(10)
df_weekdays_avro['realSum'].head(10)
df_weekdays_json['realSum'].head(10)


# Basic operations
# --------------------------

# Exploring our DataFrame contents
df.shape
df.columns
df['realSum'].head(10)
df['realSum'].tail(10)
df.describe()
df.sample(5)


# Selecting
df.select(pl.col("realSum"))

# Selecting using RegEx
df.select(pl.col("^room.*$"))

# Selecting all
df.select(pl.col("*"))

# Selecting all except
df.select(pl.exclude("realSum"))

# Select based on column dtype
df.select(pl.col(pl.Int64))

# Filtering
(df.filter(pl.col("bedrooms") >= 2).
 select(pl.col("metro_dist")).
 sort("metro_dist").
 head(5)
)

# Multiple filtering
berlin_places = (df.filter((pl.col("person_capacity") == 2) &
                           (pl.col("bedrooms")) == 1).
                 sort('cleanliness_rating', descending = True).
                 head(10)
                 )

# # Creating a folium map, initializing view with first item
# berlin_map = folium.Map(
#     location=[berlin_places[0]['lat'][0], berlin_places[0]['lng'][0]],
#     tiles='cartodbpositron',
#     zoom_start=12,
# )

# # Adding remaining coordinates
# FastMarkerCluster(data=list(zip(berlin_places['lat'], berlin_places['lng']))).add_to(berlin_map)

# # Export map to HTML file and visualize using any browser
# berlin_map.save(os.path.join(wDir, 'berlin_places.html'))

# Filtering with advanced operators

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

# Aggregations
(df.groupby(['room_shared'], maintain_order=True).
    agg(pl.col("cleanliness_rating").mean())
    )

# Joins
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

# Concatenate

# Read two different DataFrames
df_berlin = pl.read_csv(os.path.join(rDir, 'berlin_weekends.csv'))
df_vienna = pl.read_csv(os.path.join(rDir, 'vienna_weekends.csv'))

# Add city column to each one
df_berlin = (df_berlin.
             with_columns(pl.lit('Berlin').
             alias('city'))
             )

df_vienna = (df_vienna.
             with_columns(pl.lit('Vienna').
             alias('city'))
             )

# Concatenate them on vertical axis
df_berlin_vienna = pl.concat([df_berlin, df_vienna])

# Due to SchemaError, we need to cast data type from column person_capacity
df_vienna = df_vienna.with_columns(pl.col("person_capacity").cast(pl.Int64))

# Try concatenation again
df_berlin_vienna = pl.concat([df_berlin, df_vienna])

# Display resulting dataframe unique cities
(df_berlin_vienna.groupby(['city'], maintain_order=True).
 agg(pl.col('lat').n_unique().
     alias('unique_latitudes')
     )
 )

# Creating new column from numpy array
# Define a numpy array of ones
new_col = np.random.random([len(df)])

# Assign new column to dataframe
df = df.with_columns(pl.Series(name="new_col", values=new_col))

print(df[:,-3:])

# Creating new column from aggregation
(df.groupby(['room_shared'], maintain_order=True).
 agg(pl.col('cleanliness_rating').mean().
     alias('average_cleanliness')
     )
 )

# Schemas and Data Types
# --------------------------

# Define schema
schema = {'' : pl.Int64,
          'realSum' : pl.Float64,
          'room_type' : pl.Utf8,
          'room_shared' : pl.Boolean,
          'room_private' : pl.Boolean,
          'person_capacity' : pl.Int64,
          'host_is_superhost' : pl.Boolean,
          'multi' : pl.Int64,
          'biz' : pl.Int64,
          'cleanliness_rating' : pl.Float64,
          'guest_satisfaction_overall' : pl.Float64,
          'bedrooms' : pl.Int64,
          'dist' : pl.Float64,
          'metro_dist' : pl.Float64,
          'attr_index' : pl.Float64,
          'attr_index_norm' : pl.Float64,
          'rest_index' : pl.Float64,
          'rest_index_norm' : pl.Float64,
          'lng' : pl.Float64,
          'lat' : pl.Float64,
          'strict' : pl.Boolean,
 }

# Read dataframe
# df = pl.read_csv(os.path.join(rDir, 'vienna_weekends.csv'), dtypes = schema)

# Load Vienna data set without infering schema
df = pl.read_csv(os.path.join(rDir, 'vienna_weekends.csv'), infer_schema_length=0)

# Iteratively cast data types
# for i, x in schema.items():
#     df = df.with_columns(pl.col(i).cast(x), strict = False)

# Iteratively cast data types
for i, x in schema.items():
    try:
        df = df.with_columns(pl.col(i).cast(x), strict = False)
        
        # If we encounter a boolean lowercased column, we need to treat it specially
    except:
        df = df.with_columns(pl.col(i)=='true')

# Cast data types
df = (pl.read_csv(os.path.join(rDir, 'vienna_weekends.csv'), infer_schema_length=0).
      with_columns(pl.all().cast(schema.values(), strict=False)))

# Schemas and Data Types
# --------------------------







