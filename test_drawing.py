import serial
import serial.tools.list_ports # pour la communication avec le port série
import turtle
import math

liste_a = [];
liste_t = [];
liste_a = [] # liste pour stocker les valeurs d'acceleration
liste_t = []
t_acquisition = 10.0 # en s
amax =2 # en g
amin= -2 # en g

# Fonction pour la récupération des données série venant de la carte Arduino
def recup_port_Arduino() :
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if 'Arduino Due Prog. Port' in p.description :
            mData = serial.Serial(p.device,115200)
    print(mData.is_open) # Affiche et vérifie que le port est ouvert
    print(mData.name) # Affiche le nom du port
    return mData

def pythagore(x1,y1,x2,y2):
    a = math.pow((x2-x1),2)
    b = math.pow((y2-y1),2)
    c=a+b
    return math.sqrt(c)

def angle(x1,y1,x2,y2):
    a = abs(y2-y1)
    hypo = pythagore(x1,y1,x2,y2)
    return math.degrees(math.acos(a/hypo))

Data =recup_port_Arduino() #récupération des données
tut = turtle.Pen()

print(pythagore(17,10,30,30))
print(angle(17,10,30,30))

while(True) :
    line1 = str(Data.readline());
    line1 = line1[2:-5];
    print (line1) 
    if(';' in line1) :
        #temp_line = point précédente pour avoir le point de départ de notre ligne 
        #line1 = point suivant ou point de fin de notre ligne
        
        #vérification si grande différence de Z = lévé de stylo donc changement de lettre ou mot 
        x,y = line1.split(";")
        # if() :
        # elif():
        # elif():
        # else :
        tut.forward(abs(int(x)))
        tut.left(45)
    temp_line = line1
        # Remettre l'angle dans le sens de base en ajoutant ou retirant l'angle donné
    
    
# on retire les caractères d'espacement en début et fin de chaîne
listeDonnees = line1.strip()
# on sépare les informations reçues séparées par les espaces et on stocke ces informations dans une liste pour chacune de lignes
listeDonnees = line1.split()
print (listeDonnees)

