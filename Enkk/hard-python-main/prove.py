import json
import time


with open("deadge.json") as f:
    data = json.load(f)


def take_anno_mese(f_anno, f_mese):
    for anno, anno_vals in data.items():
        if anno == str(f_anno):
            for mese, mese_vals in anno_vals.items():
                if mese == f_mese.capitalize():
                    count_morti_mese = 0
                    for giorno, giorno_vals in mese_vals.items():
                        print("-" * 50)
                        print(f"anno: {anno}")
                        print(f"mese: {mese}")
                        print(f"giorno: {giorno}")

                        for persona in giorno_vals:
                            print(persona["name"])
                        print("morti", len(giorno_vals))
                        count_morti_mese += len(giorno_vals)
    time.sleep(0.2)
    print("morti mese:", count_morti_mese)


take_anno_mese(1992, "january")
