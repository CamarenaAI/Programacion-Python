# Avoiding Index Errors When Working with Lists
"""
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles[3])

This example results in an index error:
Traceback (most recent call last):
 File "motorcycles.py", line 3, in <module>
 print(motorcycles[3])
IndexError: list index out of range 
"""

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])

"""
motorcycles = [] 
print(motorcycles[-1])

No items are in motorcycles, so Python returns another index error:
Traceback (most recent call last): 
 File "motorcyles.py", line 3, in <module> 
 print(motorcycles[-1]) 
IndexError: list index out of range
"""