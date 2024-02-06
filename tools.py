def hexToDecimal(hex):
    # Convertir números hexadecimales a decimal, recibe como parametro el hexadecimal a convertir y la base en el que se tiene que interpretar lo recibido
    return int(hex, 16)

def decimalToHex(decimal):
    # Convertir números decimales a hexadecimal, quita el prefijo "0x" y convierte a mayusculas todas las letras
    return hex(decimal)[2:].upper()

def convertIPv4ToHex(IPv4):
    parts = IPv4.split(".")
    
    convertedIPv4 = ""
    
    for cont, part in enumerate(parts):
        convertedIPv4 += str(decimalToHex(int(part)))
        
        if cont != len(parts) - 1:
            convertedIPv4 += "."
    
    return convertedIPv4

def convertIPv6ToDecimal(IPv6):
    parts = IPv6.split(":")
    
    convertedIPv6 = ""
    
    for cont, part in enumerate(parts):
        convertedIPv6 += str(hexToDecimal(part))
        
        if cont != len(parts) - 1:
            convertedIPv6 += ":"
    
    return convertedIPv6