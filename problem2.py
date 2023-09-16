def fonksiyon(y):
    if y == 0:
        liste.append("a")
    elif y == "1":
        liste.append("b")
    elif y =="2":
        liste.append("c")
    elif y == "3":
        liste.append("d")     
    elif y == "4":
        liste.append("e")
    elif y == "5":
        liste.append("f")
    elif y == "6":
        liste.append("g")
    elif y == "7":
        liste.append("h")
    elif y== "8":
        liste.append("i")
    elif y == "9":
        liste.append("j")
    
        
liste = []

sayı_girisi=input("sayı girişi yapınız:")

for i in sayı_girisi:
    fonksiyon(i)
print("".join(liste))