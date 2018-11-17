"""
Pandas is a high-level data manipulation tool developed by Wes McKinney.
It is built on the Numpy package and its key data structure is called the DataFrame.
DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables.
"""

# There are several ways to create a DataFrame. One way is to create a dictionary(hash)
dict = {
        "country": [
            "Brazil",
            "Russia",
            "India",
            "China",
            "South Africa"
        ],
        "capital": [
            "Brasilla",
            "Moscow",
            "New Dehli",
            "Beijing",
            "Pretoria"
        ],
        "area": [
            8.516,
            17.10,
            3.286,
            9.597,
            1.221
        ],
        "population": [
            200.4,
            143.5,
            1252,
            1357,
            52.98
        ]
}

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

# Pandas has assigned a key for each country as the numerical values 0 through 4.
# We can change them to have different index values. We can change them to their two letter country code.
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

# Another way to create a DataFrame is by importing a csv file using Pandas.
# Import game_high_points.csv *Worked but took out path*
points = pd.read_csv('/game_high_points.csv')

# Print out points
print(points)

# We can index a DataFrame by using the square bracket notation.
# We are going to select one column of the points DataFrame by using the square brackets.
# We can use a single bracket or double brackets:
## Single bracket - outputs a Pandas Series.
## Double brackets outputs a Pandas DataFrame.

print(points["Team"]) 
# Output Results:
# 0      Lakers
# 1       Bulls
# 2        Suns
# 3    Warriors
# 4     Rockets
# 5    Warriors
# 6        Heat
# Name: Team, dtype: object

print(points[["Team"]]) 
# Output Results:
#        Team
# 0    Lakers
# 1     Bulls
# 2      Suns
# 3  Warriors
# 4   Rockets
# 5  Warriors
# 6      Heat

print(points[['Team','Points']])
# Output Results:
#        Team  Points
# 0    Lakers      81
# 1     Bulls      69
# 2      Suns      70
# 3  Warriors     100
# 4   Rockets      60
# 5  Warriors      60
# 6      Heat      61

# Square brackets can also be used to access observations (rows) from a DataFrame.

# Print out first 4 observations
print(points[0:4])
# Output Results:
#                Name      Team  Points
# 0       Kobe Bryant    Lakers      81
# 1    Michael Jordan     Bulls      69
# 2      Devin Booker      Suns      70
# 3  Wilt Chamberlain  Warriors     100

# Prints out 3rd, 4th and 5th observation(row) *Index[2,3,4]
print(points[2:5])
# Output Results:
#                Name      Team  Points
# 2      Devin Booker      Suns      70
# 3  Wilt Chamberlain  Warriors     100
# 4      James Harden   Rockets      60

# We can also use "loc" and "iloc" to perform any data selection operation.
# "loc" is label-based, which means that we have to specify rows and columns based on their row and column labels.
# "iloc" is integer index based, so we have to specify rows and columns by thier integer index. Like how we just did...

# Print out observation for Devin Booker (Index 2)
print(points.iloc[2])
# Output Results:
# Name      Devin Booker
# Team              Suns
# Points              70
# Name: 2, dtype: object

# Print out observations for Kobe(index 0) and LeBron(index 6)
print(points.loc[[0,6]])
# Output Results:
#            Name    Team  Points
# 0   Kobe Bryant  Lakers      81
# 6  LeBron James    Heat      61
