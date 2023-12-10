# Verifico che di questa classe sia presente SOLO 1 istanza!
class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            print("Creating...")
            cls.__instance = super().__new__(cls)
        return cls.__instance


s1 = Singleton()
s2 = Singleton()

print(s1)
print(s2)
