import os
import zipfile


# archivio = zipfile.ZipFile("BICHER.zip", "a")
archivio = zipfile.ZipFile(str(os.getcwd())+"/"+"BICHER.zip", "w")
# # archivio.write("elenco",compress_type=zipfile.ZIP_DEFLATED)


for cartelle, sottocartelle, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith("py"):
            archivio.write(file, compress_type=zipfile.ZIP_DEFLATED)

archivio.close()
print(archivio.namelist())    
print(list(x for x in archivio.namelist() if x.startswith("c")))
print(list(x for x in archivio.namelist() if "dizio" in x))
print(list(x for x in archivio.namelist() if "Cartelle" in x or "cartelle" in x))
# archivio.extractall(#percorso)

