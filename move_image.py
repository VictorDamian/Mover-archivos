##############
### - Python 3.7.8
### - Meve imagenes/archivos de un directorio a otro
##############
import os
import shutil

class MoveImage:
    # contructor
    def __init__(self, pathImg, pathTxt):
        self._pathTxt = pathTxt
        self._pathImg = pathImg

    # obten una lista con los archivos existentes
    def getNameToImgs(self):
        nameImg = os.listdir(self._pathImg)
        print(nameImg)
        return nameImg

    def getNameFromTxt(self):
        listTxt=[]
        # lectura del archivo
        read = open(self._pathTxt,'r')
        # lee cada linea 
        print('\n---- Nombres existentes en TXT ----\n')
        for line in read:
            # elimina los espacios
            space = line.split(' ')
            # elimina la diagonal solo de la colum' 0
            slash = space[0].split('\\')
            # almacena en una lista colum' 1
            listTxt.append(slash[1])    
            print(slash[1])
        return listTxt
    # move las imagenes al dirctorio
    def setImgToDir(self):
        listMarker = self.getNameFromTxt()
        print('\n---- Lista de archivos en el directorio ----\n')
        for img in self.getNameToImgs():
            if img in listMarker:
                # directorio destino
                shutil.move(self._pathImg+img, "img/destino/")

# directorio de archivos, archivo a leer
move = MoveImage(pathImg='img/', pathTxt='archivo.txt')
move.setImgToDir()