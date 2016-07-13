#!/bin/python3

#thi code is comitted by Amila Sampath for
#for group code bank

import random
import sys
import os

n= int(input().strip())

if((n>20) and (n % 2 == 0)):
    print("Not Weird")
elif((n > 5) and (n <21) and (n % 2 == 0)):
    print("Weird")
elif((n > 1) and (n < 5) and (n % 2 == 0)):
    print("Not Weird")
else:
    print("Weird")
