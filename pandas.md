# pandas
pandas (all lower-case) is a Python package to work with tabular data, such as 
spreadsheets and databases.  There are lots of ways to do things in pandas, 
and there is a "cookbook" to assist with determining how to do what is 
wanted.  Rather than going through the various recipes, this document will 
discuss the package overview.

Two critical imports are:  
* `import numpy as np`
* `import pandas as pd`

pandas is well suited for different kinds of data:
* Tabular data, provided the data is heterogenous in each column
* Ordered and unordered time series data
* Arbitrary matrix data with labeled rows and columns
* Other forms of statistical data sets

Two types of data structures that handle most typical use cases across 
different fields of study are:
* Series (1-dimensional)
* DataFrame (2-dimensional)
  * DataFrame is abbreviated as `df` in code

Among the many things pandas can do:
* Handle missing data (represented as NaN)
* Insert and delete columns from DataFrame
* Data alignment, both automatic and explicit or aligned via computations
* Merging and joining data sets



##### Source: [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html)
* Getting Started: index
* Getting Started: Package overview