# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 13:54:41 2020

@author: utilisateur
"""

import requests

# -----------------------------------------------------------------------------
# Ex 1 :Lister les 10 derniers livres par leur date de publication
# -----------------------------------------------------------------------------

url = 'https://demo.api-platform.com/books?order[publicationDate]=desc&page=1'
r = requests.get(url).json()
list_book = r['hydra:member'][:10]

for i in range(len(list_book)):
    print('Auteur : ', list_book[i]['author'])
    print('Titre : ', list_book[i]['title'])
    print('Date de parution : ', list_book[i]['publicationDate'])
    print()

# -----------------------------------------------------------------------------    
# Ex 2 : Lister le livre écrit par l’auteur « Dr. Kaitlyn Ratke »
# -----------------------------------------------------------------------------

url = 'https://demo.api-platform.com/books?author=Dr.%20Kaitlyn%20Ratke'
r = requests.get(url).json()
list_book = r['hydra:member']

for i in range(len(list_book)):
    print('Auteur : ', list_book[i]['author'])
    print('Titre : ', list_book[i]['title'])
    print('Date de parution : ', list_book[i]['publicationDate'])
    print()

#------------------------------------------------------------------------------
# Ex 3 : Lister tous les commentaires du livre dont l’id est « 1d52ba85-97c8-4cc3-b81a-40582f3aff64 »
#------------------------------------------------------------------------------

url = 'https://demo.api-platform.com/books/1d52ba85-97c8-4cc3-b81a-40582f3aff64'
r = requests.get(url).json()
list_book = r['reviews']

for i in range(len(list_book)):
    print('Commantaire : ', list_book[i]['body'])
    print()

#------------------------------------------------------------------------------
# Ex 4 : Créer un nouveau commentaire avec le texte et la note de votre choix pour le livre dont l'id est « 1b08c9ab-6254-4015-ad14-bac3e5c008df »
#------------------------------------------------------------------------------

url = 'https://demo.api-platform.com/reviews'

review = {
  "body": "J'aimerais tuer mon voisin de gauche, il me fait peur !",
  "rating": 2,
  "author": "LVVN",
  "book": "books/1b08c9ab-6254-4015-ad14-bac3e5c008df"  
}

r = requests.post(url, json = review)
review_id = r.json()
print('id : ' , review_id.get('@id'))

# -----------------------------------------------------------------------------
# Exo 5 : Modifier votre nouveau commentaire en utilisant l’id qui vous a été fourni lors de sa création
# -----------------------------------------------------------------------------

url = 'https://demo.api-platform.com/reviews/937ba331-b476-4166-ad5e-5b789a312543'

review = {
  "body": "J'aimerais impressionner mon voisin de gauche et reussir cet exo !",
  "rating": 2,
  "author": "LVVN",
  "book": "books/1b08c9ab-6254-4015-ad14-bac3e5c008df"  
}


r = requests.patch(url, json = review , headers={'Content-Type':'application/merge-patch+json'})
print(r)