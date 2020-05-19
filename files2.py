import os
import shutil
 
class Prueba :
    def __init__(self, pathfile, sendfile):
        self._File = pathfile
        self._Folder = sendfile

    def getImagesMarked(self):
        try:
            with open(self._File) as reader:
                line = reader.readline()
                print(line)
                while line != '':
                    _tokens = line.split(' ')
                    if(os.path.isfile(_tokens[0])):
                        shutil.move(_tokens[0], self._Folder)
                        print("Move File : "+_tokens[0]+" [+] Ruta > "+self._Folder)
                        line = reader.readline()
        except:
            print("Error de rutas incorrectas")    
        finally:
            reader.close()

test = Prueba("lolo.txt", "pox/")
test.getImagesMarked()