import time
import sys
from functools import lru_cache

"""
senza lru_cache int=200 il sistema si blocca!
con lru_cache operazione eseguita in meno di 1 secondi
"""
sys.setrecursionlimit(1500)


@lru_cache
def fib(n: int) -> int:
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)


start_time = time.process_time()
fib(1000)
end_time = time.process_time()
print("Esecuzione in:", (end_time - start_time))
