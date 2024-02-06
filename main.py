from tools import *

def processLine(line):
    # Dividir la línea en partes
    parts = line.strip().split(",")

    # Extraemos los datos que vamos a necesitar
    IPv4 = parts[5]
    IPv6 = parts[0].split("/")[0] # para obtener solamente la parte que nos interesa trabajar
    secondName = parts[2]
    
    # Generamos las nuevas IP's
    newIPv4 = convertIPv4ToHex(IPv4)
    newIPv6 = convertIPv6ToDecimal(IPv6)
    
    # Armamos la nueva linea
    newLine = secondName + "," + newIPv6 + "," + newIPv4 + "\n"
    
    return newLine

def processFile(inputFile, outputFile):
    # Abrir archivos de entrada y salida
    with open(inputFile, "r") as IF, open(outputFile, "w") as OF:

        for line in IF:
            newLine = processLine(line)
            OF.write(newLine)

# Archivo de entrada y salida
inputFile = "prueba.txt"
outputFile = "nuevoPrueba.txt"

# Procesar el archivo
processFile(inputFile, outputFile)