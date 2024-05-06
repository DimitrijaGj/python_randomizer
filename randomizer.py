#!/usr/local/bin/python3

import random

print("""
      If You want to see the list of children type in Lista 
      If You want to add dete to deca type Add
      
      """)
deca = ("Alfi", "Bobby", "Slavco", "Bojan", "Slagjana", "Svetlana", "Stojanco")

def show_deca(deca):
    print(deca)

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
    produkt=input("Pisi go produktot tuka ")
    if produkt == "Lista":
        show_deca(deca)
    else:
        randomize()
    
if __name__ == "__main__":
    main()
    


