import wbgapi as wb  
import pandas as pd  
import matplotlib.pyplot as plt
import plotly.express as px


pais_input = input("Pais a buscar: ")
pais = wb.economy.info(q=pais_input)

print(pais)

id_input = input("Seleccione el id: ")



data_list = []
choice = 0

tema_input = str(input("Variable a buscar: "))
tema = wb.series.list(q=tema_input)

for id in tema:
    id_title = id["id"]
    data_list.append(id_title)
    print(str(choice) + ": " + str(id["value"]))
    choice = choice + 1

selection = int(input("Seleccione el indicador deseado: "))

año_inicio = int(input("Seleccione el año de inicio: "))
año_final = int(input("Seleccione el año final: "))

data = wb.data.DataFrame(data_list[selection], id_input, range(año_inicio, año_final), index="time",numericTimeKeys=True, 
                         labels=True).plot(figsize=(10, 6))

plt.title(str(id["value"]))

plt.show()





