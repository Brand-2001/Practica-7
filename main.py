import json
#agregamos los datos nuevos
#data={"data":[{"cedula":"28316888","nombre":"Brandon","apellido":"Gaitan","nota1":"20","nota2":"20","nota1":"18"},{"cedula":"28316887","nombre":"Juanito","apellido":"Alcachofa","nota1":"20","nota2":"20","nota1":"20"}]}
#abrimos el archivo y extraemos los datos
#with open('data.json', 'r') as archivo_json:

#por temas de que no compila de la manera correcta no ingresarlos al codigo porque borra todo pero no agrega

#teoricamente debias juntarse csa que no paso
#    datos_existentes = json.load(archivo_json)
#datos_existentes["data"].extend(data["data"])
#datos_combinados = {"data": datos_existentes["data"] + data["data"]}
#generar el nuevo archivo con todo
#with open('data.json', 'w') as archivo_json:
#    json.dump(datos_existentes, archivo_json, indent=6)


#llamamos al archivo y decimos que cargue sus datos en el programa
with open("data.json","r") as file:
    data=json.load(file)
#busca los valores y los imprime
for estudiante in data["data"]:
    print("Cedula: "+str(estudiante["cedula"])+"\nNombre: "+str(estudiante["nombre"])+"\nApellido: "+str(estudiante["apellido"])+"\nNota: "+str(estudiante["nota1"])+"\nNota: "+str(estudiante["nota2"])+"\nNota: "+str(estudiante["nota3"]))
