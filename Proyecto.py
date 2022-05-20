import csv

#lee el archivo de características de UGAS y busca las características con esos elementos en la lista de criterios. Genera un archivo nuevo con
#el nombre de la UGA y la asignación

#import pprint

#criterios_list = list()
#caracteristicas_list = list()
Dict_Caracteristicas = {}

#class Criterio:
 #   def __init__(self, clave, disponibilidad):
  #      self.clave = clave
   #     self.disponibilidad = disponibilidad

with open('Criterios_Ag.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
 #       criterios_list.append(row)
        #va celda por celda en en archivo de criterios.
        for caracteristica in row.keys():
            if caracteristica == 'Clave' or caracteristica == 'Descripcion':
                continue
            value = row[caracteristica]
           #elimina espacios antes o después del string
            value = value.strip()
            if value == '':
                continue
            #si la celda no está vacía, crea una lista vacía dentro del diccionario
            if caracteristica not in Dict_Caracteristicas:
                Dict_Caracteristicas[caracteristica] = list()
            Dict_Caracteristicas[caracteristica].append(row)


Dict_salida = {}

with open('Caracteristicas_UGAs.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
#        caracteristicas_list.append(row)
        for caracteristica in row.keys():
            if caracteristica == 'CLV_UGA':
                continue
            value = row[caracteristica]
            value = value.strip()
            if caracteristica not in Dict_Caracteristicas:
                continue
            criterios_ref_caract = Dict_Caracteristicas[caracteristica]
            for criterio in criterios_ref_caract:
                if value in criterio[caracteristica]:
                    nombre = row['CLV_UGA']
                    if nombre not in Dict_salida:
                        Dict_salida[nombre] = list()
                    Dict_salida[nombre].append(criterio['Clave'])

for key in Dict_salida.keys():
    Dict_salida[key] = set(Dict_salida[key])

new_file_list = list(Dict_salida.items())
#pprint.pprint(Dict_salida)

with open('asignacion_UGAs.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)
#writerows solo acepta listas, no diccionarios
        csv_writer.writerows(new_file_list)


  #      for row in csv_reader:
   #        caracteristicas_list.append(row)

#        csv_writer.writerows(row[0])

