#!/usr/local/bin/python3

import random
import pprint
import datetime

pprint.pprint("-"*70)
print("""     
      Chose Your options:
      To edit List of Children type 1
      To edit list of Items for Breakfast type 2
      To assign Item to Children Type 3
      """)
pprint.pprint("-"*70)

### Variabli
deneska = datetime.date.today()
nxt_week = deneska + datetime.timedelta(weeks=1)
kw = nxt_week.isocalendar().week
deca = ["Alfi", "Bobby", "Slavco", "Bojan", "Slagjana", "Svetlana", "Stojanco"]
children = []

### Functions
def list_children():
    
    while True:
        child = input('Plese enter childs name or Type done to finish ... ')
        if child.lower() == "done":
            break
        children.append(child)
    print(children)
    with open ('children_list.txt', 'w') as children_list:
        children_list.write('_'*25)
        children_list.write("\n")
        for number,child in enumerate(children,start=1):
            children_list.write(f"{number:<2} | {child:>5}\n")
            children_list.write("_"*25)
            children_list.write("\n")
        children_list.write(f'List is updated on ==> {deneska} \n')
    print("List is updated!")
    
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
    children_list = list(zip(dete, produkti))
    print("-"*40)
    print("children_listta e kreirana na ==>", deneska)
    print("Za slednata nedela: KW >>", kw)
    print("_"*40)
    for dete, produkt in children_list:
        print(f"{dete:<10} | treba da kupi | {produkt:<15}")
        with open ('output.txt', 'w') as file:
            for item in children_list:
                file.write(f"{item}\n")
    print("_"*40)
    
    with open('output.txt', 'w') as file:
        file.write("-" * 40 + "\n")
        file.write(f"children_listta e kreirana na ==>{deneska}\n")
        file.write(f"Za slednata nedela: KW >> {kw}\n")
        file.write("_" * 40 + "\n")
        for dete, produkt in children_list:
            file.write(f"{dete:<10} | treba da kupi | {produkt:<15}\n")
        file.write("_" * 40 + "\n")
### ?Main function part
def main():
    option=int(input("What is Your option, please enter number... "))
    if option == 1:
        list_children()
    elif option == "Manage":
        manage_deca()
    else:
        randomize()

if __name__ == "__main__":
    main()
