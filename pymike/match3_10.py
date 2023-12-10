# def http_error(status_code):
#     match status_code:
#         case 200 | 201 | 202:
#             print("Success")
#         case 400 | 401 | 404:
#             print("Client Error")
#         case 500 | 501 | 503:
#             print("Server Error")
#         case _:
#             print("Unknow error")

# status_code = 401
# http_error(status_code)


# def move(action:str):
#     match action.split():
#         case ["go", ("forward" | "backward" | "left" | "right") as direction]:
#             print(f"Character is running ({direction})")
#         case ["jump", ("up" | "forward") as direction]:
#             print(f"Character is jumping ({direction}")
#         case _:
#             print(f"Action not supported")

# while True:
#     action = input("Enter action: ")
#     move(action)

from dataclasses import dataclass


@dataclass
class Element:
    name: str
    color: str


@dataclass
class Other:
    name: str


def validate_el(element):
    match element:
        case Element(name="Cubo"):
            print("Hai inserito un cubo!")
        case Element(name="Sfera", color="Verde"):
            print("Hai inserito una sfera!")
        case Element(name, color):
            print(f"Hai inserito: {name} di colore {color}")
        case _:
            print("Oggetto non valido!")


y_name = "andrea"

match y_name:
    case  "andrea":
        print("Ciao amico mio")
    case "federica":
        print("Ciao carissima amica")
    case "eleonora":
        print("Benvenuta nella nostra umile dimora")
    case _:
        print("Mi dispiace, non ti conosco!")