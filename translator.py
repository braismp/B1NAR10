# PROYECTO: TRADUCTOR DE ESPAÑOL A BINARIO (B1NAR10)
# PROGRAMADOR: BRAISM.P
# FECHA: 03/10/2025

import re
from typing import Optional

def text_to_binary(text: str, encoding:  str = "utf-8", per_char: bool = False, sep: str = "") -> str:
    
    if per_char:
        parts = []
        for ch in text:
            ch_bytes = ch.encode(encoding)
            parts.append(sep.join(format(b, "08b") for b in ch_bytes))
        return " | ".join(parts)
    else:
        b = text.encode(encoding)
        return sep.join(format(byte, "08b") for byte in b)
    
def binary_to_text(binary: str, encoding: str = "utf-8") -> str:
    
    """
    Convierte una cadena de bits a texto usando la codificación indicada.
    Acepta entradas con bytes separados por espacios o '|'.
    Ejemplo válido:
      "01101000 01101111 01101100 01100001"
      "01101101 | 01100001 11000011 10110001 | 01100001"
    """
    
    s = binary.strip()
    if not s:
        return ""
    
    tokens = re.split(r"[\s|]+", s)
    bytes_list = []
    for tok in tokens:
        if tok == "":
            continue
        if not all(c in "01" for c in tok):
            raise ValueError(f"Token inválido (Solo se permite 0 y 1): {tok!r}")
        
        if len(tok) % 8 == 0:
            for i in range(0, len(tok), 8):
                bytes_list.append(int(tok[i : i + 8], 2))
                
        else:
            raise ValueError(f"Token con longitud no múltiplo de 8 bits: {tok!r}")
        
    try:
        return bytes(bytes_list).decode(encoding)
    except UnicodeDecodeError as e:
        raise ValueError(f"Los bytes no forman una secencia válida en {encoding}: {e}")