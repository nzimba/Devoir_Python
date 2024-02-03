#!/usr/bin/env python
# coding: utf-8

# # exercice 1

# In[ ]:


#proposition 1

def transform(chain):
     chaine1 = liste[0]
     chaine2 = liste[1]
      entiers = set()
      for caractere in chaine1:
            if caractere.isdigit()
            entiers.add(int(caractere))
     # Parcourir chaque caractère de la deuxième chaîne
     for caractere in chaine2:
             if caractere.isdigit():
                     entiers.add(int(caractere))
     entiers_tries = sorted(list(entiers))
     nouvelle_chaine = ''.join(str(entier) for entier in entiers_tries)
     nouvelle_chaine += "NZIMBA_BENI_Master1AI"
     return nouvelle_chaine


# In[13]:


# proposition 2

def transform(liste_chaines):
    # Extraire les entiers de chaque chaîne
    entiers_chaine1 = set(map(int, liste_chaines[0].split()))
    entiers_chaine2 = set(map(int, liste_chaines[1].split()))

    # Fusionner les ensembles d'entiers sans doublons
    entiers_fusionnes = sorted(entiers_chaine1 | entiers_chaine2)

    # Créer la nouvelle chaîne de caractères
    nouvelle_chaine = ''.join(str(entier) for entier in entiers_fusionnes)

    # Ajouter votre nom, prénom et classe à la fin
    nouvelle_chaine += "NZIMBA_BENI_Master1AI"

    return nouvelle_chaine


# In[ ]:





# In[ ]:




