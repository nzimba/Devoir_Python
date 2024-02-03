#!/usr/bin/env python
# coding: utf-8

# # Exercice 2

# In[7]:


# Programme alternatif
def create_lists():
    lst1    = []
    lst2    = []
    o       = []
    e       = []
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

    # Création de lst1
    for i in range(1200, 2000, 135):
        lst1.append(i)

    # Création de lst2 (en multipliant par 2)
    for num in lst1:
        if num % 2 == 0:
            lst2.append(num * 2)

    # Création de o et e
    for num in numbers:
        if num % 2 == 0:
            o.append(num)
        else:
            e.append(num)

    return lst1, lst2, o, e

# Appel de la fonction et affichage des résultats
lst1, lst2, o, e = create_lists()
print("lst1:", lst1)
print("lst2:", lst2)
print("o:", o)
print("e:", e)


# In[8]:


import operator
lst1 = list(range(1200, 2000, 135)) # (1)
lst2 = [i * 2 for i in lst1 if i % 2 == 0] # (2)
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
o = list(filter(lambda x: operator.mod(x, 2) == 0, numbers))
e = list(filter(lambda x: operator.mod(x, 2) != 0, numbers))
print(lst1)
print(lst2)
print(o)
print(e)


# In[ ]:




