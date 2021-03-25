# takes ytplaylist.txt and creates a list of lists
import os

mylist=[]
list=[]

with open('ytplaylist.txt') as f:
    data=f.read().splitlines()
    result = [data[i:i+3] for i in range(0,len(data))]

print(result[0])
