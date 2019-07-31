# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 10:14:21 2019

@author: STEM
"""

cadburryType1= "and 6 milk chocolates"
cadburryType2= "5 dark chocolates"
cadburryType3= "8 white chocolates"
def cadburrybox(m,d,w):
    print("there are ",m, ",", d, w, "in the box")

cadburrybox("8 white chocolates", "5 dark chocolates", "and 6 milk chocolates")

cadburryType1= "6 milk chocolates"
cadburryType2= "5 dark chocolates"
cadburryType3= "8 white chocolates"

cadburryType1= "and 6 milk chocolates"
cadburryType2= "5 dark chocolates"
cadburryType3= "8 white chocolates"
def cadburrybox(m,d,w):
    print("there are ",m, ",", d, w, "in the box")

cadburrybox(cadburryType2, cadburryType3, cadburryType1)


cad1 = "white"
cad2 = "dark"
cad3 = "milk"

chocolate1 = {"cadburrymilk": 6}
chocolate2 = {"cadburrydark": 5}
chocolate3 = {"cadburrywhite": 8}
print(chocolate1,chocolate2,chocolate3)

chocolatebox ={"dark":5, "milk":6, "white":8}
chocolatebox
#dictexample
name1 = "steve"
name2 = "lia"
name3 = "vin"
name4 = "katie"

age1 = {"steve": 32}
age2 = {"lia": 28}
age3 = {"vin": 45}
age4 = {"katie": 38}
print(age1,age2,age3,age4)

gender1 = {"steve": "male"}
gender2 = {"lia": "female"}
gender3 = {"vin": "male"}
gender4 = {"katie": "female"}
print(gender1,gender2,gender3,gender4)
print(name1,name2,name3,name4,age1,age2,age3,age4,gender1,gender2,gender3,gender4)

studentage ={"steve":32,"lia":28,"vin":45,"katie":38}
studentage

studentgender = {"steve":"M","lia:":"F","vin":"M","katie":"F"}
studentgender

#list:all data can go in one line

studentlist

import pandas
dir(pandas)

studentdf = pandas.DataFrame(studentlist,columns=("name","age","gender"))
studentdf["name"]

chocolatelist = [["milk" , 5],["dark" , 8],["white" , 3]]
chocodf = pandas.DataFrame(chocolatelist,columns=("chocolate", "quanity"))

import pandas
dir (pandas)

#how to create a data frame of information

chocolatelist = [["milk",5,],["dark",8,],["white",3,]]
chocolatelist

import pandas

chocolatelist = pandas.DataFrame(chocolatelist,columns=("type","quantity"))
chocolatelist

#bargraph
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]

plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('Usage')
plt.title('Programming language usage')

plt.show()
#plotingagraph
import plotly
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as graphobjects

studentlist = [['steve',32,'M'],["lia",28,"F"],["vin",45,"M"],["katie",38,"F"]]

studentdf = pandas.DataFrame(studentlist,columns=("name","age","gender"))

studentbar = graphobjects.Bar(x=studentdf["name"],y=studentdf["age"])
plot([studentbar])
#chocolate bargraph
import plotly
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as graphobjects

chocolatelist = [["milk",5,],["dark",8,],["white",3,]]

chocolatelist = pandas.DataFrame(chocolatelist,columns=("type","quantity"))
                   )
chocolatebar = graphobjects.Bar(x=chocolatelist["type"],y=chocolatelist["type"])
plot([chocolatebar])

titles = go.Layout(title = "number of chocolates by type")

fig = go.Figure(data=[chocolatebar], layout=titles)
plot(fig)












