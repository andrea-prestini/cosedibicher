from functools import lru_cache


@lru_cache()
def fibo(number):
    if number == 1:
        return 1
    elif number == 2:
        return 1
    elif number > 2:
        return fibo(number-1) + fibo(number-2)


for number in range(1, 100):
    print(number, ":", fibo(number), "-->", (fibo(number+1) / fibo(number)))


print("soluzione stampata")
