def main():
    print("Salve e benvenuto nella mia funzione spesa...")
    
def mia_funzione(x:int, y:int) -> int:
    lista = ["pomodori", "carote", "coca-cola"]
    for val in lista:
        print( f'''
        devo comperare
        {val}: numero {x+y}''')
    print()
    print("PS: Se non vedi il saluto è perchè questo è un modulo")

if __name__=="__main__":
    main()

mia_funzione(5,3)
