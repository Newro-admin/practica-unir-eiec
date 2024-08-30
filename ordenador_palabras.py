import sys
import argparse

def ordenar_lista(elementos, reverso=False):
    return sorted(elementos, reverse=reverso)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ordena una lista de palabras.")
    parser.add_argument('palabras', nargs='+', help="Palabras para ordenar")
    parser.add_argument('-r', '--reverso', action='store_true', help="Ordenar en orden descendente")
    args = parser.parse_args()

    palabras_ordenadas = ordenar_lista(args.palabras, reverso=args.reverso)
    
    print("Lista ordenada:")
    for palabra in palabras_ordenadas:
        print(palabra)