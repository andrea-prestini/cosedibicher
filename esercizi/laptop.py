#!/usr/bin/python3

def laptop_nuovo(ram, cpu, antivirus=False):
    print("il portatile avrà le seguenti caratteristiche:")
    print("RAM\n" + ram)
    print("Cpu\n" + cpu)
    if antivirus is True:
        print("hai comprato anche un antivirus")


laptop_nuovo("16G", "i7")
laptop_nuovo("16G", "i7", antivirus=True)
