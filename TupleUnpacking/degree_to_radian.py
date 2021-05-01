
import numpy as np
import math
import csv

input =[]


# Open and read csv file line by line
with open('csvInput.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    # print("Data",data)

# convert each element of list to int and append to empty list 'input'
    for k in data:
        i=0
        input.append([int(i) for i in k])    
                
input_list = list(input)

new = []
for l in data:
    new.append([x.split(',') for x in l ])

#  Function to convert to radian to degree
"""Input: list of list (in degree) as input parameter (passed using tuple unpacking)
   Outout: list in radians"""
def degree_to_radian(*argv):
   
    for arg in argv:
       # print(f'Degree in radian of the {arg} : {np.radians(arg)}')
       print("Input file as Degree:",arg)
       print("Output in Radian:", np.radians(arg))
        
# Function call
degree_to_radian(input_list)
