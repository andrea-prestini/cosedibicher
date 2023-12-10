import time


my_dict = {
    "1992": {
        "1": [
            {"name": "andrea", "paese": "esine"},
            {"name": "eleonora", "paese": "leno"},
            {"name": "roberto", "paese": "breno"},
            {"name": "filippo", "paese": "breno"},
        ],
        "2": [
            {"name": "franco", "paese": "esine"},
            {"name": "giovanni", "paese": "leno"},
            {"name": "mario", "paese": "breno"},
            {"name": "elisa", "paese": "breno"},
        ],
        "3": [
            {"name": "francesca", "paese": "esine"},
            {"name": "paolo", "paese": "leno"},
            {"name": "adriano", "paese": "breno"},
            {"name": "denis", "paese": "breno"},
        ],
        "4": [
            {"name": "sara", "paese": "esine"},
            {"name": "davide", "paese": "leno"},
            {"name": "giovanni", "paese": "breno"},
            {"name": "livio", "paese": "breno"},
        ],
        "5": [
            {"name": "simone", "paese": "esine"},
            {"name": "franca", "paese": "leno"},
            {"name": "marco", "paese": "breno"},
            {"name": "ugo", "paese": "breno"},
        ],
        "6": [
            {"name": "isabella", "paese": "esine"},
            {"name": "giuseppe", "paese": "leno"},
            {"name": "anna", "paese": "breno"},
            {"name": "roberta", "paese": "breno"},
        ],
        "7": [
            {"name": "giovanna", "paese": "esine"},
            {"name": "marcello", "paese": "leno"},
            {"name": "ancilla", "paese": "breno"},
            {"name": "nicola", "paese": "breno"},
        ],
        "8": [
            {"name": "elisabetta", "paese": "esine"},
            {"name": "elisa", "paese": "leno"},
            {"name": "gianluigi", "paese": "breno"},
            {"name": "ottavio", "paese": "breno"},
        ],
        "9": [
            {"name": "fabio", "paese": "esine"},
            {"name": "simonetta", "paese": "leno"},
            {"name": "nicoletta", "paese": "breno"},
            {"name": "iride", "paese": "breno"},
        ],
        "10": [
            {"name": "rino", "paese": "esine"},
            {"name": "pietro", "paese": "leno"},
            {"name": "tommaso", "paese": "breno"},
            {"name": "elvino", "paese": "breno"},
        ],
    }
}


for k, v in my_dict.items():
    for giorno, persone in v.items():
        for i in range(4):
            print(f'''
                    anno: {k}
                    giorno: {giorno}
                    nome: {persone[i]["name"]}
                    paese: {persone[i]["paese"]}
                        ''')
            time.sleep(0.5)
