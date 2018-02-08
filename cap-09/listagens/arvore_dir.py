import os
tamanho = 0

for raiz, diretorios, arquivos in os.walk('z'):
     print("\nCaminho:", raiz)
     for d in diretorios:
         print("   %s/" % d)
     for f in arquivos:
         print("   %s" % f)
         tamanho += os.path.getsize(os.path.join(raiz, f))
     print("%d diretório(s), %d arquivo(s)" % (len(diretorios), len(arquivos)))
     print('Tamanho %d bytes' % tamanho)
     tamanho = 0