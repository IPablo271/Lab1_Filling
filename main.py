from gl import *

glCreateWindow(1000, 1000)
glColor(0, 1, 0)



listapuntos = [(165,380),(185,360),(180,330),(207,345),(233,330),(230,360),(250,380),(220,385),(205,410),(193,383)]
lista2 = [(321, 335), (288, 286) ,(339, 251),(374, 302)]


lista3 = [(377, 249) , (411, 197), (436, 249)]
lista4 = [(413, 177),(448, 159),(502, 88),(553, 53),(535, 36),(676, 37),(660, 52),(750, 145),(761, 179),(672, 192),(659, 214),(615, 214),(632, 230),(580, 230),
(597, 215),(552, 214),(517, 144),(466, 180)]

lista5 = [(682, 175),(708, 120),(735, 148),(739, 170)]
          
    

fillfigure2(listapuntos)
fillfigure2(lista2)
fillfigure2(lista3)
fillfigure2(lista4)
glColor(1, 1, 1)
fillfigure2(lista5)

glFinish()



