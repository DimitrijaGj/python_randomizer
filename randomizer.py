#!/usr/local/bin/python3

import random
import pprint
import datetime

pprint.pprint("-"*70)
print("""     
      If You want to see the list of children type in Lista 
      If You want to add or delete dete type Manage
      If You want to create a List for Breakfast press Enter
      """)
pprint.pprint("-"*70)

### Variabli
deneska = datetime.date.today()
nxt_week = deneska + datetime.timedelta(weeks=1)
kw = nxt_week.isocalendar().week
deca = ["Alfi", "Bobby", "Slavco", "Bojan", "Slagjana", "Svetlana", "Stojanco"]


### Functions
def show_deca(deca):
    for broj,dete in enumerate(deca,start=1):
        print(f"{broj:<2} | {dete:>5}")
    with open ('lista.txt', 'w') as lista:
        lista.write('_'*25)
        lista.write("\n")
        for broj,dete in enumerate(deca,start=1):
            lista.write(f"{broj:<2} | {dete:>5}\n")
            lista.write("_"*25)
            lista.write("\n")
    print("Listata e aktuelizirana!")
    
def manage_deca():
    vnes = input("Za da dodate dete vnesete Add, za da odzemete vnesete Delete. Koj e Vasiot izbor?...")
    if vnes == "Add":
        new_dete = input("Napiseto go imeto na deteto ==>")
        deca.append(new_dete)
        show_deca(deca)
    if vnes == "Delete":
       out_dete = input("Koe dete sakate da go izbrisete ===>")
       deca.remove(out_dete)
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
    print("Listata e kreirana na ==>", deneska)
    print("Za slednata nedela: KW >>", kw)
    print("_"*40)
    for dete, produkt in lista:
        print(f"{dete:<10} | treba da kupi | {produkt:<15}")
        with open ('output.txt', 'w') as file:
            for item in lista:
                file.write(f"{item}\n")
    print("_"*40)
    
    with open('output.txt', 'w') as file:
        file.write("-" * 40 + "\n")
        file.write(f"Listata e kreirana na ==>{deneska}\n")
        file.write(f"Za slednata nedela: KW >> {kw}\n")
        file.write("_" * 40 + "\n")
        for dete, produkt in lista:
            file.write(f"{dete:<10} | treba da kupi | {produkt:<15}\n")
        file.write("_" * 40 + "\n")
### ?Main function part
def main():
    produkt=input("Vasiot izbor e ... (za da kreirate lista pritisnete Enter) ")
    if produkt == "Lista":
        show_deca(deca)
    elif produkt == "Manage":
        manage_deca()
    elif produkt == "Delete":
        remove_dete()    
    else:
        randomize()

if __name__ == "__main__":
    main()
