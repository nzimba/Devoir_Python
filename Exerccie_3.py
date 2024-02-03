#!/usr/bin/env python
# coding: utf-8

# # exercie 3

# In[4]:


## proposition 1

import sqlite3

def find_missing_number_and_store_1(numbers):
    x = min(numbers)
    y = max(numbers)
    expected_sum = (y*(y+1))//2 - ((x-1)*x)//2
    actual_sum = sum(numbers)
    missing_number = expected_sum - actual_sum

    conn = sqlite3.connect('missing_number.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS missing_numbers (number int)''')
    c.execute("INSERT INTO missing_numbers VALUES (?)", (missing_number,))
    conn.commit()
    conn.close()

    return missing_number


# In[5]:


##proposition 2

import sqlite3

def find_missing_number_and_store_2(numbers):
    x = min(numbers)
    y = max(numbers)
    full_list = list(range(x, y+1))
    missing_number = list(set(full_list) - set(numbers))[0]

    conn = sqlite3.connect('missing_number.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS missing_numbers (number int)''')
    c.execute("INSERT INTO missing_numbers VALUES (?)", (missing_number,))
    conn.commit()
    conn.close()

    return missing_number

