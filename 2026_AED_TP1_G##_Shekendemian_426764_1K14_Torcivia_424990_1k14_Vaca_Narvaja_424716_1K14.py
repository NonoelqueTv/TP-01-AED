#Entrada: Datos del paciente, el código ICD10 que identifica la enfermedad (o sea, el diagnóstico) y el monto base
nombre_del_paciente = input("Ingrese el nombre del paciente: ")
codigo_ice10 = input("Ingrese el codigo del ICD10: ")
monto_base = int(input("Ingrese el monto base a pagar: "))

monto_base += 25000

#Variables para los condicionales
a_l = "ABCDEFGHIJKL"
m_z = "MNOPQRSTVWXYZ"
u = "U"
descripcion = ""
total = 0
primer_caracter = codigo_ice10[0]
primeros_3_carcteres = codigo_ice10[0] + codigo_ice10[1] + codigo_ice10[2]
codigo_valido = True

#Requerimientos y posibles salidas:
if len(codigo_ice10) == 5 or len(codigo_ice10) == 6:
    if codigo_ice10[3] == ".":
        if primer_caracter in a_l:
            monto_base = monto_base + 25000
            if primer_caracter == "A" or primer_caracter == "B":
                descripcion = "Ciertas enfermedades infecciosas y parasitarias"
            elif primer_caracter == "C":
                descripcion = "Tumores [neoplasias]"
            elif primeros_3_carcteres == "D49": #Excepción de D
                print("No se registra en el ICD10")
                codigo_valido = False
            elif primer_caracter == "D" and "0" <= codigo_ice10[1] <= "4":
                descripcion = "Tumores [neoplasias]"
            elif primer_caracter == "D" and codigo_ice10[1] >= "5" and codigo_ice10[1] != "9":
                descripcion = "Enfermedades de la sangre y de los órganos hematopoyéticos, y ciertos trastornos que afectan el mecanismo de la inmunidad"
            elif primeros_3_carcteres == "E91" or primeros_3_carcteres == "E92" or primeros_3_carcteres == "E93" or primeros_3_carcteres == "E94" or primeros_3_carcteres == "E95" or primeros_3_carcteres == "E96" or primeros_3_carcteres == "E97" or primeros_3_carcteres == "E98" or primeros_3_carcteres == "E99": #Excepciones de E
                print("No se registra en el ICD10")
                codigo_valido = False
            elif primer_caracter == "E":
                descripcion = "Enfermedades endocrinas, nutricionales y metabólicas"
            elif primer_caracter == "F":
                descripcion = "Trastornos mentales y del comportamiento"
            elif primer_caracter == "G":
                descripcion = "Enfermedades del sistema nervioso"
            elif primeros_3_carcteres == "H96" or primeros_3_carcteres == "H97" or primeros_3_carcteres == "H98" or primeros_3_carcteres == "H99": #Excepciones de H
                print("No se registra en el ICD10")
                codigo_valido = False
            elif primer_caracter == "H" and "0" <= primeros_3_carcteres[1] <= "5":
                descripcion = "Enfermedades del ojo y sus anexos"
            elif primer_caracter == "H" and codigo_ice10[1] >= "6":
                descripcion = "Enfermedades del oído y de la apófisis mastoides"
            elif primer_caracter == "I":
                descripcion = "Enfermedades del sistema circulatorio"
            elif primer_caracter == "J":
                descripcion = "Enfermedades del sistema respiratorio"
            elif primeros_3_carcteres == "K94" or primeros_3_carcteres == "K95" or primeros_3_carcteres == "K96" or primeros_3_carcteres == "K97" or primeros_3_carcteres == "K98" or primeros_3_carcteres == "K99": #Excepciones de K
                print("No se registra en el ICD10")
                codigo_valido = False
            elif primer_caracter == "K":
                descripcion = "Enfermedades del sistema digestivo"
            elif primer_caracter == "L":
                descripcion = "Enfermedades de la piel y del tejido subcutáneo"
        elif primer_caracter in m_z:
            monto_base = monto_base + 40000
            if primer_caracter == "M":
                descripcion = "Enfermedades del sistema osteomuscular y del tejido conjuntivo"
            elif primer_caracter == "N":
                descripcion = "Enfermedades del sistema genitourinario"
            elif primer_caracter == "O":
                descripcion = "Embarazo, parto y puerperio"
            elif primeros_3_carcteres == "P97" or primeros_3_carcteres == "P98" or primeros_3_carcteres == "P99": #Excepciones de P
                print("No se registra en el ICD10")
                codigo_valido = False
            elif primer_caracter == "P":
                descripcion = "Ciertas afecciones originadas en el período perinatal"
            elif primer_caracter == "Q":
                descripcion = "Malformaciones congénitas, deformidades y anomalías cromosómicas"
            elif primer_caracter == "R":
                descripcion = "Síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte"
            elif primeros_3_carcteres == "T99":  # Excepciones de T
                print("No se registra en el ICD10")
                codigo_valido = False
            elif primer_caracter == "S" or primer_caracter == "T":
                descripcion = "Traumatismos, envenenamientos y algunas otras consecuencias de causas externas"
            elif primeros_3_carcteres == "Y99":  # Excepciones de Y
                print("No se registra en el ICD10")
                codigo_valido = False
            elif primer_caracter == "V" or primer_caracter == "W" or primer_caracter == "X" or primer_caracter == "Y":
                descripcion = "Causas externas de morbilidad y de mortalidad"
            elif primer_caracter == "Z":
                descripcion = "Factores que influyen en el estado de salud y contacto con los servicios de salud"
        elif primer_caracter in u:
            monto_base = monto_base + 100000
            descripcion= "Códigos para propósitos especiales"
        else:
            print("Codigo no valido. Los codigos llevan mayúscula")
            codigo_valido = False
    else:
        print("Los codigos ICD10 llevan punto (.)")
        codigo_valido = False
else:
    print("No se registra en el ICD10")
    codigo_valido = False

#Salidas
if codigo_valido == True:
    total = ((int(codigo_ice10[4:]) * monto_base) / 100) + monto_base
    print("Beneficiario:",nombre_del_paciente)
    print("Codigo:",codigo_ice10)
    print("Capitulo:",descripcion)
    print("Monto a pagar:",total)






