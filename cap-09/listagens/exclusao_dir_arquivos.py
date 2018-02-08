import os
# Cria um arquivo e o fecha imediatamente
open("morimbundo.txt","w").close()
os.mkdir("vago")
os.rmdir("vago")
os.remove("morimbundo.txt")