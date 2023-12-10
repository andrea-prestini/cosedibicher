import time

contatore = 0
while True:
    print("il contatore vale ", contatore)
    contatore += 1
    time.sleep(1)
    if contatore > 10:
        print("esco dal LOOP!")
        break