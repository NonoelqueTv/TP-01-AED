#Entrada: Datos del paciente, el código ICD10 que identifica la enfermedad (o sea, el diagnóstico) y el monto base
nombre_del_paciente = input("Ingrese el nombre del paciente: ")
codigo_ice10 = input("Ingrese el codigo del ICD10: ")
monto_base = int(input("Ingrese el monto base a pagar: "))

#Variables para los condicionales
a_l = "ABCDEFGHIJKL"
m_z = "MNOPQRSTVWXYZ"
u = "U"
descripcion = ""
total = 0
primeros_3_carcteres = codigo_ice10[0] + codigo_ice10[1] + codigo_ice10[2]
monto_base += 25000
codigo_valido = True

#Requerimientos y posibles salidas:
if len(codigo_ice10) == 5 or len(codigo_ice10) == 6:
    if codigo_ice10[3] == ".":
        if primeros_3_carcteres[0] in a_l:
            monto_agregado = monto_base + 25000
            total = ((int(codigo_ice10[4:]) * monto_agregado) / 100) + monto_agregado
            if primeros_3_carcteres[0] == "A" or primeros_3_carcteres[0] == "B":
                descripcion = "Ciertas enfermedades infecciosas y parasitarias"
            elif primeros_3_carcteres[0] == "C":
                descripcion = "Tumores [neoplasias]"
            elif primeros_3_carcteres == "D49": #Excepción de D
                print("No se registra en el ICD10")
                codigo_valido = False
            elif primeros_3_carcteres[0] == "D" and "0" <= primeros_3_carcteres[1] <= "4":
                descripcion = "Tumores [neoplasias]"
            elif primeros_3_carcteres[0] == "D" and codigo_ice10[1] >= "5" and codigo_ice10[1] != "9":
                descripcion = "Enfermedades de la sangre y de los órganos hematopoyéticos, y ciertos trastornos que afectan el mecanismo de la inmunidad"
            elif primeros_3_carcteres == "E91" or primeros_3_carcteres == "E92" or primeros_3_carcteres == "E93" or primeros_3_carcteres == "E94" or primeros_3_carcteres == "E95" or primeros_3_carcteres == "E96" or primeros_3_carcteres == "E97" or primeros_3_carcteres == "E98" or primeros_3_carcteres == "E99": #Excepciones de E
                print("No se registra en el ICD10")
                codigo_valido = False
            elif primeros_3_carcteres[0] == "E":
                descripcion = "Enfermedades endocrinas, nutricionales y metabólicas"
            elif primeros_3_carcteres[0] == "F":
                descripcion = "Trastornos mentales y del comportamiento"
            elif primeros_3_carcteres[0] == "G":
                descripcion = "Enfermedades del sistema nervioso"
            elif primeros_3_carcteres == "H96" or primeros_3_carcteres == "H97" or primeros_3_carcteres == "H98" or primeros_3_carcteres == "H99": #Excepciones de H
                print("No se registra en el ICD10")
                codigo_valido = False
            elif primeros_3_carcteres[0] == "H" and "0" <= primeros_3_carcteres[1] <= "5":
                descripcion = "Enfermedades del ojo y sus anexos"
            elif primeros_3_carcteres[0] == "H" and codigo_ice10[1] >= "6":
                descripcion = "Enfermedades del oído y de la apófisis mastoides"
            elif codigo_ice10[0] == "I":
                descripcion = "Enfermedades del sistema circulatorio"
            elif codigo_ice10[0] == "J":
                descripcion = "Enfermedades del sistema respiratorio"
            elif primeros_3_carcteres == "K94" or primeros_3_carcteres == "K95" or primeros_3_carcteres == "K96" or primeros_3_carcteres == "K97" or primeros_3_carcteres == "K98" or primeros_3_carcteres == "K99": #Excepciones de K
                print("No se registra en el ICD10")
                codigo_valido = False
            elif codigo_ice10[0] == "K":
                descripcion = "Enfermedades del sistema digestivo"
            elif codigo_ice10[0] == "L":
                descripcion = "Enfermedades de la piel y del tejido subcutáneo"
        elif primeros_3_carcteres[0] in m_z:
            monto_agregado = monto_base + 40000
            total = ((int(codigo_ice10[4:]) * monto_agregado) / 100) + monto_agregado
            if codigo_ice10[0] == "M":
                descripcion = "Enfermedades del sistema osteomuscular y del tejido conjuntivo"
            elif codigo_ice10[0] == "N":
                descripcion = "Enfermedades del sistema genitourinario"
            elif codigo_ice10[0] == "O":
                descripcion = "Embarazo, parto y puerperio"
            elif primeros_3_carcteres == "P97" or primeros_3_carcteres == "P98" or primeros_3_carcteres == "P99": #Excepciones de P
                print("No se registra en el ICD10")
                codigo_valido = False
            elif codigo_ice10[0] == "P":
                descripcion = "Ciertas afecciones originadas en el período perinatal"
            elif codigo_ice10[0] == "Q":
                descripcion = "Malformaciones congénitas, deformidades y anomalías cromosómicas"
            elif codigo_ice10[0] == "R":
                descripcion = "Síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte"
            elif primeros_3_carcteres == "T99":  # Excepciones de T
                print("No se registra en el ICD10")
                codigo_valido = False
            elif codigo_ice10[0] == "S" or codigo_ice10[0] == "T":
                descripcion = "Traumatismos, envenenamientos y algunas otras consecuencias de causas externas"
            elif primeros_3_carcteres == "Y99":  # Excepciones de T
                print("No se registra en el ICD10")
                codigo_valido = False
            elif codigo_ice10[0] == "V" or codigo_ice10[0] == "W" or codigo_ice10[0] == "X" or codigo_ice10[0] == "Y":
                descripcion = "Causas externas de morbilidad y de mortalidad"
            elif codigo_ice10[0] == "Z":
                descripcion = "Factores que influyen en el estado de salud y contacto con los servicios de salud"
        elif primeros_3_carcteres[0] in u:
            monto_agregado = monto_base + 100000
            total = ((int(codigo_ice10[4:]) * monto_agregado) / 100) + monto_agregado
            descripcion= "Códigos para propósitos especiales"
        else:
            print("Codigo no valido")
            codigo_valido = False
    else:
        print("Los codigos ICD10 llevan punto (.)")
        codigo_valido = False
else:
    print("No se registra en el ICD10")
    codigo_valido = False

#Salidas
if codigo_valido == True:
    print("Beneficiario: ",nombre_del_paciente)
    print("Codigo: ",codigo_ice10)
    print("Capítulo: ",descripcion)
    print("Monto a pagar: ",total)



