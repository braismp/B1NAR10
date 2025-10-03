# PROYECTO: TRADUCTOR DE ESPAÑOL A BINARIO (B1NAR10)
# PROGRAMADOR: BRAISM.P
# FECHA: 03/10/2025

import argparse
from translator import text_to_binary, binary_to_text

def main():
    parser = argparse.ArgumentParser(description="Traductor sencillo Español <-> Binario")
    sub = parser.add_subparsers(dest="command")
    
    enc = sub.add_parser("encode", help="Texto -> Binario")
    enc.add_argument("text", nargs="?", help="Texto a convertir. Si falta, se lee por stdin.")
    enc.add_argument("-e", "--encoding",default="utf-8", help="Codificación (por defecto utf-8)")
    enc.add_argument("-c", "--per-char", action="store_true", help="Agrupar por caracter")
    
    dec = sub.add_parser("decode", help="Binario -> Texto")
    dec.add_argument("binary", nargs="?", help="Cadena binaria. Si falta, se lee por stdin.")
    dec.add_argument("-e", "--encoding", default="utf-8", help="Codificación para decodificar")
    
    args = parser.parse_args()
    
    if args.command == "encode":
        text = args.text or input("Introduce el texto a convertir: ")
        output = text_to_binary(text, encoding=args.encoding, per_char=args.per_char)
        print(output)
    elif args.command == "decode":
        bin_input = args.binary or input("Introduce la cadena binaria (Bytes por espacios o '|'): ")
        try:
            output = binary_to_text(bin_input,encoding=args.encoding)
        except ValueError as e:
            print("Error:", e)
            return(0)
        print(output)
        
        
if __name__ == "__main__":
    main()