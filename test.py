from tabulate import tabulate

# d = [ ["Mark", 12, 95],
#      ["Jay", 11, 88],
#      ["Jack", 14, 90]]

# print(tabulate(d, headers=["Sobrou", "Quantia"]))

quantiaAcucar = 2
quantiaArroz = 4

sobras = [
    ["Açucar", quantiaAcucar], 
    ["Arroz", quantiaArroz] ]
    # quantiaArroz, 
    # quantiaCafe, 
    # quantiaExtrato, 
    # quantiaMacarrao, 
    # quantiaOleo, 
    # quantiaFtrigo, 
    # quantiaFeijao, 
    # quantiaSal]

for i in sobras:
     for b in i:
          if b > 0:
               print(tabulate(sobras, headers=["Sobrou", "Quantia"]))