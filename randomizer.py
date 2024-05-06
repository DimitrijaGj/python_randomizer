#!/usr/local/bin/python3

import random
import pprint

pprint.pprint("-"*70)
print("""     
      If You want to see the list of children type in Lista 
      If You want to add dete to deca type Add
      If You want to delete a dete type Delete
      If You want to create a List for Breakfast press Enter
      """)
pprint.pprint("-"*70)

deca = ["Alfi", "Bobby", "Slavco", "Bojan", "Slagjana", "Svetlana", "Stojanco"]

def show_deca(deca):
    for broj,dete in enumerate(deca,start=1):
        print(f"{broj:<2} | {dete:>5}")

def add_dete():
    new_dete = input("Napiseto go imeto na deteto ==>")
    deca.append(new_dete)
    show_deca(deca)

def randomize():
    #print(len(deca))
    x = len(deca)
    produkti = []
    dete = []
    while x != len(produkti):
        produkt=input("Pisi go produktot ")
        produkti.append(produkt)
        for y in random.sample(deca, x):
               dete.append(y)        
    lista = list(zip(dete, produkti))
    print("-"*40)
    print("Za slednata nedela: ")
    print("_"*40)
    for dete, produkt in lista:
        print(f"{dete:<10} | treba da kupi | {produkt:<15}")

    print("-"*40)
    
def main():
    produkt=input("Vasiot izbor e ... (za da kreirate lista pritisnete Enter) ")
    if produkt == "Lista":
        show_deca(deca)
    elif produkt == "Add":
        add_dete()
    else:
        randomize()

if __name__ == "__main__":
    main()
    


