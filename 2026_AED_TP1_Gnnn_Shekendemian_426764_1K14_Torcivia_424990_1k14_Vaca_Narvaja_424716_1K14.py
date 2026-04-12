#Entrada
#Datos del paciente#El código ICD10 que identifica la enfermedad (o sea, el diagnósti
#El monto base a pagar por el tratamiento
nombre_del_paciente = input("Ingrese el nombre del paciente: ")
codigo_ice10 = input("Ingrese el codigo del ICE10: ")
monto_base = int(input("Ingrese el monto base a pagar: "))

#Requerimiento
monto_base += 25000
print("El monto base sumados a $25.000 es: ", monto_base)
if "A" <= codigo_ice10[0] <= "L":
    monto_base += 25000
    total = ((int(codigo_ice10[4]) * monto_base)/100) +monto_base
    if codigo_ice10[0] == "A" or codigo_ice10[0] == "B":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10: Ciertas enfermedades infecciosas y parasitarias")
        print("Importe total: ", total)
    elif codigo_ice10[0] == "C":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10: Tumores [neoplasias] ")
        print("Importe total: ", total)
    elif codigo_ice10[0] == "D" and codigo_ice10[1] <= "4" or codigo_ice10[1] >= "0":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10: Tumores [neoplasias]")
        print("Importe total: ", total)
   #elif codigo_ice10[0] == "D" and codigo_ice10[1] == "9":
    #    print("No se registra en el ICD10")
    #elif codigo_ice10[1,2] == "49":
     #   print("No se registra en el ICD10")
    elif codigo_ice10[0] == "D" and codigo_ice10[1] >= "5" and codigo_ice10[0] != "9":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10: Enfermedades de la sangre y de los órganos hematopoyéticos, y ciertos trastornos que afectan el mecanismo de la inmunidad")
        print("Importe total: ", total)
    elif codigo_ice10[0] == "E":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10: Enfermedades endocrinas, nutricionales y metabólicas ")
        print("Importe total: ", total)
    elif codigo_ice10[0] == "F":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10: Trastornos mentales y del comportamiento")
        print("Importe total: ", total)
    elif codigo_ice10[0] == "G":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10: Enfermedades del sistema nervioso")
        print("Importe total: ", total)
    elif codigo_ice10[0] == "H" and codigo_ice10[1] < "6":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10: Enfermedades del ojo y sus anexos")
        print("Importe total: ", total)
    elif codigo_ice10[0] == "H" and codigo_ice10[1] >= "6":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10: Enfermedades del oído y de la apófisis mastoides")
        print("Importe total: ", total)
    elif codigo_ice10[0] == "I":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10: Enfermedades del sistema circulatorio ")
        print("Importe total: ", total)
    elif codigo_ice10[0] == "J":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10: Enfermedades del sistema respiratorio")
        print("Importe total: ", total)
    elif codigo_ice10[0] == "K":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10: Enfermedades del sistema digestivo")
        print("Importe total: ", total)
    elif codigo_ice10[0] == "L":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10: Enfermedades de la piel y del tejido subcutáneo")
        print("Importe total: ", total)

elif "M" <= codigo_ice10[0] <= "Z" and codigo_ice10[0] != "U":
    monto_base += 40000
    total = ((int(codigo_ice10[4]) * monto_base) / 100) + monto_base
    if codigo_ice10[0] == "M":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10: Enfermedades del sistema osteomuscular y del tejido conjuntivo")
        print("Importe total: ", total)
    elif codigo_ice10[0] == "N":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10: Enfermedades del sistema genitourinario")
        print("Importe total: ", total)
    elif codigo_ice10[0] == "O":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10: Embarazo, parto y puerperio ")
        print("Importe total: ", total)
    elif codigo_ice10[0] == "P":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10: Ciertas afecciones originadas en el período perinatal")
        print("Importe total: ", total)
    elif codigo_ice10[0] == "Q":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10: Malformaciones congénitas, deformidades y anomalías cromosómicas")
        print("Importe total: ", total)
    elif codigo_ice10[0] == "R":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10:  Síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte")
        print("Importe total: ", total)
    elif codigo_ice10[0] == "S" or codigo_ice10[0] == "T":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10:  Traumatismos, envenenamientos y algunas otras consecuencias de causas externas ")
        print("Importe total: ", total)
    elif codigo_ice10[0] == "V" or codigo_ice10[0] == "W" or codigo_ice10[0] == "X" or codigo_ice10[0] == "Y":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10:  Causas externas de morbilidad y de mortalidad ")
        print("Importe total: ", total)
    elif codigo_ice10[0] == "Z":
        print("Nombre del paciente: ", nombre_del_paciente)
        print("Codigo CD10 del diagnóstico,", codigo_ice10)
        print("Descipción del capitulo ICD10: Factores que influyen en el estado de salud y contacto con los servicios de salud")
        print("Importe total: ", total)

elif codigo_ice10[0] == "U":
    monto_base += 100000
    total = ((int(codigo_ice10[4]) * monto_base) / 100) + monto_base
    print("Nombre del paciente: ", nombre_del_paciente)
    print("Codigo CD10 del diagnóstico,", codigo_ice10)
    print("Descipción del capitulo ICD10: Códigos para propósitos especiales")
    print("Importe total: ", total)

