import serial
import serial.tools.list_ports # pour la communication avec le port série
import turtle
import math

# TODO : Changer le nom des fonctions
# TODO : Travailler sur l'optimisation
# TODO : Travailler sur le nom des variables
# TODO : créer une fonction de draw...

temps = 120
def getDistance(ax, ay, vx = 0, vy = 0) :
    dx = vx + ax * math.pow(temps, 2)
    dy = vy + ay * math.pow(temps, 2)
    return dx, dy

def getVitesse(ax, ay, vx = 0, vy = 0) :
    newVx = vx + ax * temps
    newVy = vy + ay * temps
    return newVx, newVy

def calculDistance(ax, ay, vx = 0, vy = 0) :
    dx, dy = getDistance(ax, ay, vx, vy)
    return math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))

def angle(ax, ay, vx = 0, vy = 0) :
    dx, dy = getDistance(ax, ay, vx, vy)
    hypo = calculDistance(ax, ay, vx, vy)
    return int(math.degrees(math.acos(abs(dx)/hypo)))

def recup_port_Arduino() :
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if 'IOUSBHostDevice' in p.description :
            mData = serial.Serial(p.device,115200)
    print(mData.is_open) # Affiche et vérifie que le port est ouvert
    print(mData.name) # Affiche le nom du port
    return mData

data = recup_port_Arduino() #récupération des données
pen = turtle.Pen()

print(calculDistance(17, 10))
print(angle(17, 10))
vx = 0
vy = 0

while(True) :
    line = str(data.readline())
    line = line[2:-5]
    print (line) 
    if(';' in line) :
        #if(v0) :
        x,y = line.split(";")
        x = int(x)/10
        y = int(y)/10
        # temp_line = point précédente pour avoir le point de départ de notre ligne 
        # line1 = point suivant ou point de fin de notre ligne
        # vérification si grande différence de Z = lévé de stylo donc changement de lettre ou mot
        dx, dy = getDistance(x, y, vx, vy)
        #
        # if(hauteur_base == 0) :
        #     hauteur_base = z
        angle_to_move = angle(x, y, vx, vy)
        if(dx > 0 and dy > 0) :
            print("1")
            pen.left(angle_to_move)
            pen.forward(abs(int(dx)))
            pen.right(angle_to_move)
        elif(dx > 0 and dy < 0) :
            print("2")
            pen.right(angle_to_move)
            pen.forward(abs(int(dx)))
            pen.left(angle_to_move)
        elif(dx < 0 and dy > 0) :
            print("3")
            pen.left(180-angle_to_move)
            pen.forward(abs(int(dx)))
            pen.right(180-angle_to_move)
        else :
            print("4")
            pen.right(180-angle_to_move)
            pen.forward(abs(int(dx)))
            pen.left(180-angle_to_move)
        vx, vy = getVitesse(x, y, vx, vy)
        print(vx)
        print(vy)

        # Remettre l'angle dans le sens de base en ajoutant ou retirant l'angle donné