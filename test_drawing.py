import serial
import serial.tools.list_ports # pour la communication avec le port série
import turtle
import math

hauteur_base = 0
temp_line = None

# Fonction pour la récupération des données série venant de la carte Arduino
def recup_port_Arduino() :
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if 'IOUSBHostDevice' in p.description :
            mData = serial.Serial(p.device,115200)
    print(mData.is_open) # Affiche et vérifie que le port est ouvert
    print(mData.name) # Affiche le nom du port
    return mData

def pythagore(x1, y1, x2, y2):
    a = math.pow((x2-x1), 2)
    b = math.pow((y2-y1), 2)
    c = a+b
    return math.sqrt(c)

def angle(x1, y1, x2, y2):
    a = abs(y2-y1)
    hypo = pythagore(x1, y1, x2, y2)
    return int(math.degrees(math.acos(a/hypo)))

Data =recup_port_Arduino() #récupération des données
tut = turtle.Pen()

print(pythagore(17, 10, 30, 30))
print(angle(17, 10, 30, 30))

while(True) :
    line1 = str(Data.readline())
    line1 = line1[2:-5]
    print (line1) 
    if(';' in line1) :
        if(temp_line) :
            # temp_line = point précédente pour avoir le point de départ de notre ligne 
            # line1 = point suivant ou point de fin de notre ligne
            # vérification si grande différence de Z = lévé de stylo donc changement de lettre ou mot
            x,y = line1.split(";")
            x = int(x)/10
            y = int(y)/10
            x_old,y_old = temp_line.split(";")
            x_old = int(x_old)/10
            y_old = int(y_old)/10
            # if(hauteur_base == 0) :
            #     hauteur_base = z
            angle_to_move = angle(x,y,x_old,y_old)
            if(x>x_old and y>y_old) :
                print("1")
                tut.left(angle_to_move)
                tut.forward(abs(int(x)))
                tut.right(angle_to_move)
            elif(x<x_old and y<y_old) :
                print("2")
                tut.right(angle_to_move)
                tut.forward(abs(int(x)))
                tut.left(angle_to_move)
            elif(x<x_old and y>y_old) :
                print("3")
                tut.left(180-angle_to_move)
                tut.forward(abs(int(x)))
                tut.right(180-angle_to_move)
            else :
                print("4")
                tut.right(180-angle_to_move)
                tut.forward(abs(int(x)))
                tut.left(180-angle_to_move)
        temp_line = line1

        # Remettre l'angle dans le sens de base en ajoutant ou retirant l'angle donné